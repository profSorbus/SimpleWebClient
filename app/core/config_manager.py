import configparser
import logging
import os
import pathlib
import sys

from app.utils.tools import listContains

logger = logging.getLogger(__name__)


DEFAULT_CONF = str(
    pathlib.Path(__file__).parent.parent.resolve() / "conf" / "config.ini"
)
MANDATORY_SECTIONS = ["APP"]
MANDATORY_KEYS = [
    "api_url",
]


class ConfigManager:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(DEFAULT_CONF)
        self._valid()

    def _valid(self) -> None:
        """
        This function checks if the config file has a valid format or not. It must contain [APP],
        [DATABASE] section and keys such as LOG_DIR, DB_TYPE, ETC. If the config file does not
        contain the necessary information for launching the app. We consider this is a fatal error, and
        we stopped the program
        :return:
        """

        # check if the config has all mandatory sections
        if not listContains(MANDATORY_SECTIONS, self.config.sections()):
            logger.error(
                f"The configuration file is not valid, it misses mandatory sections: {MANDATORY_SECTIONS}"
            )
            sys.exit(1)
        allKeys = []
        # loop through all mandatory section and get all keys for each section
        for section in MANDATORY_SECTIONS:
            for key in dict(self.config.items(section)).keys():
                allKeys.append(key)
        # check if the config file has all mandatory keys
        if not listContains(MANDATORY_KEYS, allKeys):
            logger.error(
                f"The configuration file is not valid, it misses mandatory keys: {MANDATORY_KEYS}"
            )
            sys.exit(1)

    def showAllConfig(self) -> None:
        """
        This function prints all available conf field in the std out
        :return:
        """
        for section in self.config.sections():
            print(section)
            for key in self.config[section]:
                print((key, self.config[section][key]))
