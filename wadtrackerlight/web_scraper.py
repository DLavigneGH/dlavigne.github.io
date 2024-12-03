from selenium.webdriver.common.by import By

import time
import undetected_chromedriver as uc

class WadWebScraper:
    """
    A class responsible for web scraping Doom WAD files from the Doomworld website.

    This class creates a headless Chrome browser instance using the undetected-chromedriver 
    to bypass bot detection and scrapes WAD data from Doomworld's idgames section.

    Attributes:
        driver (uc.Chrome): A headless Chrome WebDriver instance configured with custom options.

    Methods:
        __init__(): Initializes the Chrome driver, opens the Doomworld URL.
    """
    def __init__(self):
        # Create undetected Chrome driver
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = uc.Chrome(options=chrome_options)
        
        # Open URL
        self.driver.get("https://www.doomworld.com/idgames/")
        time.sleep(3)

    def get_random_wad_filename(self):
        """
        Scrape a random WAD filename from Doomworld

        Returns:
            str: Filename of a random WAD
        """
        try:
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
