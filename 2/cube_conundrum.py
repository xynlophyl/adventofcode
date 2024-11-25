def main():

    path = './input.txt'

    with open(path, 'r') as f:

        lines = f.read().splitlines()
    
    part1 = 0
    part2 = 0

    for l in lines:

        part1 += check_cube_combination(l, red = 12, green = 13, blue = 14)
        part2 += combination_power(l)

    return part1, part2

def check_cube_combination(line, red, green, blue):

    # line = Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

    game, sets = line.split(':') # Game 1 AND 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    _, game_no = game.split(' ') # Game AND 1

    color_counts = {
            'red': red,
            'green': green,
            'blue': blue
        }

    combination = sets.split(';')

    for comb in combination: # 3 blue, 4 red AND 1 red, 2 green, 6 blue AND 2 green

        for c in comb.split(','): # 3 blue AND 4 red
            
            count, color = c[1:].split(' ') # 3 AND blue

            if int(count) > color_counts.get(color, 0): return 0

    return int(game_no)

def combination_power(line):

    game, sets = line.split(':') # Game 1 AND 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    _, game_no = game.split(' ') # Game AND 1

    combination = sets.split(';')

    color_mins = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

    for comb in combination: # 3 blue, 4 red AND 1 red, 2 green, 6 blue AND 2 green

        for c in comb.split(','): # 3 blue AND 4 red
            
            count, color = c[1:].split(' ') # 3 AND blue

            color_mins[color] = max(color_mins[color], int(count))

    power = 1
    for _, v in color_mins.items():

        power *= v

    return power

            
if __name__ == '__main__':

    print(main())