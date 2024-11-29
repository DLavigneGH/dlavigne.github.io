import sys
import webbrowser
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QWidget, QMessageBox
from PySide6.QtCore import Qt
from ui.wadui import Ui_wadList
from ui.wad_item_ui import Ui_wadInfo

BASE_URL = 'https://doomworld.com/idgames/api/api.php?'

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

class DoomWadRandomizer(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Setup headless mode for Selenium WebDriver
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Enable headless mode
        chrome_options.add_argument("--disable-gpu")  # Disable GPU (recommended for headless mode)
        #chrome_options.add_argument("--window-size=1920x1080")  # Optional: Set window size for rendering

        # Setup Selenium WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        
        # Setup main window UI
        self.main_ui = Ui_wadList()
        self.main_ui.setupUi(self)
        
        # Setup WAD item dialog
        self.wad_item_ui = Ui_wadInfo()
        self.wad_item_widget = QWidget()
        self.wad_item_ui.setupUi(self.wad_item_widget)

        # Add the WAD item widget to the scroll area's layout
        self.main_ui.verticalLayout.addWidget(self.wad_item_widget)
        
        # Connect Randomize button
        self.main_ui.pushRandomize.clicked.connect(self.fetch_random_wad)
        
        # Labels for WAD details
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

        # Store current WAD URL
        self.current_wad_url = ""
    
    def fetch_random_wad(self):
        self.wad_item_ui.visitedCheckBox.setChecked(False)
        try:
            # Open random WAD page
            self.driver.get('https://www.doomworld.com/idgames/')
            
            # Click random button
            random_button = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Random')]")
            random_button.click()
            
            # Find filename
            filename_element = self.driver.find_element(By.CLASS_NAME, 'filelist_field2')
            filename = filename_element.text.strip()
            print(filename)
            
            params = {
                "action": "get",
                "file": filename,
                "out": "json",
            }

            # API request for WAD details
            response = requests.get(BASE_URL, headers=HEADERS, params=params, verify=False)
            data = response.json()
            files_data = data["content"]
            
            # Update labels
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
                self.labels[label_name].setText(f"{data_key.capitalize()} : {str(files_data.get(data_key, 'N/A'))}")

            # Enable the Download button after successful fetch
            self.main_ui.pushDownload.setEnabled(True)
            self.main_ui.pushSaveJson.setEnabled(True)

            # Disconnect previous connections before connecting again
            self.main_ui.pushSaveJson.clicked.disconnect()
            self.main_ui.pushDownload.clicked.disconnect()

            # Connect Open URL button
            self.main_ui.pushDownload.clicked.connect(lambda: self.open_wad_url(filename))

            # Connect Save button to the save_data function
            self.main_ui.pushSaveJson.clicked.connect(self.save_data)

            # Store current WAD URL
            self.current_wad_url = files_data.get('url', '')
            
            # Set description
            self.description_browser.setText(files_data.get('textfile', 'No description available'))
        
        except Exception as e:
            print(f"Error fetching WAD: {e}")
    
    def open_wad_url(self, filename):
        print(filename)
        if self.current_wad_url:
            webbrowser.open(f'https://www.quaddicted.com/files/idgames/{filename}')
    
    def closeEvent(self, event):
        # Close the Selenium WebDriver when the application closes
        self.driver.quit()
        event.accept()

    def save_data(self):
        # Collect data from the populated fields
        visited_status = "Yes"

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
            "visited": visited_status

        }

        # Path to your JSON file
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

            # Optionally show a success message
            QMessageBox.information(self, "Success", "Data saved successfully!")
            self.main_ui.pushSaveJson.setEnabled(False)
            self.wad_item_ui.visitedCheckBox.setChecked(True)  # Check the box

        except Exception as e:
            # Show an error message if something goes wrong
            QMessageBox.critical(self, "Error", f"Failed to save data: {e}")

def main():
    app = QApplication(sys.argv)
    window = DoomWadRandomizer()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()