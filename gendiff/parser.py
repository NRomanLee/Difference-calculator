import json
import yaml
def parse_file(file_path):
    with open(file_path, "r") as file:
        if file_path.endswith((".yml",".yaml")):
                return yaml.safe_load(file)
        elif file_path.endswith(".json"):
             return json.load(file)
        