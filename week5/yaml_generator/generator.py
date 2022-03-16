import os
import sys
import json
import yaml


def generate_dict(path: str):
    items = os.listdir(path)

    if len(items) == 0:
        return None

    final_list = list()

    for item in items:
        item_path = path + os.sep + item
        if os.path.isdir(item_path):
            final_list.append(
                {item: generate_dict(item_path)}
            )
        else:
            with open(item_path, 'r') as file:
                content = file.read()
                
                try: content = json.loads(content)
                except: ...

                try: content = yaml.safe_load(content)
                except: ...
                    
            final_list.append({item: content})
    
    return final_list


def write_yaml(data: dict) -> None:
    with open('file_struct.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)


if __name__ == '__main__':
    top_dir_path = sys.argv[1]
    data = {top_dir_path: generate_dict(top_dir_path)}
    write_yaml(data)
