import json
import os


def get_all_params_and_possible_values(type):
    base_dir = os.path.dirname(__file__)
    directory = base_dir + "\\" + type + "\\"
    data_dict = {}
    for filename in os.listdir(directory):
        print(f"checking : {filename}")
        if filename.endswith('.json'):
            with open(directory + filename, 'r') as fp:
                json_dict = json.load(fp)
                for key, val in json_dict.items():
                    data_dict.setdefault(key, [])
                    if isinstance(val, list):
                        for elem in val:
                            if elem not in data_dict[key]:
                                data_dict[key].append(elem)
                    else:
                        if not val in data_dict[key]:
                            data_dict[key].append(val)
#        print(data_dict)
    return data_dict

if __name__ == "__main__":
    type = "testplan"
    print(get_all_params_and_possible_values(type))