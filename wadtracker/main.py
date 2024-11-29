import json
import sys

# isort: off
import requests
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QLabel, QScrollArea, QVBoxLayout, QWidget
from ui.wad_item_ui import Ui_Form
from ui.wadui import Ui_Dialog


class WADCatalogueUI(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Initialize the UI components from the .ui file

        # Find the scroll area and its content widget
        self.scroll_area_levels = self.findChild(QScrollArea, "scrollAreaLevels")
        self.scroll_area_levels_content = self.findChild(
            QWidget, "scrollAreaLevels_Content"
        )

        print("ScrollArea:", self.scroll_area_levels)
        print("ScrollArea Content:", self.scroll_area_levels_content)

        # Ensure the scroll area is set to resize its widget
        self.scroll_area_levels.setWidgetResizable(True)

        try:
            with open("some_file.json", "r", encoding="utf-8") as file:
                data = json.load(file)
            wads = self.parse_wads_data(data)
            self.populate_wad_list(wads)
        except Exception as e:
            print(f"Error in initialization: {e}")

    def parse_wads_data(self, data):
        wads = []
        file_data = data.get("content", {}).get("file", [])
        for wad in file_data:
            wad_info = {
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
            wads.append(wad_info)
        return wads

    def populate_wad_list(self, wads):
        print(f"Total WADs to display: {len(wads)}")

        if not wads:
            print("No WADs to display!")
            return

        # Create a container widget
        container_widget = QWidget()
        layout = QVBoxLayout(container_widget)
        layout.setAlignment(Qt.AlignTop)

        # Add each WAD to the layout
        for i, wad in enumerate(wads):
            print(f"Adding WAD {i + 1}: {wad.get('title', 'No Title')}")

            # Create a new widget for each WAD
            wad_widget = QWidget()
            wad_layout = QVBoxLayout(wad_widget)

            # Create labels for WAD details
            labels = [
                f"Id: {wad.get('id', 'N/A')}",
                f"Title: {wad.get('title', 'N/A')}",
                f"Filename: {wad.get('filename', 'N/A')}",
                f"Date: {wad.get('date', 'N/A')}",
                f"Size: {round(float(wad.get('size', 0)) / 1024, 2)} Mb",
                f"Author: {wad.get('author', 'N/A')}",
                f"Rating: {wad.get('rating', 'N/A')}",
                f"Votes: {wad.get('votes', 'N/A')}",
                f"Url: {wad.get('url', 'N/A')}",
                f"Description: {wad.get('description', 'N/A')}",
            ]

            for label_text in labels:
                label = QLabel(label_text)
                wad_layout.addWidget(label)

            # Add a separator (optional)
            separator = QWidget()
            separator.setFixedHeight(2)
            separator.setStyleSheet("background-color: lightgray;")
            wad_layout.addWidget(separator)

            # Add the WAD widget to the main layout
            layout.addWidget(wad_widget)

        # Set the container widget as the scroll area's widget
        self.scroll_area_levels.setWidget(container_widget)

        print(f"Layout has {layout.count()} widgets after adding WADs.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WADCatalogueUI()
    window.show()
    sys.exit(app.exec())
