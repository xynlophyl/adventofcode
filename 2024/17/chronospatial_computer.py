import functools
path = '17/sample_input.txt'
path = '17/input.txt'

with open(path, 'r') as f:
    text = f.read()

lines = text.splitlines()

n = len("Register A: ")
A, B, C = [int(line[n:]) for line in lines[:3]]

program = lines[-1]
program = [int(v) for v in program[len("Program: "):].split(',')]

"""INSTRUCTIONS
op_code = name: instructions                           -> save
0       =  adv: val(A) / (2**combo_op)                 -> A
1       =  bxl: bitwise_XOR( val(B), literal_op )      -> B
2       =  bst: combo_op%8                             -> B
3       =  jnz: if val(A) = 0, then _, else literal_op -> ptr (don't +2 after)
4       =  bxc: bitwise_XOR( val(B), val(C) )          -> B
5       =  out: combo_op%8                             -> output
6       =  bdv: val(A) / (2**combo_op)                 -> B
7       =  cdv: val(A) / (2**combo_op)                 -> C
"""


### PART 1 ###
def get_output(A, B, C, program):

    def get_combo_operand(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        else:
            print('invalid program: operand 7')
            return -1

    # print('SET UP')
    # print(A, B, C)
    # print(program)
    # print()

    output = []
    ptr = 0
    iters = []
    while ptr < len(program) - 1:
        assert ptr >= -1

        operand = None

        op_code = program[ptr]
        operand = program[ptr+1]

        # print(ptr, op_code, operand, get_combo_operand(operand))
        if ptr == 0:
            # print(A, B, C)
            iters.append((A,B,C))
            # input()
        if op_code == 0:
            A = A // (2**get_combo_operand(operand))
            # print('A:', A)
        elif op_code == 1:
            B = B ^ operand
            # print('B:', B)
        elif op_code == 2:
            B = get_combo_operand(operand)%8
            # print('B:', B)
        elif op_code == 3:
            if A != 0 and operand != ptr:
                ptr = operand
                ptr -= 2
        elif op_code == 4:
            B = B ^ C
            # print('B:', B)
        elif op_code == 5:
            output.append(get_combo_operand(operand)%8)
            # print(B%8)
        elif op_code == 6:
            B = A // (2**get_combo_operand(operand))
            # print('B:', B)
        else:
            C = A // (2**get_combo_operand(operand))
            # print('C:', C)
        ptr += 2
    
    iters.append((A,B,C))
    
    # for i, j in zip(iters, output):
    #     print(i)
    #     print(j)
    #     print()

    return output

print()
output = get_output(1000, B, C, program)
res = ','.join([str(val) for val in output])
print('res', res)


"""PART 2"""
val = program[-1]
As = []
# get the first 3 bits of A
for a in range(7): # for the index of program, A has to have 3 bits, in order to safely exit loop
    output = get_output(a, 0, 0, program)
    if output[0] == program[-1]:
        As.append(a)

print(As)
for val in program[::-1][1:]:
    nxt_As = []
    # print(As)
    for A in As:
        for c in range(7): # considering the last 3 bits of C => C is A[:-B]
            b = val^c 
            b = b ^ 6
            a = b ^ 5

            nxt_As.append(A+a)
    As = nxt_As

    print(len(As))
print(As)
    