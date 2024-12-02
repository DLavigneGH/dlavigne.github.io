import requests

BASE_URL = 'https://www.doomworld.com/idgames/api/api.php?'

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
        print(filename)
        params = {
            "action": "get",
            "file": filename,
            "out": "json",
        }
        try:
            response = requests.get(BASE_URL, params=params)
            data = response.json()
            return data["content"]
        except Exception as e:
            print(f"API Request Error: {e}")
            return None