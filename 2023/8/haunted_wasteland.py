def main():

    path = './input.txt'
    # path = './sample_input.txt'

    with open(path, 'r') as f:

        lines = f.read().splitlines()
        # res1 = haunted_wasteland(lines)
        res1 = None
        res2 = haunted_wasteland2(lines)

    return res1, res2

def haunted_wasteland(lines):

    steps = lines[0]

    graph = make_graph(lines[2:])

    count = 0

    node = 'AAA'

    while count < 1000000:
        
        if node == 'ZZZ':

            return count

        curr = steps[count%len(steps)]

        if curr == 'L':
            node = graph[node][0]
        
        else:
            node = graph[node][1]

        count += 1

    return -1  

def make_graph(lines):

    graph  = {}

    for l in lines:

        node, neighbors = l.split(' = ')

        nei1, nei2 = neighbors.split(', ')
        nei1, nei2 = nei1[1:], nei2[:-1]

        graph[node] = [nei1, nei2]
    
    return graph

def haunted_wasteland2(lines):

    steps = [0 if i == 'L' else 1 for i in lines[0]]

    graph = make_graph(lines[2:])

    nodes = [k for k in graph.keys() if k[-1] == 'A']
    
    lengths_to_z = [find_length(graph, steps, node) for node in nodes]

    import math

    return math.lcm(*lengths_to_z)

def find_length(graph, steps, node):

    count = 0

    curr = node

    while True:

        if curr[-1] == 'Z': return count
        
        curr = graph[curr][steps[count%len(steps)]]
    
        count += 1


if __name__ == '__main__':

    print(main())