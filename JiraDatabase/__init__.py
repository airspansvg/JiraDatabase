import json
import os

package_dir = os.path.dirname(__file__)

def load_jira_data(type, ticket_key):
    with open(os.path.join(package_dir, f"{type}\\{ticket_key}.json"), 'r') as file:
        return json.load(file)

def get_all_bs_hw_types():
    directory = package_dir + "\\subtask\\"
    all_hw_list = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            with open(directory + filename, 'r') as fp:
                try:
                    all_hw_list.append(json.load(fp)["BS Hardware Type"])
                except Exception as e1:
                    print(f"Exception : {e1}")
    return all_hw_list