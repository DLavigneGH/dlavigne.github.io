import requests

BASE_URL = 'https://www.doomworld.com/idgames/api/api.php?'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

class WadApiService:
    @staticmethod
    def get_wad_details(filename):
        """
        Fetch WAD details from the IDGames API
        
        Args:
            filename (str): The filename of the WAD to retrieve

        Returns:
            dict: WAD details from the API
        """
        params = {
            "action": "get",
            "file": filename,
            "out": "json",
        }

        try:
            response = requests.get(BASE_URL, headers=HEADERS, params=params, verify=False)
            #response = requests.get('https://www.doomworld.com/idgames/api/api.php?action=get&id=14151&out=json', headers=HEADERS, verify=False)
            data = response.json()
            return data["content"]
        except Exception as e:
            print(f"API Request Error: {e}")
            return None