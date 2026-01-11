import pathlib
import requests

from app.core.config_manager import ConfigManager


confFilePath = pathlib.Path.cwd() / "app" / "conf" / "config.ini"

configManager = ConfigManager()

print("Your API URL is : " + configManager.config["APP"]["API_URL"])

API_URL = configManager.config["APP"]["API_URL"]


def contactAPI():
    try:
        response = requests.get(API_URL + "YOUR_API_ENDPOINT")
        print(response.json())
    except requests.exceptions.InvalidSchema:
        print(
            "Requests could not find the API. Are you sure you replaced the API url in the config.ini file ??"
        )


if __name__ == "__main__":
    contactAPI()
