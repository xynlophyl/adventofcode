def main():

    path = './input.txt'
    path = './sample_input.txt'

    with open(path, 'r') as f:

        lines = f.read().splitlines()
        res1 = wait_for_it(lines)
        res2 = wait_for_it2(lines)

    return res1, res2

def wait_for_it(lines):

    times, distances, n = parse_records(lines)
    res = 1

    for i in range(n):

        n_ways = find_ways_to_win(times[i], distances[i])
        res *= n_ways

    return res

def wait_for_it2(lines):

    time, distance = parse_records2(lines)

    return find_ways_to_win(time, distance)

def parse_records(lines):

    times = [int(t) for t in lines[0].split(':')[1].split(' ') if t]
    distances = [int(d) for d in lines[1].split(':')[1].split(' ') if d]

    assert len(times) == len(distances)

    return times, distances, len(times)

def parse_records2(lines):

    time = int(lines[0].split(':')[1].replace(" ", ""))
    distance = int(lines[1].split(':')[1].replace(" ", ""))

    return time, distance

def find_ways_to_win(time, record):

    t = time // 2
    count = 0

    while t >= 0:
        # t: time holding down => speed of boat

        r = time - t # r: remaining time for boat to travel
        dist = r * t

        if dist > record:
            count += 2
        t -= 1
    
    if time%2:
        return count
    return count-1


if __name__ == '__main__':

    print(main())