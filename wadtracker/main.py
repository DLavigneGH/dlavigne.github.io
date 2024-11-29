# main.py
import random
import sys
import webbrowser

from api_handler import fetch_wad_data, parse_wads_data, save_wad_data
from config import JSON_FILE_PATH
from PySide6.QtWidgets import QApplication, QMessageBox, QScrollArea, QWidget
from ui.wad_item_ui import Ui_wadInfo
from ui.wadui import Ui_wadList
from utils.file_operations import clear_layout, create_container_widget


class WADCatalogueUI(QWidget, Ui_wadList):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.wads_json = fetch_wad_data()

        # Connect the 'pushRandomize' button to the randomize function
        self.pushRandomize.clicked.connect(self.randomize_wad)

        self.scroll_area_levels = self.findChild(QScrollArea, "scrollAreaLevels")
        self.scroll_area_levels_content = self.findChild(
            QWidget, "scrollAreaLevels_Content"
        )
        self.scroll_area_levels.setWidget(self.scroll_area_levels_content)

        self.container_widget = None
        self.container_layout = None

        wad_info = parse_wads_data(self.wads_json)
        self.populate_wad_list(wad_info)

    def create_wad_widget(self, wad, index):
        """Create a widget to display WAD information"""
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
        ui_form.textFile.setPlainText(textfile)

        # Directly set the checkbox state based on the 'Completed' value
        is_completed = wad.get("Completed", "No") == "Yes"
        ui_form.visitedCheckBox.setChecked(is_completed)

        # Connect checkbox signal to update method, passing the index
        ui_form.visitedCheckBox.stateChanged.connect(
            lambda state: self.update_wad_completed_state(index, state)
        )

        # Add separator
        separator = QWidget()
        separator.setFixedHeight(2)
        separator.setStyleSheet("background-color: lightgray;")
        ui_form.wadItemLayout.addWidget(separator)
        wad_widget.setLayout(ui_form.wadItemLayout)

        return wad_widget

    def populate_wad_list(self, wads):
        """Populate the scroll area with WAD widgets"""
        self.container_widget, self.container_layout = create_container_widget()

        clear_layout(self.scroll_area_levels_content.layout())

        for index, wad in enumerate(wads):
            wad_widget = self.create_wad_widget(wad, index)
            self.container_layout.addWidget(wad_widget)

        self.scroll_area_levels.setWidget(self.container_widget)

    def show_error(self, message):
        """Show error messages to the user"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def update_wad_completed_state(self, index, state):
        """Update the completed status of a WAD"""
        # Convert Qt.CheckState to 'Yes' or 'No'
        completed_status = "Yes" if state == 2 else "No"

        # Update the JSON data
        self.wads_json[index]["Completed"] = completed_status

        # Save updated data back to the JSON file
        save_wad_data(self.wads_json)

    def randomize_wad(self):
        """Select a random WAD where 'Completed' = 'No' and open its URL"""
        # Filter WADs that are not completed
        incomplete_wads = [
            wad for wad in self.wads_json if wad.get("Completed") == "No"
        ]

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
        else:
            self.show_error("No URL available for the selected WAD.")


# Main application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WADCatalogueUI()
    window.show()
    sys.exit(app.exec())
