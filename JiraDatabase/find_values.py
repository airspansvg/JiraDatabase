import json
import os

type = "subtask"
param = "Product support"

package_dir = os.path.dirname(__file__)
directory = package_dir + "\\" + type + "\\"
param_list = []
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        with open(directory + filename, 'r') as fp:
            json_dict = json.load(fp)
            if json_dict.get(param):
                param_list.append(json_dict.get(param))
final_list = list(set(param_list))
list_of_tuple = [(item, item) for item in final_list]
print(list_of_tuple)
