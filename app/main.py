import pathlib
import requests

from app.core.config_manager import ConfigManager


confFilePath = pathlib.Path.cwd() / "app" / "conf" / "config.ini"

configManager = ConfigManager()

print("Your API URL is : " + configManager.config["APP"]["API_URL"])

API_URL = configManager.config["APP"]["API_URL"]


def contactAPI():
    response = requests.get(API_URL + "YOUR_API_ENDPOINT")
    print(response.json())


if __name__ == "__main__":
    contactAPI()
