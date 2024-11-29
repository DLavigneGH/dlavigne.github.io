import json
import os

import requests
from config import BASE_URL, DIRS_DOOM2, HEADERS, JSON_FILE_PATH


def fetch_textfile(wad_id):
    """Fetch the textfile content for a given WAD ID"""
    params = {
        "action": "get",
        "id": wad_id,
        "out": "json",
    }

    try:
        response = requests.get(BASE_URL, params=params, verify=False)

        if response.status_code == 200:
            data = response.json()
            if "content" in data and "textfile" in data["content"]:
                return data["content"]["textfile"]
    except Exception as e:
        print(f"Error fetching textfile for WAD ID {wad_id}: {e}")

    return "No textfile available"


def fetch_wad_data():
    """Fetch WAD data from Doomworld API, preserving existing metadata"""
    if os.path.exists(JSON_FILE_PATH):
        print(f"Using existing data from {JSON_FILE_PATH}")
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
        return merge_wad_data(existing_data)
    else:
        return initial_wad_data_fetch()


def initial_wad_data_fetch():
    """Perform first-time data fetch from the API"""
    print("First-time data fetch from the API...")
    merged_data = []

    for directory in DIRS_DOOM2:
        params = {
            "action": "getfiles",
            "name": directory,
            "out": "json",
        }

        try:
            response = requests.get(
                BASE_URL, headers=HEADERS, params=params, verify=False
            )

            if response.status_code == 200:
                data = response.json()
                if isinstance(data, dict) and "content" in data:
                    files_data = data["content"].get("file", [])
                    if isinstance(files_data, list):
                        for new_wad in files_data:
                            new_wad["Completed"] = "No"
                            wad_id = new_wad.get("id", None)
                            if wad_id:
                                new_wad["textfile"] = fetch_textfile(wad_id)
                            merged_data.append(new_wad)
        except Exception as e:
            print(f"Error fetching data for {directory}: {e}")

    save_wad_data(merged_data)
    return merged_data


def merge_wad_data(existing_data):
    """Merge existing data with new API data"""
    merged_data = []

    for directory in DIRS_DOOM2:
        params = {
            "action": "getfiles",
            "name": directory,
            "out": "json",
        }

        try:
            response = requests.get(
                BASE_URL, headers=HEADERS, params=params, verify=False
            )

            if response.status_code == 200:
                data = response.json()
                if isinstance(data, dict) and "content" in data:
                    files_data = data["content"].get("file", [])
                    if isinstance(files_data, list):
                        for new_wad in files_data:
                            # Find if this WAD already exists
                            existing_wad = next(
                                (
                                    wad
                                    for wad in existing_data
                                    if wad["id"] == new_wad.get("id")
                                ),
                                None,
                            )

                            if existing_wad:
                                # Preserve existing metadata
                                new_wad["Completed"] = existing_wad.get(
                                    "Completed", "No"
                                )
                                new_wad["textfile"] = existing_wad.get("textfile", "")
                            else:
                                # Default for new WADs
                                new_wad["Completed"] = "No"

                            # Fetch textfile if not already present
                            wad_id = new_wad.get("id", None)
                            if wad_id and not new_wad.get("textfile"):
                                new_wad["textfile"] = fetch_textfile(wad_id)

                            merged_data.append(new_wad)
        except Exception as e:
            print(f"Error merging data for {directory}: {e}")

    save_wad_data(merged_data)
    return merged_data


def save_wad_data(data):
    """Save WAD data to JSON file"""
    try:
        with open(JSON_FILE_PATH, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)
        print("Data successfully written to 'merged_data.json'")
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")


def parse_wads_data(data):
    """Extract relevant WAD information"""
    return [
        {
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
            "textfile": wad.get("textfile", "No textfile available"),
            "Completed": wad.get("Completed", "No"),
            "Directory": wad.get("Directory", "Unknown"),
        }
        for wad in data
    ]
