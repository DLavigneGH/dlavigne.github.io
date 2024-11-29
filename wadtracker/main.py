# isort: skip_file
import json
import os
import sys

import requests
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMessageBox,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)
from ui.wad_item_ui import Ui_wadInfo  # Ensure you're importing your custom UI
from ui.wadui import Ui_wadList


class WADCatalogueUI(QWidget, Ui_wadList):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Initialize the UI components from the .ui file

        # Find the scroll area and its content widget
        self.scroll_area_levels = self.findChild(QScrollArea, "scrollAreaLevels")
        self.scroll_area_levels_content = self.findChild(
            QWidget, "scrollAreaLevels_Content"
        )
        self.scroll_area_levels.setWidget(self.scroll_area_levels_content)

        self.container_widget = None
        self.container_layout = None

        wads_json = self.fetch_wad_data()
        wad_info = self.parse_wads_data(wads_json)
        self.populate_wad_list(wad_info)

    def fetch_wad_data(self):
        """Fetch WAD data from Doomworld API if JSON doesn't already exist"""
        json_file_path = "merged_data.json"

        if os.path.exists(json_file_path):
            print(f"Using existing data from {json_file_path}")
            # If the file exists, load the data from the file
            with open(json_file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        else:
            print(f"Fetching new data from the API...")
            BASE_URL = "https://test.doomworld.com/idgames/api/api.php?"

            # List of directories you want to query
            DIRS = [
                "levels/doom2/0-9/",
                "levels/doom2/a-c/",
                "levels/doom2/d-f/",
                "levels/doom2/g-i/",
                "levels/doom2/j-l/",
                "levels/doom2/p-r/",
                "levels/doom2/m-o/",
                "levels/doom2/s-u/",
                "levels/doom2/v-z/",
            ]

            merged_data = []  # List to store all the results
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }

            # Make the GET request for each directory
            for e in DIRS:
                params = {
                    "action": "getfiles",  # API action to get the files (WADs)
                    "name": e,  # Directory to query
                    "out": "json",  # Request JSON format
                }

                # Make the GET request for the current directory
                response = requests.get(
                    BASE_URL, headers=headers, params=params, verify=False
                )

                # Check if the response is successful and contains data
                if response.status_code == 200:
                    try:
                        data = response.json()  # Get the JSON data from the response
                        if (
                            isinstance(data, dict) and "content" in data
                        ):  # Check if 'content' exists
                            files_data = data["content"].get("file", [])
                            if isinstance(files_data, list):
                                merged_data.extend(
                                    files_data
                                )  # Merge files data from this directory
                        else:
                            print(f"No 'content' key in the response for {e}.")
                    except ValueError:
                        print(f"Failed to parse JSON for {e}: {response.text}")
                else:
                    print(
                        f"Failed to fetch data for {e} (Status Code: {response.status_code})"
                    )

            # Write the merged data to a JSON file
            try:
                with open(json_file_path, "w", encoding="utf-8") as outfile:
                    json.dump(merged_data, outfile, indent=4, ensure_ascii=False)
                print("Data successfully written to 'merged_data.json'")
            except Exception as e:
                print(f"An error occurred while writing to file: {e}")
            return merged_data

    def parse_wads_data(self, data):
        return [
            {
                "id": wad.get("id", "Unknown"),
                "title": wad.get("title", "Unknown"),
                "filename": wad.get("filename", "Unknown"),
                "description": wad.get("description", "No description available"),
                "date": wad.get("date", "Unknown"),
                "size": wad.get("size", "Unknown"),
                "author": wad.get("author", "Unknown"),
                "rating": wad.get("rating", "Unknown"),
                "votes": wad.get("votes", "Unknown"),
                "url": wad.get("url", "Unknown"),
            }
            for wad in data
        ]

    def create_wad_widget(self, wad):
        """Create a widget to display WAD information using Ui_Form."""
        wad_widget = QWidget()
        ui_form = Ui_wadInfo()  # Instantiate the custom UI for each WAD item
        ui_form.setupUi(wad_widget)  # Set up the UI for this widget

        # Set the WAD details into the corresponding UI components
        ui_form.idLabel.setText(f"Id: {wad.get('id', 'N/A')}")
        ui_form.titleLabel.setText(f"Title: {wad.get('title', 'N/A')}")
        ui_form.filenameLabel.setText(f"Filename: {wad.get('filename', 'N/A')}")
        ui_form.dateLabel.setText(f"Date: {wad.get('date', 'N/A')}")
        ui_form.sizeLabel.setText(
            f"Size: {round(float(wad.get('size', 0)) / 1024, 2)} Mb"
        )
        ui_form.authorLabel.setText(f"Author: {wad.get('author', 'N/A')}")
        ui_form.ratingLabel.setText(f"Rating: {wad.get('rating', 'N/A')}")
        ui_form.votesLabel.setText(f"Votes: {wad.get('votes', 'N/A')}")
        ui_form.urlLabel.setText(f"Url: {wad.get('url', 'N/A')}")
        ui_form.descriptionLabel.setText(
            f"Description: {wad.get('description', 'N/A')}"
        )

        # Add a separator widget to the wadItemLayout
        separator = QWidget()
        separator.setFixedHeight(2)
        separator.setStyleSheet("background-color: lightgray;")
        ui_form.wadItemLayout.addWidget(separator)
        wad_widget.setLayout(ui_form.wadItemLayout)

        return wad_widget

    def populate_wad_list(self, wads):
        """Populate the scroll area with WAD widgets."""
        if not self.container_widget:
            self.container_widget = QWidget()
            self.container_layout = QVBoxLayout(self.container_widget)
            self.container_layout.setAlignment(Qt.AlignTop)

        self.clear_layout(self.scroll_area_levels_content.layout())

        for i, wad in enumerate(wads):
            wad_widget = self.create_wad_widget(wad)
            self.container_layout.addWidget(wad_widget)

        self.scroll_area_levels.setWidget(self.container_widget)

    def clear_layout(self, layout):
        """Clear widgets from a layout."""
        if layout:
            for i in reversed(range(layout.count())):
                widget = layout.itemAt(i).widget()
                if widget:
                    widget.deleteLater()

    def show_error(self, message):
        """Show error messages to the user using a message box."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WADCatalogueUI()
    window.show()
    sys.exit(app.exec())
