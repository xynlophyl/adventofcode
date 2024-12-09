path = '9/sample_input.txt'
path = '9/input.txt'

with open(path, 'r') as f:
    text = f.read()

text = text.strip('\n')

def generate_disk(text):

    disk = []
    free_space = '.'

    for idx, val in enumerate(text):
        curr = str(idx//2) if idx%2==0 else free_space
        disk += [curr]*int(val)

    return disk

"""PART 1"""
disk = generate_disk(text)
# print(''.join(disk))
    
low, high = 0, len(disk)-1

while low < high:
    if disk[low] != '.': # not a free space
        low += 1
    elif disk[high] == '.': # not a block
        high -= 1
    else:
        disk[low], disk[high] = disk[high], disk[low]
        low += 1
        high -= 1

res = sum([idx*int(val)for idx, val in enumerate(disk) if val != '.' ])
print(res)

"""PART 2"""
disk = generate_disk(text)
high = len(disk) - 1

def find_free_spaces(start):
    last_block = disk[start]    
    while start < len(disk) and disk[start] != '.':
        start += 1
        last_block = disk[low]

    end = start
    while end < len(disk) and disk[end] == '.':
        end += 1

    return start, end, last_block

visited = set('.')
while high >= 0:
    if disk[high] in visited: # find block to move
        high -= 1
    else:
        low = 0
        curr = disk[high] # get block id
        high_start = disk.index(curr) # find the first instance of block
        
        while low < len(disk):
            n = high - high_start + 1 # get range of block
            start, end, last_block = find_free_spaces(low) # get range of free spaces
            # print(end, start, end-start)

            if start > high_start:
                break
            elif end - start >= n: # fits
                disk[start:start+n], disk[high_start:high+1] = disk[high_start:high+1], disk[start:start+n]
                # print(''.join(disk))
                # input()
                break
            else:
                low = end

        # print('block', disk[high], n)
        high = high_start - 1
        visited.add(curr)
        

# print(''.join(disk))
res = sum([idx*int(val)for idx, val in enumerate(disk) if val != '.' ])
print(res)