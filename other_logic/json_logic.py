import json


def read_json(file):
    f = open(file, )

    data = json.load(f)

    f.close()

    return data



def edit_json(file, value1, char1):
    f = open(file, )
    data = json.load(f)

    data[value1] = char1
    with open(file, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)