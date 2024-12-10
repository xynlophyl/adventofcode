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
    while start < len(disk) and disk[start] != '.':
        start += 1

    end = start
    while end < len(disk) and disk[end] == '.':
        end += 1

    return start, end

visited = set('.')
low = 0
while high >= 0:
    if disk[high] in visited: # find block to move
        high -= 1
    else:
        start, end = find_free_spaces(low) # get range of free spaces
        low = start # since this is the current first instance of ".", set the start point here for next block's search here 

        curr = disk[high] # get block id
        high_start = disk.index(curr) # find the first instance of block
        n = high - high_start + 1 # get range of block
        
        while start < len(disk):
            if start > high_start:
                break
            elif end - start >= n: # fits
                disk[start:start+n], disk[high_start:high+1] = disk[high_start:high+1], disk[start:start+n]
                break
            else:
                start, end = find_free_spaces(end)

        high = high_start - 1
        visited.add(curr)
        

# print(''.join(disk))
res = sum([idx*int(val)for idx, val in enumerate(disk) if val != '.' ])
print(res)