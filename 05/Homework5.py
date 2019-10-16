import json


# check the type of data in list or dict
def def_type(value):
    type = None
    if isinstance(value, int):
        type = 'int'
    elif isinstance(value, float):
        type = 'float'
    elif isinstance(value, str):
        type = 'str'
    else:
        print("[Error]: unexpected basic data type, data = {}".format(value))
        exit(1)

    return type


# restore the data from string to original type before serialized
def convert_type(unit):
    if unit[1] == 'int':
        return int(unit[0])
    elif unit[1] == 'float':
        return float(unit[0])
    elif unit[1] == 'str':
        return str(unit[0])


# serialize the data
def serializer(data):
    data_str = ''
    if isinstance(data, list):
        data_str = data_str + 'list' + '\n'
        for i in range(len(data)):
            t = def_type(data[i])
            data_str = data_str + str(data[i]) + '_' + t + '\t'
        return data_str[:-1]
    elif isinstance(data, dict):
        data_str = data_str + 'dict' + '\n'
        keys = ''
        values = ''
        for key in data.keys():
            key_type = def_type(key)
            keys = keys + key + '_' + key_type + '\t'
            value_type = def_type(data[key])
            values = values + str(data[key]) + '_' + value_type + '\t'
        data_str = data_str + keys[:-1] + '\n' + values[:-1]
        return data_str


# deserialize data read from file
def deserializer(lines):
    if len(lines) == 0:
        return None
    elif lines[0] == 'list':
        data_restored = []
        if len(lines) > 1:
            lists = lines[1].split('\t')
            for list in lists:
                data_restored.append(convert_type(list.split('_')))
    elif lines[0] == 'dict':
        data_restored = {}
        if len(lines) > 1:
            keys = lines[1].split('\t')
            values = lines[2].split('\t')
            keys_restored = []
            values_restored = []
            for key in keys:
                keys_restored.append(convert_type(key.split('_')))
            for value in values:
                values_restored.append(convert_type(value.split('_')))
            data_restored = dict(zip(keys_restored, values_restored))
    return data_restored


# compare if 2 data structure are the same
def my_compare(ds1, ds2):
    if type(ds1) != type(ds2):
        return False

    if len(ds1) != len(ds2):
        return False
    if isinstance(ds1, list):
        for i in range(len(ds1)):
            if ds1[i] != ds2[i] or type(ds1[i]) != type(ds2[i]):
                return False
    if isinstance(ds1, dict):
        for key in ds1.keys():
            if key not in ds2.keys():
                return False
            if ds1[key] != ds2[key] or type(ds1[key]) != type(ds2[key]):
                return False

    return True


def getFileLines(fname):
    fhandle = open(fname)
    lines = []
    for line in fhandle:
        line = line.rstrip()
        if line:
            lines.append(line)
    fhandle.close()
    return lines


if __name__ == '__main__':
    json_path = input("Please key in path to the json file: ")
    fh = open(json_path)
    data = json.load(fh)
    fh.close()
    data_serialized = serializer(data)
    filename = input("Please key in file name:")
    with open(filename, 'w') as f:
        f.write(data_serialized)
        f.close()

    lines = getFileLines(filename)
    data_deserialized = deserializer(lines)
    same_data = my_compare(data, data_deserialized)

    if same_data:
        print("Successful! Deserialized data {} is the same as original file.".format(data_deserialized))
    else:
        print("Failed! Deserialized data {} is different from original file.".format(data_deserialized))
