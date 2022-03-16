import os
import sys
import json
import yaml


def make_dir(dir: dict, path: str = os.getcwd()) -> None:
    for current_item, inner_data in dir.items():
        path += os.sep + current_item
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
            with open(path, 'w') as file:
                match current_item.split('.')[-1]:
                    case 'json':
                        file.write(json.dumps(inner_data, indent=2))
                    case 'yaml' | 'yml':
                        yaml.dump(inner_data, file, default_flow_style=False)
                    case _:
                        file.write(str(inner_data))


def scan_yaml(path: str) -> dict:
    with open(path, 'r') as file:
        return yaml.safe_load(file)


if __name__ == '__main__':
    yaml_path = sys.argv[1]
    files = scan_yaml(yaml_path)
    make_dir(files)
