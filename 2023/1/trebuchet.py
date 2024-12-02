def main():

    path = './assets/1_trebuchet_input.txt'
    # path = './assets/2_sample_input.txt'

    with open(path, 'r') as f:

        lines = f.read().splitlines()
    
    res = 0

    for l in lines:

        # print(l, get_numerical_val(l))

        res += get_numerical_val(l)

    return res


def get_numerical_val(line):

    numbers = []

    number_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    low = 0
    high = 0

    while high < len(line):

        if line[high].isnumeric():

            while low < high:

                for i in range(3, 7):

                    if line[low:low+i] in number_map:
                        # print(line[low:low+i])

                        numbers.append(number_map[line[low:low+i]])

                low += 1
            
            numbers.append(int(line[high]))

            low = high + 1
        high += 1

    # print('suff', line[low:])

    while low < high:

        for i in range(3, 7):

            if line[low:low+i] in number_map:
                # print(line[low:low+i])

                numbers.append(number_map[line[low:low+i]])

        low += 1

    if numbers:
        # print(int(f'{numbers[0]}{numbers[-1]}'))
        return int(f'{numbers[0]}{numbers[-1]}')
    return 0
        


if __name__ == '__main__':
    res = main()
    print(res)