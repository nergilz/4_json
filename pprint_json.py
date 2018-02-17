import os
import json
import sys


def load_data(path_to_file):
    with open(os.path.join(path_to_file), 'r', encoding='utf-8') as data_handler:
        json_content = json.load(data_handler)
        return json_content


def pretty_print_json(json_content):
    print(json.dumps(json_content, ensure_ascii=False, sort_keys=True, indent=2))


path_to_file = sys.argv[1]

if __name__ == '__main__':
    json_content = load_data(path_to_file)
    pretty_print_json(json_content)
