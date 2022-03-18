import os
import sys
import json
import yaml

from pprint import pprint


def make_dir(dir: dict, path: str = os.getcwd()) -> None:
    for current_item, inner_data in dir.items():
        # pprint(f"{current_item}: {inner_data}")
        path = os.path.join(path, current_item)
        if all((
            any((
                isinstance(inner_data, list),
                inner_data == None,
            )),
            len(current_item.split('.')) == 1,
        )):
            
            if not os.path.exists(path):
                os.mkdir(path)
            
            if inner_data != None:
                for item in inner_data:
                    make_dir(item, path)

        else:
            if inner_data['file_type'] is not None:
                path = '.'.join([path, inner_data['file_type']])
            with open(path, 'w') as file:
                match inner_data['file_type']:
                    case 'json':
                        file.write(json.dumps(inner_data['content'], indent=2))
                    case 'yaml' | 'yml':
                        yaml.dump(inner_data['content'], file, default_flow_style=False)
                    case _:
                        file.write(str(inner_data['content']))


def scan_yaml(path: str) -> dict:
    with open(path, 'r') as file:
        return yaml.safe_load(file)


if __name__ == '__main__':
    yaml_path = sys.argv[1]
    files = scan_yaml(yaml_path)
    make_dir(files)
