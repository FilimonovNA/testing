def division(x, y):
    return x/y


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
