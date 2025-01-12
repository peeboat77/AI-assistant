import os 
import requests
from dotenv import load_dotenv
from langchain_core.documents import Document

load_dotenv()

github_token = os.getenv("GITHUB_TOKEN")

def fetch_github(username, repo, endpoint):
    url = f"https://api.github.com/repos/{username}/{repo}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {github_token}"
    }
    response = requests.get(url, headers=headers)
    
    print(response.status_code)  # Should not be 401
    print(response.json())

    if response.status_code == 200:
        data = response.json
    else:
        print(f"Error fetching data from GitHub: {response.status_code}")
        return []
    print(data)
    return data

username = "peeboat77"
repo = "Weather-Application"
endpoint = "issues"

fetch_github(username, repo, endpoint)

