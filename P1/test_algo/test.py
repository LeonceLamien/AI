"""
Name of the author(s):
- Charles Lohest <charles.lohest@uclouvain.be>
"""
import time
import sys
from search import *


#################
# Problem class #
#################
dico = {}
class Pacman(Problem):


    def trouver_position_P(self,t):
        for i, sous_tuple in enumerate(t):
            for j, element in enumerate(sous_tuple):
                if element == 'P':
                    return (i, j)

        return None

    def actions(self, state):
        # Define the possible actions for a given state
        print(state.move)
        actions = []
        nrows, ncols = state.shape
        # x, y = state.grid.index('P') // ncols, state.grid.index('P') % ncols
        x, y = self.trouver_position_P(state.grid)
        # print(x,y)

        # Check if Pacman can move left
        if y > 0 and state.grid[x][y - 1] != '#':
            if state.grid[x][y-1]=='F':
                actions.append('EAT')
                print("--------------------------------------",x,y)
            actions.append('LEFT')

        # Check if Pacman can move right
        if y < ncols - 1 and state.grid[x][y + 1] != '#':
            if state.grid[x][y+1]=='F':
                actions.append('EAT')
            actions.append('RIGHT')

        # Check if Pacman can move up
        if x > 0 and state.grid[x - 1][y] != '#':
            if state.grid[x-1][y]=='F':
                actions.append('EAT')
            actions.append('UP')

        # Check if Pacman can move down
        if x < nrows - 1 and state.grid[x + 1][y] != '#':
            if state.grid[x+1][y]=='F':
                actions.append('EAT')
            actions.append('DOWN')
        
        

        return actions

    def result(self, state, action):
        # Apply the action to the state and return the new state
        nrows, ncols = state.shape
        x, y = self.trouver_position_P(state.grid)
        new_x, new_y = x, y  # Initialize new_x and new_y to current position

        if action == 'LEFT':
            new_y = y - 1
        elif action == 'RIGHT':
            new_y = y + 1
        elif action == 'UP':
            new_x = x - 1
        elif action == 'DOWN':
            new_x = x + 1
        elif action == 'EAT':
            # Decrease the fruit count by 1
            state.answer -= 1

        new_grid = list(state.grid)
        new_row = list(new_grid[x])
        new_row[y] = '.'  # Remove Pacman from the current position
        new_grid[x] = tuple(new_row)

        if action != 'EAT':
            new_row = list(new_grid[new_x])
            new_row[new_y] = 'P'  # Place Pacman in the new position
            new_grid[new_x] = tuple(new_row)

        return State(state.shape, tuple(new_grid), state.answer, action)

    # def result(self, state, action):
    #     # Apply the action to the state and return the new state
    #     nrows, ncols = state.shape
    #     # x, y = state.grid.index('P') // ncols, state.grid.index('P') % ncols
    #     x, y = self.trouver_position_P(state.grid)
    #     if action == 'LEFT':
    #         new_y = y - 1
    #         new_x = x
    #         # state.move(new_x,new_y)
    #     elif action == 'RIGHT':
    #         new_y = y + 1
    #         new_x = x
    #         # state.move(new_x,new_y)
    #     elif action == 'UP':
    #         new_y = y
    #         new_x = x - 1
    #         # state.move(new_x,new_y)
    #     elif action == 'DOWN':
    #         new_y = y
    #         new_x = x + 1
    #         # state.move(new_x,new_y)
    #     elif action == 'EAT':
    #         state.answer -= 1

    #     new_grid = list(state.grid)
    #     # new_grid[x] = new_grid[x][:y] + '.' + new_grid[x][y + 1:]
    #     new_row = list(new_grid[x])
    #     # Modify the row by replacing the character at index y with '.'
    #     new_row[y] = '.'
    #     # Convert the modified row back to a tuple and assign it to the grid
    #     new_grid[x] = tuple(new_row)
    #     # new_grid[new_x] = new_grid[new_x][:new_y] + 'P' + new_grid[new_x][new_y + 1:]
    #     new_row = list(new_grid[new_x])
    #     # Modify the row by replacing the character at index new_y with 'P'
    #     new_row[new_y] = 'P'
    #     # Convert the modified row back to a tuple and assign it to the grid
    #     new_grid[new_x] = tuple(new_row)
    #     # if action != 'EAT':
    #     #     new_row = list(new_grid[new_x])
    #     #     new_row[new_y] = 'P'  # Place Pacman in the new position
    #     #     new_grid[new_x] = tuple(new_row)
    #     return State(state.shape, tuple(new_grid), state.answer, action)
        
    def goal_test(self, state):
    	#check for goal state
    	return state.answer == 0 and state.move != "Init"



###############
# State class #
###############
class State:

    def __init__(self, shape, grid, answer=None, move="Init"):
        self.shape = shape
        self.answer = answer
        self.grid = grid
        self.move = move

    def __str__(self):
        s = self.move + "\n"
        for line in self.grid:
            s += "".join(line) + "\n"
        return s


def read_instance_file(filepath):
    with open(filepath) as fd:
        lines = fd.read().splitlines()
    shape_x, shape_y = tuple(map(int, lines[0].split()))
    initial_grid = [tuple(row) for row in lines[1:1 + shape_x]]
    initial_fruit_count = sum(row.count('F') for row in initial_grid)

    return (shape_x, shape_y), initial_grid, initial_fruit_count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: ./Pacman.py <path_to_instance_file>")
    filepath = sys.argv[1]

    shape, initial_grid, initial_fruit_count = read_instance_file(filepath)
    init_state = State(shape, tuple(initial_grid), initial_fruit_count, "Init")
    problem = Pacman(init_state)

    # Example of search
    start_timer = time.perf_counter()
    node, nb_explored, remaining_nodes = breadth_first_tree_search(problem)
    end_timer = time.perf_counter()

    # Example of print
    path = node.path()

    for n in path:
        # assuming that the __str__ function of state outputs the correct format
        print(n.state)

    print("* Execution time:\t", str(end_timer - start_timer))
    print("* Path cost to goal:\t", node.depth, "moves")
    print("* #Nodes explored:\t", nb_explored)
    print("* Queue size at goal:\t",  remaining_nodes)

