from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class WadWebScraper:
    def __init__(self):
        # Setup headless mode for Selenium WebDriver
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")

        # Setup Selenium WebDriver
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), 
            options=chrome_options
        )

    def get_random_wad_filename(self):
        """
        Scrape a random WAD filename from Doomworld

        Returns:
            str: Filename of a random WAD
        """
        try:
            # Open random WAD page
            self.driver.get('https://www.doomworld.com/idgames/')
            
            # Click random button
            random_button = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Random')]")
            random_button.click()
            
            # Find filename
            filename_element = self.driver.find_element(By.CLASS_NAME, 'filelist_field2')
            return filename_element.text.strip()
        
        except Exception as e:
            print(f"Web Scraping Error: {e}")
            return None

    def close(self):
        """Close the WebDriver"""
        self.driver.quit()