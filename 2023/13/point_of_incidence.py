def point_of_incidence(lines):
	
	springs = find_springs(lines)

	res = 0

	for low, high in springs:

		rows = count_reflections(lines[low:high], 0)
		cols = count_reflections(lines[low:high], 1)

		# print('rows', rows, 'cols', cols)

		res += rows*100 + cols

	return res

def point_of_incidence2(lines):

	springs = find_springs(lines)

	res = 0

	for low, high in springs:

		rows = count_reflections(lines[low:high], 0, 1)
		cols = count_reflections(lines[low:high], 1, 1)

		res += rows*100 + cols

	return res

def find_springs(lines):
	
	low = 0
	high = 0

	springs = []

	while high < len(lines):
			
		if not lines[high]:

			springs.append((low, high))

			low = high + 1

		high += 1

	springs.append((low, high))
	
	return springs

def count_reflections(lines, kind, err = 0):

	m = len(lines) if kind == 0 else len(lines[0])
	n = len(lines[0]) if kind == 0 else len(lines)

	curr = 0
	count = 0

	while curr < m-1:

		diff = check_equal(lines, curr, curr+1, kind)

		if diff <= err:

			low = curr - 1
			high = curr + 2

			reflect_flag = True

			while low >= 0 and high < m:

				diff += check_equal(lines, low, high, kind)

				if diff > err:

					reflect_flag = False
					break

				low -= 1
				high += 1

			if reflect_flag and err - diff == 0:

				count += curr + 1

		curr += 1

	return count

def check_equal(lines, curr, nei, kind):

	count = 0

	if kind == 0:

		for i in range(len(lines[curr])):

			if lines[curr][i] != lines[nei][i]:

				count += 1

	else:

		for i in range(len(lines)):

			if lines[i][curr] != lines[i][nei]:

				count += 1

	# print(n, kind, count)
	return count

def main():

	path = './input.txt'
	# path = './sample_input.txt'
	# path = './sample_input2.txt'

	with open(path, 'r') as f:

		lines = f.read().splitlines()
		res1 = point_of_incidence(lines)
		res2 = point_of_incidence2(lines)
		# res2 = None

	return res1, res2

if __name__ == '__main__':

		print(main())