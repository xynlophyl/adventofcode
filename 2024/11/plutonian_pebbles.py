import functools
path = '11/sample_input.txt'
path = '11/input.txt'

with open(path, 'r') as f:
    text = f.read()

def count_stones_after_blinking(engravings, n):
    @functools.cache
    def split_stone(x, n):
        if n == 0:
            return 1
        if x == '0':
            return split_stone('1', n-1)
        elif len(x)%2 == 0:
            left, right = x[:len(x)//2], x[len(x)//2:]
            left = '0' if left == '' else str(int(left))
            right = '0' if right == '' else str(int(right))
            return split_stone(left, n-1) + split_stone(right, n-1)
        else:
            return split_stone(str(int(x)*2024), n-1)
    
    return sum([split_stone(x, n) for x in engravings])

"""PART 1"""
engravings = [x for x in text.split()]
# res = count_stones_after_blinking(engravings, 6)
res = count_stones_after_blinking(engravings, 25)
print(res)

"""PART 2"""    

engravings = [x for x in text.split()]
res = count_stones_after_blinking(engravings, 75)
print(res)