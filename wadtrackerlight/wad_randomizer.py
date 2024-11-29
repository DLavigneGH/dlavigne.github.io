import sys
import webbrowser
import json
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from ui.wadui import Ui_wadList
from ui.wad_item_ui import Ui_wadInfo
from web_scraper import WadWebScraper
from api_service import WadApiService

class DoomWadRandomizer(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialize web scraper
        self.web_scraper = WadWebScraper()
        
        # Setup main window UI
        self.main_ui = Ui_wadList()
        self.main_ui.setupUi(self)
        
        # Setup WAD item dialog
        self.setup_wad_item_ui()
        
        # Connect buttons
        self.connect_buttons()
        
        # Store current WAD URL
        self.current_wad_url = ""
        
        # JSON file path for tracking visited WADs
        self.json_file_path = 'data.json'

    def setup_wad_item_ui(self):
        """Setup WAD item user interface"""
        self.wad_item_ui = Ui_wadInfo()
        self.wad_item_widget = QWidget()
        self.wad_item_ui.setupUi(self.wad_item_widget)

        # Add the WAD item widget to the scroll area's layout
        self.main_ui.verticalLayout.addWidget(self.wad_item_widget)

        # Create labels dictionary for easy access
        self.labels = {
            'idLabel': self.wad_item_ui.idLabel,
            'titleLabel': self.wad_item_ui.titleLabel,
            'filenameLabel': self.wad_item_ui.filenameLabel,
            'authorLabel': self.wad_item_ui.authorLabel,
            'dateLabel': self.wad_item_ui.dateLabel,
            'sizeLabel': self.wad_item_ui.sizeLabel,
            'ratingLabel': self.wad_item_ui.ratingLabel,
            'votesLabel': self.wad_item_ui.votesLabel,
            'urlLabel': self.wad_item_ui.urlLabel,
            'descriptionLabel': self.wad_item_ui.descriptionLabel,
        }
        
        self.description_browser = self.wad_item_ui.textFile

    def connect_buttons(self):
        """Connect UI buttons to their respective functions"""
        self.main_ui.pushRandomize.clicked.connect(self.fetch_random_wad)
        self.main_ui.pushDownload.setEnabled(False)
        self.main_ui.pushSaveJson.setEnabled(False)

    def is_wad_visited(self, filename):
            """
            Check if a WAD has been previously visited
            
            Args:
                filename (str): Filename of the WAD to check
            
            Returns:
                bool: True if WAD has been visited, False otherwise
            """
            # If the JSON file doesn't exist, return False
            if not os.path.exists(self.json_file_path):
                return False

            try:
                # Read the existing JSON file
                with open(self.json_file_path, 'r') as file:
                    visited_wads = json.load(file)
                
                # Check if the filename exists in the visited WADs
                for wad in visited_wads:
                    if wad.get('filename', '').strip() == filename.strip():
                        return True
                
                return False
            
            except Exception as e:
                print(f"Error checking visited WADs: {e}")
                return False
            
    def fetch_random_wad(self):
            """Fetch details of a random WAD"""
            self.wad_item_ui.visitedCheckBox.setChecked(False)
            
            try:
                # Get random WAD filename
                filename = self.web_scraper.get_random_wad_filename()
                if not filename:
                    raise Exception("Could not retrieve random WAD")

                # Check if WAD has been visited before
                is_visited = self.is_wad_visited(filename)
                self.wad_item_ui.visitedCheckBox.setChecked(is_visited)

                # Get WAD details from API
                files_data = WadApiService.get_wad_details(filename)
                if not files_data:
                    raise Exception("Could not retrieve WAD details")

                # Update UI labels
                self.update_wad_labels(files_data)

                # Enable download and save buttons
                self.main_ui.pushDownload.setEnabled(True)
                self.main_ui.pushSaveJson.setEnabled(True)

                # Disconnect previous connections before connecting again
                try:
                    self.main_ui.pushSaveJson.clicked.disconnect()
                    self.main_ui.pushDownload.clicked.disconnect()
                except TypeError:
                    # Ignore if no connections exist
                    pass

                # Connect Open URL and Save buttons
                self.main_ui.pushDownload.clicked.connect(lambda: self.open_wad_url(filename))
                self.main_ui.pushSaveJson.clicked.connect(self.save_data)

                # Store current WAD URL
                self.current_wad_url = files_data.get('url', '')
                
                # Set description
                self.description_browser.setText(files_data.get('textfile', 'No description available'))
            
            except Exception as e:
                print(f"Error fetching WAD: {e}")
                QMessageBox.warning(self, "Error", str(e))

    def update_wad_labels(self, files_data):
        """Update WAD labels with fetched data"""
        label_mapping = {
            'idLabel': 'id',
            'titleLabel': 'title',
            'filenameLabel': 'filename',
            'authorLabel': 'author',
            'dateLabel': 'date',
            'sizeLabel': 'size',
            'ratingLabel': 'rating',
            'votesLabel': 'votes',
            'urlLabel': 'url',
            'descriptionLabel': 'description'
        }
        
        for label_name, data_key in label_mapping.items():
            self.labels[label_name].setText(str(files_data.get(data_key, 'N/A')))

    def open_wad_url(self, filename):
        """Open WAD download URL in browser"""
        if self.current_wad_url:
            webbrowser.open(f'https://www.quaddicted.com/files/idgames/{filename}')

    
    def save_data(self):
        """Save WAD data to JSON file"""
        data = {
            "id": self.wad_item_ui.idLabel.text(),
            "title": self.wad_item_ui.titleLabel.text(),
            "filename": self.wad_item_ui.filenameLabel.text(),
            "author": self.wad_item_ui.authorLabel.text(),
            "date": self.wad_item_ui.dateLabel.text(),
            "size": self.wad_item_ui.sizeLabel.text(),
            "rating": self.wad_item_ui.ratingLabel.text(),
            "votes": self.wad_item_ui.votesLabel.text(),
            "url": self.wad_item_ui.urlLabel.text(),
            "description": self.wad_item_ui.descriptionLabel.text(),
            "visited": "Yes"
        }

        json_file_path = 'data.json'

        try:
            # Try to read the existing file and append the data
            try:
                with open(json_file_path, 'r') as file:
                    current_data = json.load(file)
            except FileNotFoundError:
                # If the file doesn't exist, create an empty list to start
                current_data = []

            # Append the new data to the existing data list
            current_data.append(data)

            # Write the updated data back to the JSON file
            with open(json_file_path, 'w') as file:
                json.dump(current_data, file, indent=4)

            # Show success message
            QMessageBox.information(self, "Success", "Data saved successfully!")
            self.main_ui.pushSaveJson.setEnabled(False)
            self.wad_item_ui.visitedCheckBox.setChecked(True)

        except Exception as e:
            # Show an error message if something goes wrong
            QMessageBox.critical(self, "Error", f"Failed to save data: {e}")

    def closeEvent(self, event):
        """Close WebDriver when application closes"""
        self.web_scraper.close()
        event.accept()