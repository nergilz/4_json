import os
import json
import sys
from json.decoder import JSONDecodeError


def load_data(path_to_file):
    with open(os.path.join(path_to_file), 'r', encoding='utf-8') as file_handler:
        try:
            json_content = json.load(file_handler)
        except JSONDecodeError:
            print(' Script_Error: This is not json-file or the file is empty.')
        else:
            return json_content


def pretty_print_json(json_content):
    print(json.dumps(json_content, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == '__main__':
    try:
        path_to_file = sys.argv[1]
        json_content = load_data(path_to_file)
        if json_content is not None:
            pretty_print_json(json_content)
    except FileNotFoundError:
        print(' Script_Error: File or path "{0}" not found.'.format(path_to_file))
    except IndexError:
        print(' Script_Error: No file name for reading.')
