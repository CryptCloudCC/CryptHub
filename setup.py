import os
import subprocess


CRYPTHUB_COMPONENTS: dict = {

    ## CryptUI ##
    "CryptUI": {
        "name": "CryptUI",
        "description": "CryptHub's User Interface system built using Deno and React.",
        "url": "https://github.com/CryptCloudCC/CryptUI"
        },

    ## CryptDB ##
    "CryptDB": {
        "name": "CryptDB",
        "description": "CryptHub's database management system.",
        "url": "https://github.com/CryptCloudCC/CryptDB"
        },

    ## CryptBucket ##
    "CryptBucket": {
        "name": "CryptBucket",
        "description": "CryptHub's storage solution based on Amazon S3.",
        "url": "https://github.com/CryptCloudCC/CryptBucket"
    },

    ## CryptFlows ##
    "CryptFlows": {
        "name": "CryptFlows",
        "description": "Task orchestrator handling workflow logic using Directed Acyclic Graphs (DAGs).",
        "url": "https://github.com/CryptCloudCC/CryptFlows"
    },

    ## CryptComms ##
    "CryptComms": {
        "name": "CryptComms",
        "description": "CryptHub's comprehensive communication system.",
        "url": "https://github.com/CryptCloudCC/CryptComms"
    },

    ## CryptAuth ##


}

def clone_component_repos_to_components_directory():

    ## Establish the relative path of the components directory
    ## `CryptHub-Platform/CryptHub-Components`
    CRYPTHUB_COMPONENTS_DIRECTORY: str = "CryptHub-Platform/CryptHub-Components"

    for component in CRYPTHUB_COMPONENTS:
        subprocess.run(f"git clone {CRYPTHUB_COMPONENTS[component]['url']}", shell=True, cwd=CRYPTHUB_COMPONENTS_DIRECTORY)
        subprocess.run(f"cd {CRYPTHUB_COMPONENTS_DIRECTORY}/{CRYPTHUB_COMPONENTS[component]['name']} && git checkout {CRYPTHUB_COMPONENTS[component]['branch']}", shell=True, cwd=CRYPTHUB_COMPONENTS_DIRECTORY)

def main():
    pass
