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
visited = set()

class Pacman(Problem):
    # def actions(self, state):
    #     # Define possible actions for a given state
    #     actions = []
    #     nrows, ncols = state.shape

    #     for direction in ["Up", "Down", "Left", "Right"]:
    #         for k in range(1, max(nrows, ncols)):
    #             actions.append((direction, k))
        
    #     return actions
    def actions(self, state):
    # Define possible actions for a given state
        actions = []
        nrows, ncols = state.shape
        pacman_i, pacman_j = self.find_pacman(state.grid)

        for direction in ["Up", "Down", "Left", "Right"]:
            # for k in range(1, max(nrows, ncols)):
            for k in range(1, max(nrows, ncols)):
                if direction == "Up" and pacman_i - k >= 0 and state.grid[pacman_i - k][pacman_j] != '#' and (pacman_i-k, pacman_j) not in visited:
                    visited.add((pacman_i-k, pacman_j))
                    actions.append((direction, k))
                elif direction == "Down" and pacman_i + k < nrows and state.grid[pacman_i + k][pacman_j] != '#' and (pacman_i+k, pacman_j) not in visited:
                    visited.add((pacman_i+k, pacman_j))
                    actions.append((direction, k))
                elif direction == "Left" and pacman_j - k >= 0 and state.grid[pacman_i][pacman_j - k] != '#' and (pacman_i, pacman_j-k) not in visited:
                    visited.add((pacman_i, pacman_j-k))
                    actions.append((direction, k))
                elif direction == "Right" and pacman_j + k < ncols and state.grid[pacman_i][pacman_j + k] != '#' and (pacman_i, pacman_j+k) not in visited:
                    visited.add((pacman_i, pacman_j+k))
                    actions.append((direction, k))
                else:
                    
                    break

        return actions
    def result(self, state, action):
        # Apply the action to the state and return the new state
        nrows, ncols = state.shape
        pacman_i, pacman_j = self.find_pacman(state.grid)
        new_grid = [list(row) for row in state.grid]

        direction, num_moves = action

        if direction == "Up":
            for k in range(1, num_moves + 1):
                if pacman_i - k >= 0:
                    if state.grid[pacman_i - k][pacman_j] != '#':
                        # if state.grid[pacman_i - k][pacman_j] == 'F':
                        #     new_grid[pacman_i - k][pacman_j] = 'P'
                        #     new_grid[pacman_i - k + 1][pacman_j] = '.'
                        #     break
                        new_grid[pacman_i - k][pacman_j] = 'P'
                        new_grid[pacman_i - k + 1][pacman_j] = '.'
                        
                    else:
                        break
        elif direction == "Right":
            for k in range(1, num_moves + 1):
                if pacman_j + k < ncols:
                    if state.grid[pacman_i][pacman_j + k] != '#':
                        
                        # if state.grid[pacman_i][pacman_j + k] == 'F':
                        #     new_grid[pacman_i][pacman_j + k] = 'P'
                        #     new_grid[pacman_i][pacman_j + k - 1] = '.'
                        #     break
                        new_grid[pacman_i][pacman_j + k] = 'P'
                        new_grid[pacman_i][pacman_j + k - 1] = '.'
                    else:
                        break
        elif direction == "Down":
            for k in range(1, num_moves + 1):
                if pacman_i + k < nrows:
                    if state.grid[pacman_i + k][pacman_j] != '#':
                        new_grid[pacman_i + k][pacman_j] = 'P'
                        new_grid[pacman_i + k - 1][pacman_j] = '.'
                        # if state.grid[pacman_i + k][pacman_j] == 'F':
                        #     new_grid[pacman_i + k][pacman_j] = 'P'
                        #     new_grid[pacman_i + k - 1][pacman_j] = '.'
                        #     break
                        # new_grid[pacman_i + k][pacman_j] = 'P'
                        # new_grid[pacman_i + k - 1][pacman_j] = '.'
                    else:
                        break
        elif direction == "Left":
            for k in range(1, num_moves + 1):
                if pacman_j - k >= 0:
                    if state.grid[pacman_i][pacman_j - k] != '#':
                        
                        # if state.grid[pacman_i][pacman_j - k] == 'F':
                        #     new_grid[pacman_i][pacman_j - k] = 'P'
                        #     new_grid[pacman_i][pacman_j - k + 1] = '.'
                        #     break
                        new_grid[pacman_i][pacman_j - k] = 'P'
                        new_grid[pacman_i][pacman_j - k + 1] = '.'
                    else:
                        break
        for i in new_grid:
            print(i)
        print("\n")
        return State(state.shape, new_grid, state.answer, action)

    def goal_test(self, state):
        return all('F' not in row for row in state.grid)

    def find_pacman(self, grid):
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 'P':
                    return i, j


###############
# State class #
###############
class State:

    def __init__(self, shape, grid, answer=None, move=["Init"]):
        self.shape = shape
        self.answer = answer if answer is not None else []
        self.grid = grid
        self.move = move[0]

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
    # filepath = sys.argv[1]
    shape, initial_grid, initial_fruit_count = read_instance_file(
            'Instances/i03')
    # shape, initial_grid, initial_fruit_count = read_instance_file(filepath)
    init_state = State(shape, tuple(initial_grid), initial_fruit_count, ["Init"])
    problem = Pacman(init_state)

    # Example of search
    start_timer = time.perf_counter()
    node, nb_explored, remaining_nodes =  depth_first_tree_search(problem)
    # breadth_first_graph_search
    # breadth_first_tree_search
    #depth_first_tree_search
    #depth_first_graph_search
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
