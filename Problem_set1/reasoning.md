### Objective or problem statement
Write a short python script that will output a 2 dimensional grid cell whose elements are probabilities that total to one.  These values would represent our guesses as to where the symbolic robot would be after we provide it with a set of moves (as well as rates of error for its movements and sensors)

### Input and output requirements

#### Inputs
1. 2 dimensional map of color names
2. A list of 2 element lists representing robot motion [[1,0], [0,0], [0,-1] ...]
3. A float representing motion error rates
4. Another float representing  sensor error rates

#### Output
1. A 2 dimensional map with elements of type float representing the robot's guesses as to which part of the map it currently is in.  All elements when added together should total 1

### Solution reasoning

#### Overview
To start off, we should attempt to break the problem down into smaller pieces.  The first piece is to try to get the robot to output correct values when it is simply staying in place, in a very simple 2D environment. We will also assume that it has perfect sensors. After which, we check later on if we are still getting correct results once we introduce imperfect sensors.

After this, we try to get the robot to output correct values when it is moving. Once again, we assume perfect motion.  Once settled, we then proceed to introduce imperfect motion.

#### The sense function
The sense function basically takes several inputs.  A 2D world_map, the sensed measurement, the rate at which the sensor is correct, and optionally, a pre existing probability map.  If no preexisting probability map is provided, it constructs a probability map with uniform distribution.
It's role is then to guess the probability of which tile it is currently on, given the sensed measurement input.  The current sense function only handles one measurement, but a list of measurements can iterated and fed to it one by one to get cumulative values for multiple measurements.

#### The move function
The move function's responsibility is to shift the provided probability map vertically and horizontally based on given inputs. Shifting to the right should shift the entire map to the right, and moving to upwards should shift the map upwards. Same as moving to the left, and moving downwards.
Doing this in a single dimension has been demonstrated in class.  Adapting this onto the second dimension involves assigning the sum of a successful move and a failed move on to each and every single tile.

#### The localize function
This function brings the move and sense functions together.  For each pair of move and sense function elements, we call the move function first, then the sense function.  Once done with all the inputs, we send the return the resulting two dimensional probability map. 