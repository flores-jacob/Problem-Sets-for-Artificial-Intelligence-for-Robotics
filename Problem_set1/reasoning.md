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

To start off, we should attempt to break the problem down into smaller pieces.  The first piece is to try to get the robot to output correct values when it is simply stying in place, in a very simple 2D environment. Furthermore, we will first assume that it has perfect motion and perfect sensors. Once it can detect itself, we can then try to check if the answers we get are still correct if we make it move. Lastly, we mix in sensor and motion error rates one at a time. We should be finished with the exercise once we have succeeded in performing that.