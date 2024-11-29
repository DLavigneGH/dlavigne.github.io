# Base URL for the Doomworld API
BASE_URL = "https://test.doomworld.com/idgames/api/api.php?"

# List of directories to query
DIRS_DOOM2 = [
    "levels/doom2/0-9/",
    # Uncomment other directories as needed
    # "levels/doom2/a-c/",
    # "levels/doom2/d-f/",
    # "levels/doom2/g-i/",
    # "levels/doom2/j-l/",
    # "levels/doom2/p-r/",
    # "levels/doom2/m-o/",
    # "levels/doom2/s-u/",
    # "levels/doom2/v-z/"
]

# Headers for API requests
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# JSON file path for storing WAD data
JSON_FILE_PATH = "merged_data.json"
