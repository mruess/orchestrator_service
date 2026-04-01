import os
import requests

JENKINS_URL = "https://jenkins.data-al.de"
JOB_NAME = "data-al%28Entwicklung10-2%29"


def trigger_build(branch_name, quartals_version="false"):
    user = os.environ["JENKINS_USER"]
    token = os.environ["JENKINS_TOKEN"]

    response = requests.post(
        f"{JENKINS_URL}/job/{JOB_NAME}/buildWithParameters",
        auth=(user, token),
        data={
            "BRANCH_NAME": branch_name,
            "QUARTALS_VERSION": quartals_version,
        },
        verify=False,
    )
    response.raise_for_status()
    return response.status_code


def get_last_successful_build():
    user = os.environ["JENKINS_USER"]
    token = os.environ["JENKINS_TOKEN"]

    response = requests.get(
        f"{JENKINS_URL}/job/{JOB_NAME}/lastSuccessfulBuild/api/json",
        auth=(user, token),
        verify=False,
    )
    response.raise_for_status()
    data = response.json()
    return data.get("description")


def get_last_build_for_branch(branch_name):
    user = os.environ["JENKINS_USER"]
    token = os.environ["JENKINS_TOKEN"]

    response = requests.get(
        f"{JENKINS_URL}/job/{JOB_NAME}/api/json?tree=builds[number,description,result]",
        auth=(user, token),
        verify=False,
    )
    response.raise_for_status()
    data = response.json()

    import json
    for build in data.get("builds", []):
        desc = build.get("description")
        if not desc:
            continue
        try:
            desc_json = json.loads(desc)
        except (json.JSONDecodeError, TypeError):
            continue
        if desc_json.get("branch") == branch_name:
            return desc_json

    return ""
