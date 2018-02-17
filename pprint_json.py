import os
import json
import sys


def load_data(filepath):
    with open(os.path.join(filepath), 'r', encoding='utf-8') as filehandler:
        data_read = json.load(filehandler)
        return data_read


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2))


arg_path = sys.argv[1]

if __name__ == '__main__':
    data = load_data(arg_path)
    pretty_print_json(data)
