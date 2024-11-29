# isort: skip_file
# fmt:off
import webbrowser
import random
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
    "levels/doom2/a-c/",
    "levels/doom2/d-f/",
    "levels/doom2/g-i/",
    "levels/doom2/j-l/",
    "levels/doom2/p-r/",
    "levels/doom2/m-o/",
    "levels/doom2/s-u/",
    "levels/doom2/v-z/"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

JSON_FILE_PATH = "merged_data.json"


class WADCatalogueUI(QWidget, Ui_wadList):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.wads_json = self.fetch_wad_data()

        # Connect the 'pushRandomize' button to the randomize function
        self.pushRandomize.clicked.connect(self.randomize_wad)

        self.scroll_area_levels = self.findChild(QScrollArea, "scrollAreaLevels")
        self.scroll_area_levels_content = self.findChild(
            QWidget, "scrollAreaLevels_Content"
        )
        self.scroll_area_levels.setWidget(self.scroll_area_levels_content)

        self.container_widget = None
        self.container_layout = None

        wad_info = self.parse_wads_data(self.wads_json)
        self.populate_wad_list(wad_info)

    def fetch_wad_data(self):
        """Fetch WAD data from Doomworld API, preserving existing metadata"""
        if os.path.exists(JSON_FILE_PATH):
            print(f"Using existing data from {JSON_FILE_PATH}")
            with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
                existing_data = json.load(file)

            # If we already have data, fetch new data and merge
            merged_data = self.merge_wad_data(existing_data)
            return merged_data
        else:
            # First-time fetch: get data from API and create initial JSON
            print(f"First-time data fetch from the API...")
            merged_data = []

            for e in DIRS:
                params = {
                    "action": "getfiles",
                    "name": e,
                    "out": "json",
                }

                response = requests.get(
                    BASE_URL, headers=HEADERS, params=params, verify=False
                )

                if response.status_code == 200:
                    try:
                        data = response.json()
                        if isinstance(data, dict) and "content" in data:
                            files_data = data["content"].get("file", [])
                            if isinstance(files_data, list):
                                for new_wad in files_data:
                                    # Default for new WADs
                                    new_wad['Completed'] = 'No'

                                    # Fetch textfile
                                    wad_id = new_wad.get('id', None)
                                    if wad_id:
                                        new_wad['textfile'] = self.fetch_textfile(wad_id)

                                    merged_data.append(new_wad)
                        else:
                            print(f"No 'content' key in the response for {e}.")
                    except ValueError:
                        print(f"Failed to parse JSON for {e}: {response.text}")
                else:
                    print(
                        f"Failed to fetch data for {e} (Status Code: {response.status_code})"
                    )

            # Save the initial data
            try:
                with open(JSON_FILE_PATH, "w", encoding="utf-8") as outfile:
                    json.dump(merged_data, outfile, indent=4, ensure_ascii=False)
                print("Initial data successfully written to 'merged_data.json'")
            except Exception as e:
                print(f"An error occurred while writing to file: {e}")

            return merged_data

    def merge_wad_data(self, existing_data):
        """Merge existing data with new API data"""
        merged_data = []

        for e in DIRS:
            params = {
                "action": "getfiles",
                "name": e,
                "out": "json",
            }

            response = requests.get(
                BASE_URL, headers=HEADERS, params=params, verify=False
            )

            if response.status_code == 200:
                try:
                    data = response.json()
                    if isinstance(data, dict) and "content" in data:
                        files_data = data["content"].get("file", [])
                        if isinstance(files_data, list):
                            for new_wad in files_data:
                                # Find if this WAD already exists in existing data
                                existing_wad = next(
                                    (wad for wad in existing_data if wad['id'] == new_wad.get('id')),
                                    None
                                )

                                if existing_wad:
                                    # Preserve existing metadata
                                    new_wad['Completed'] = existing_wad.get('Completed', 'No')
                                    new_wad['textfile'] = existing_wad.get('textfile', '')
                                else:
                                    # Default for new WADs
                                    new_wad['Completed'] = 'No'

                                # Fetch textfile if not already present
                                wad_id = new_wad.get('id', None)
                                if wad_id and not new_wad.get('textfile'):
                                    new_wad['textfile'] = self.fetch_textfile(wad_id)

                                merged_data.append(new_wad)
                    else:
                        print(f"No 'content' key in the response for {e}.")
                except ValueError:
                    print(f"Failed to parse JSON for {e}: {response.text}")
            else:
                print(
                    f"Failed to fetch data for {e} (Status Code: {response.status_code})"
                )

        # Save the merged data, preserving existing metadata
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
                "Completed": wad.get("Completed", "No")
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
        print(f"Creating widget for WAD: {wad.get('title', 'Unknown')}, Completed: {wad.get('Completed', 'No')}")
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

        print(f"Completed status for {wad.get('title', 'Unknown')}: {wad.get('Completed', 'No')}")
        # Directly set the checkbox state based on the 'Completed' value
        is_completed = wad.get('Completed', 'No') == 'Yes'
        ui_form.visitedCheckBox.setChecked(is_completed)

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
        # Convert Qt.CheckState to 'Yes' or 'No'
        completed_status = 'Yes' if state == Qt.Checked.value else 'No'

        # Update the JSON data
        self.wads_json[index]["Completed"] = completed_status

        # Save updated data back to the JSON file
        self.save_wad_data()

    def save_wad_data(self):
        try:
            with open(JSON_FILE_PATH, "w", encoding="utf-8") as outfile:
                json.dump(self.wads_json, outfile, indent=4, ensure_ascii=False)
            print("Data successfully written to 'merged_data.json'")
        except Exception as e:
            print(f"An error occurred while writing to file: {e}")

    def randomize_wad(self):
        """Select a random WAD where 'Completed' = 'No' and open its URL."""
        # Filter WADs that are not completed
        incomplete_wads = [wad for wad in self.wads_json if wad.get("Completed") == "No"]

        if not incomplete_wads:
            self.show_error("No incomplete WADs found.")
            return

        # Select a random WAD from the incomplete ones
        random_wad = random.choice(incomplete_wads)

        # Get the URL of the selected WAD
        wad_url = random_wad.get("url", None)

        if wad_url:
            # Open the URL in the default browser
            webbrowser.open(wad_url)
            print(f"Opening URL: {wad_url}")
        else:
            self.show_error("No URL available for the selected WAD.")

# Main application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WADCatalogueUI()
    window.show()
    sys.exit(app.exec())
