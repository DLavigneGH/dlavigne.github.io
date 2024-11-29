# isort: skip_file
# fmt:off
import json
import os
import sys

import requests
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMessageBox,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)
from ui.wad_item_ui import Ui_wadInfo
from ui.wadui import Ui_wadList

BASE_URL = "https://test.doomworld.com/idgames/api/api.php?"

# List of directories to query
DIRS = [
    "levels/doom2/0-9/",
    # "levels/doom2/a-c/",
    # "levels/doom2/d-f/",
    # "levels/doom2/g-i/",
    # "levels/doom2/j-l/",
    # "levels/doom2/p-r/",
    # "levels/doom2/m-o/",
    # "levels/doom2/s-u/",
    # "levels/doom2/v-z/"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

JSON_FILE_PATH = "merged_data.json"


class WADCatalogueUI(QWidget, Ui_wadList):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.wads_json = self.fetch_wad_data()  # Store loaded data here

        self.scroll_area_levels = self.findChild(QScrollArea, "scrollAreaLevels")
        self.scroll_area_levels_content = self.findChild(
            QWidget, "scrollAreaLevels_Content"
        )
        self.scroll_area_levels.setWidget(self.scroll_area_levels_content)

        self.container_widget = None
        self.container_layout = None

        self.wads_json = self.fetch_wad_data()
        wad_info = self.parse_wads_data(self.wads_json)
        self.populate_wad_list(wad_info)

    def fetch_wad_data(self):
        """Fetch WAD data from Doomworld API if JSON doesn't already exist"""
        # If the file exists, load the data from the file
        if os.path.exists(JSON_FILE_PATH):
            print(f"Using existing data from {JSON_FILE_PATH}")
            with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)
        else:
            print(f"Fetching new data from the API...")

            merged_data = []  # List to store all the results

            for e in DIRS:
                params = {
                    "action": "getfiles",
                    "name": e,
                    "out": "json",
                }

                response = requests.get(
                    BASE_URL, headers=HEADERS, params=params, verify=False
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
                                for wad in files_data:
                                    # Add the "Completed" key with "No" to each WAD data
                                    wad["Completed"] = "No"
                                    # Pre-fetch textfile content and add it to the WAD
                                    wad_id = wad.get("id", None)
                                    if wad_id:
                                        wad["textfile"] = self.fetch_textfile(
                                            wad_id
                                        )  # Add textfile directly
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
                with open(JSON_FILE_PATH, "w", encoding="utf-8") as outfile:
                    json.dump(merged_data, outfile, indent=4, ensure_ascii=False)
                print("Data successfully written to 'merged_data.json'")
            except Exception as e:
                print(f"An error occurred while writing to file: {e}")
            return merged_data

    def parse_wads_data(self, data):
        """Extract relevant WAD information and pre-fetch textfiles"""
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
                "textfile": wad.get("textfile", "No textfile available"),
            }
            for wad in data
        ]

    def fetch_textfile(self, wad_id):
        """Fetch the textfile content for a given WAD ID"""
        params = {
            "action": "get",
            "id": wad_id,
            "out": "json",
        }

        response = requests.get(BASE_URL, params=params, verify=False)

        if response.status_code == 200:
            try:
                data = response.json()
                if "content" in data and "textfile" in data["content"]:
                    return data["content"]["textfile"]  # Return the textfile content
                else:
                    print(f"No 'textfile' key found for WAD ID {wad_id}.")
            except ValueError:
                print(f"Failed to parse JSON for WAD ID {wad_id}: {response.text}")
        else:
            print(
                f"Failed to fetch textfile for WAD ID {wad_id} (Status Code: {response.status_code})"
            )

        return "No textfile available"  # Default if not found

    def create_wad_widget(self, wad, index):
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

        # Display the textfile in QTextBrowser if available
        textfile = wad.get("textfile", "No textfile available")
        ui_form.textFile.setPlainText(
            textfile
        )  # Assuming you have a QTextBrowser for this

        # Set checkbox state
        completed_state = (
            Qt.Checked if wad.get("Completed", "No") == "Yes" else Qt.Unchecked
        )
        ui_form.visitedCheckBox.setChecked(completed_state == Qt.Checked)

        # Connect checkbox signal to update method, passing the index
        ui_form.visitedCheckBox.stateChanged.connect(
            lambda state: self.update_wad_completed_state(index, state)
        )

        # Add a separator widget to the wadItemLayout
        separator = QWidget()
        separator.setFixedHeight(2)
        separator.setStyleSheet("background-color: lightgray;")
        ui_form.wadItemLayout.addWidget(separator)
        wad_widget.setLayout(ui_form.wadItemLayout)

        return wad_widget

    def populate_wad_list(self, wads):
        if not self.container_widget:
            self.container_widget = QWidget()
            self.container_layout = QVBoxLayout(self.container_widget)
            self.container_layout.setAlignment(Qt.AlignTop)

        self.clear_layout(self.scroll_area_levels_content.layout())

        for index, wad in enumerate(wads):  # Use enumerate to get the index
            wad_widget = self.create_wad_widget(wad, index)  # Pass index here
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
        """Show error messages to the user using QMessageBox."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def update_wad_completed_state(self, index, state):
        if state == Qt.Checked.value:
            self.wads_json[index]["Completed"] = "Yes"
            print("yes")
        else:
            self.wads_json[index]["Completed"] = "No"
            print("no")

        # Save updated data back to the JSON file
        self.save_wad_data()

    def save_wad_data(self):
        try:
            with open(JSON_FILE_PATH, "w", encoding="utf-8") as outfile:
                json.dump(self.wads_json, outfile, indent=4, ensure_ascii=False)
            print("Data successfully written to 'merged_data.json'")
        except Exception as e:
            print(f"An error occurred while writing to file: {e}")


# Main application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WADCatalogueUI()
    window.show()
    sys.exit(app.exec())
