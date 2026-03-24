import os

import requests

GITLAB_URL = "https://gitlab.data-al.de"
PRIVATE_TOKEN = os.environ["GITLAB_TOKEN"]
USERNAME = "Michael"


def get_merge_requests():
    url = f"{GITLAB_URL}/api/v4/merge_requests"
    headers = {"PRIVATE-TOKEN": PRIVATE_TOKEN}
    params = {
        "state": "opened",
        "scope": "all",
    }
    response = requests.get(url, headers=headers, params=params, timeout=10, verify=False)
    response.raise_for_status()
    return response.json()
