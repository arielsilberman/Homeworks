import os
import json

print(f"Current dirfectory: {os.getcwd()}")
os.chdir(os.path.dirname(__file__))

config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}

config_filename = "app_config.json"

try:
    with open(config_filename, "w") as file:
        file.write(str(config))
    print("Configuration file created: app_config.json")
except Exception as e:
    print(f"Error ocurred: {e}")
