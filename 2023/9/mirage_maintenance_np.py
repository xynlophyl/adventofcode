import numpy as np

def main():

    # path = './input.txt'
    path = './sample_input.txt'

    with open(path, 'r') as f:

        lines = f.read().splitlines()
        res1 = mirage_maintenance(lines)
        res2 = None

    return res1, res2

def mirage_maintenance(lines):

    vals = np.array([[int(i) for i in l.split(' ')] for l in lines])

    print(vals)

    _, m = vals.shape

    terms = np.array([[i**j for j in range(m)] for i in range(1,m+1)], dtype = 'int64')

    coefs = np.linalg.solve(terms, vals.T).T

    next_terms = np.array([(m+1)**j for j in range(m)])

    return np.sum(np.dot(coefs, next_terms))


if __name__ == '__main__':

    print(main())