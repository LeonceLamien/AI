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

    # def trouver_position_P(self, state):
    #     nrows, ncols = state.shape
    #     for i in range(nrows):
    #         for j in range(ncols):
    #             if state.grid[i][j] == 'P':
    #                 return (i, j)

    #     return None

    # def actions(self, state):
    #     actions = []
    #     x, y = self.trouver_position_P(state)
    #     nrows, ncols = state.shape
    #     actions = []

    #     if y > 0 and state.grid[x][y - 1] != '#':
    #         actions.append('LEFT')

    #     if y < ncols - 1 and state.grid[x][y + 1] != '#':
    #         actions.append('RIGHT')

    #     if x > 0 and state.grid[x - 1][y] != '#':
    #         actions.append('UP')

    #     if x < nrows - 1 and state.grid[x + 1][y] != '#':
    #         actions.append('DOWN')
    #     return actions

    # def result(self, state, action):
    #     x, y = self.trouver_position_P(state)
    #     new_grid = [list(row) for row in state.grid]
    #     if action == 'UP':
    #         if x > 0 and new_grid[x - 1][y] != '#':
    #             if new_grid[x - 1][y] == 'F':
    #                 state.answer -= 1
    #             new_grid[x][y] = '.'
    #             new_grid[x - 1][y] = 'P'
    #     elif action == 'DOWN':
    #         if x < state.shape[0] - 1 and new_grid[x + 1][y] != '#':
    #             if new_grid[x + 1][y] == 'F':
    #                 state.answer -= 1
    #             new_grid[x][y] = '.'
    #             new_grid[x + 1][y] = 'P'
    #     elif action == 'LEFT':
    #         if y > 0 and new_grid[x][y - 1] != '#':
    #             if new_grid[x][y - 1] == 'F':
    #                 state.answer -= 1
    #             new_grid[x][y] = '.'
    #             new_grid[x][y - 1] = 'P'
    #     elif action == 'RIGHT':
    #         if y < state.shape[1] - 1 and new_grid[x][y + 1] != '#':
    #             if new_grid[x][y + 1] == 'F':
    #                 state.answer -= 1
    #             new_grid[x][y] = '.'
    #             new_grid[x][y + 1] = 'P'

    #     # for i in new_grid:
    #     #     print(i)
    #     # print('\n')
    #     new_grid = tuple(tuple(row) for row in new_grid)
    #     return State(state.shape, new_grid, state.answer, action)

    # def goal_test(self, state):
    #     return state.answer == 0
    def actions(self, state):
        # Define the possible actions for a given state
        pacman_pos = None
        actions = []
        for i in range(state.shape[0]):
            for j in range(state.shape[1]):
                if state.grid[i][j] == 'P':
                    pacman_pos = (i, j)
                    break
            if pacman_pos:
                break

        # Check possible moves
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            new_pos = (pacman_pos[0] + move[0], pacman_pos[1] + move[1])
            if 0 <= new_pos[0] < state.shape[0] and 0 <= new_pos[1] < state.shape[1]:
                if state.grid[new_pos[0]][new_pos[1]] != '#':
                    actions.append(move)
        return actions

    def result(self, state, action):
        # Apply the action to the state and return the new state
        pacman_pos = None
        for i in range(state.shape[0]):
            for j in range(state.shape[1]):
                if state.grid[i][j] == 'P':
                    pacman_pos = (i, j)
                    break
            if pacman_pos:
                break
        
        new_pos = (pacman_pos[0] + action[0], pacman_pos[1] + action[1])
        if state.grid[new_pos[0]][new_pos[1]] == 'F':
            # If Pacman moves to a cell with fruit, eat the fruit
            row = list(state.grid[new_pos[0]])
            row[new_pos[1]] = '.'
            state.grid = tuple(state.grid[:new_pos[0]] + (tuple(row),) + state.grid[new_pos[0] + 1:])
            state.answer -= 1  # Decrement fruit count
        # Move Pacman to the new position
        row = list(state.grid[pacman_pos[0]])
        row[pacman_pos[1]] = '.'
        state.grid = tuple(state.grid[:pacman_pos[0]] + (tuple(row),) + state.grid[pacman_pos[0] + 1:])
        row = list(state.grid[new_pos[0]])
        row[new_pos[1]] = 'P'
        state.grid = tuple(state.grid[:new_pos[0]] + (tuple(row),) + state.grid[new_pos[0] + 1:])
        state.move = f"Pacman moved to {new_pos}"
        return state



    def goal_test(self, state):
        # Check for goal state
        return state.answer == 0  # All fruits have been eaten
###############
# State class #
###############


class State:

    def __init__(self,shape, grid, answer=None, move="Init"):
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
    # if len(sys.argv) != 2:
    #     print(f"Usage: ./Pacman.py <path_to_instance_file>")
    # filepath = sys.argv['Instances/i03']

    shape, initial_grid, initial_fruit_count = read_instance_file(
        'Instances/i03')
    init_state = State(shape, tuple(initial_grid), initial_fruit_count, "Init")
    problem = Pacman(init_state)

    # Example of search
    start_timer = time.perf_counter()
    node, nb_explored, remaining_nodes = breadth_first_graph_search(problem)
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
