import os

def read_file(path):

    with open(path, 'r') as f:

        text = f.read()

    return text

def print_answers(path, ans1, ans2 = None):

    space = ' '*(len('1/sample_input.txt') - len(path))

    if ans2 is None:    
        print(f"{path}: {ans1}")
    else:
        print(f"{space}{path}: {ans1} | \t {ans2}")

def get_day(file_path):
    folder_path = os.path.dirname(os.path.abspath(file_path))
    day = os.path.split(folder_path)[-1]

    return day