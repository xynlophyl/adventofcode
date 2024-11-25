import numpy as np

def main():

    path = './input.txt'
    # path = './sample_input.txt'

    with open(path, 'r') as f:

        lines = f.read().splitlines()
        res1 = wait_for_it(lines)
        res2 = wait_for_it2(lines)

    return res1, res2

def wait_for_it(lines):

    times, distances = parse_records(lines)
    return find_ways_to_win(times, distances)

def wait_for_it2(lines):

    time, distance = parse_records2(lines)
    return find_ways_to_win(time, distance)

def parse_records(lines):

    times = np.array([int(t) for t in lines[0].split(':')[1].split(' ') if t])
    distances = np.array([int(d) for d in lines[1].split(':')[1].split(' ') if d])

    assert times.shape == distances.shape

    return times, distances

def parse_records2(lines):

    time = np.array([int(lines[0].split(':')[1].replace(" ", ""))], dtype = 'int64')
    distance = np.array([int(lines[1].split(':')[1].replace(" ", ""))])

    return time, distance

def find_ways_to_win(times, records):

    print(times.dtype, records.dtype)

    root = np.sqrt(times**2-4*records)

    high, low = (
        ((times+root)/2 - 1e-10),
        ((times-root)/2 + 1e-10)
        ) # small epsilon value to account for integral roots

    return np.prod(np.floor(high) - np.ceil(low)+1).astype('int64')

if __name__ == '__main__':

    print(main())