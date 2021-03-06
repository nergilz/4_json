import json
import sys
from json.decoder import JSONDecodeError


def load_data(path_to_file):
    with open(path_to_file, 'r') as file_handler:
        json_content = json.load(file_handler)
        return json_content


def output_dump_json(json_content):
    json_content_for_print = json.dumps(
        json_content,
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    )
    return json_content_for_print


if __name__ == '__main__':
    try:
        path_to_file = sys.argv[1]
        json_content = load_data(path_to_file)
        print(output_dump_json(json_content))
    except IndexError:
        print(' Script_Error: No filename for reading.')
    except FileNotFoundError:
        print(' Script_Error: File or path "{0}" not found.'.format(path_to_file))
    except JSONDecodeError:
        print(' Script_Error: This is not json-file or file is empty.')
