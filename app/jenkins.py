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
    )
    response.raise_for_status()
    return response.status_code
