# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up


def sense(world_map, measurement, sensor_right, p_map_input=None):
    if not p_map_input:
        # num_elements_world_map = len(world_map) * len(world_map[0])
        # single_row = [1.0/num_elements_world_map for elem in range(len(world_map[0]))]
        # probability_map = [single_row for row in range(len(world_map))]
        probability_map = []
        for i in range(len(world_map)):
            row = []
            for k in range(len(world_map[i])):
                row.append(1.0/(len(world_map) * len(world_map[0])))
            probability_map.append(row)
    else:
        probability_map = p_map_input

    for row_index in range(len(world_map)):
        current_row = world_map[row_index]
        for tile_index in range(len(current_row)):
            current_world_tile = current_row[tile_index]
            hit = current_world_tile == measurement
            current_pmap_tile = probability_map[row_index][tile_index]
            prob_answer = current_pmap_tile * ((hit * sensor_right) + ((1 - hit) * (1 - sensor_right)))
            probability_map[row_index][tile_index] = prob_answer

    sum_probabilities = sum([sum(row) for row in probability_map])

    for row_index in range(len(probability_map)):
        for tile_index in range(len(probability_map[row_index])):
            probability_map[row_index][tile_index] /= sum_probabilities

    return probability_map


def localize(colors, measurements, motions, sensor_right, p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]

    # >>> Insert your code here <<<

    return p


def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x), r)) + ']' for r in p]
    print('[' + ',\n '.join(rows) + ']')


#############################################################
# For the following test case, your output should be
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

colors = [['R', 'G', 'G', 'R', 'R'],
          ['R', 'R', 'G', 'R', 'R'],
          ['R', 'R', 'G', 'G', 'R'],
          ['R', 'R', 'R', 'R', 'R']]
measurements = ['G', 'G', 'G', 'G', 'G']
motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]
p_map = localize(colors, measurements, motions, sensor_right=0.7, p_move=0.8)
show(p_map)  # displays your answer
