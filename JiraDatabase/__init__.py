import json
import os

package_dir = os.path.dirname(__file__)

def load_jira_data(type, ticket_key):
    with open(os.path.join(package_dir, f"{type}\\{ticket_key}.json"), 'r') as file:
        return json.load(file)
