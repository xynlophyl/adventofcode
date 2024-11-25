def parabolic_reflector_dish(lines):
	
    stones = [[0 for s in line] for line in lines]
    max_height = len(lines)
    top = [max_height for l in lines[0]]

    for r, row  in enumerate(lines):
		
        for c, val in enumerate(row):
			
            if val == 'O':

                stones[r][c] = top[c]
                top[c] -= 1

            else:

                if val == '#':

                    top[c] = max_height - r - 1
    
    # display_grid(stones)
    return calculate_load(stones)

def display_grid(lines):
      
    for l in lines:
        print(l)

def calculate_load(stones):
      
    return sum(sum(s) for s in stones)


func1 = parabolic_reflector_dish
func2 = None

def main():

	path = './input.txt'
	# path = './sample_input.txt'
	# path = './sample_input2.txt'

	with open(path, 'r') as f:

		lines = f.read().splitlines()
		res1 = func1(lines)
		# res2 = func2(lines)
		res2 = None

	return res1, res2

if __name__ == '__main__':

		print(main())