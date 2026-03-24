import requests

GITLAB_URL = "https://gitlab.data-al.de"
PRIVATE_TOKEN = "YOUR_GITLAB_TOKEN"  # TODO: replace with real token
USERNAME = "BuildSystem"


def get_merge_requests():
    url = f"{GITLAB_URL}/api/v4/merge_requests"
    headers = {"PRIVATE-TOKEN": PRIVATE_TOKEN}
    params = {
        "state": "opened",
        "scope": "all",
    }
    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()
    return response.json()
