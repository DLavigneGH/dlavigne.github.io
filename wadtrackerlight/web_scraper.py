from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

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
        __init__(): Initializes the Chrome driver, opens the Doomworld URL, and handles verification.
        handle_verification(driver): Processes any necessary verification steps during webpage access.
    """
    def __init__(self):

        # Create undetected Chrome driver
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--disable-quic")
        self.driver = uc.Chrome(options=chrome_options)
        # Open URL
        self.driver.get("https://www.doomworld.com/idgames/")
        time.sleep(3)
        # Handle verification
        self.handle_verification(self.driver)

    def handle_verification(self, driver):
        """This is to bypass the anti-bot Cloudfare detection

        Args:
            driver (uc.Chrome): The Chrome WebDriver instance used for web scraping.

        Raises:
            TimeoutException: If the expected verification element does not appear within the timeout.
            NoSuchElementException: If the necessary verification button or element is not found.
        """
        try:
            # Wait for Logo Assembly image
            WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'img[alt="Logo Assembly"]'))
            )
            time.sleep(3)
        except (TimeoutException, NoSuchElementException):
            try:
                # Check for Verify button
                verify_button = driver.find_element(By.CSS_SELECTOR, 'input[value*="Verify"]')
                verify_button.click()
            except NoSuchElementException:
                # Fallback to manual captcha handling (you might need to customize this)
                pass


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