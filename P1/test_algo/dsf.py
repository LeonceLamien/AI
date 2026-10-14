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
ste = set()

class Pacman(Problem):

    def actions(self, state):
        Xs = state.shape[0]
        Ys = state.shape[1]
        actions = []
        x, y = self.find_pacman(state.grid)
        if x > 0 and state.grid[x-1][y] != '#' and (x-1, y) not in visited:
            # if state.grid[x-1][y] == 'F' :
            visited.add((x-1, y))
            actions.append('LEFT')
            ste.add('RIGHT')
            
        elif x < Xs-1 and state.grid[x+1][y] != '#' and (x+1, y) not in visited:
            # if state.grid[x+1][y] == 'F':
            visited.add((x+1, y))
            actions.append('RIGHT')
            ste.add('LEFT')
        elif y > 0 and state.grid[x][y-1] != '#' and (x, y-1) not in visited:
            # if state.grid[x][y-1] == 'F':
            visited.add((x, y-1))
            actions.append('UP')
            ste.add('DOWN')
        elif y < Ys-1 and state.grid[x][y+1] != '#'and (x, y+1) not in visited:
            # if state.grid[x][y+1] == 'F':
            visited.add((x, y+1))
            actions.append('DOWN')
            ste.add('UP')
        else:
            actions.append(ste.pop())
        # print(actions)
        return actions

    def result(self, state, action):
        x, y = self.find_pacman(state.grid)
        new_grid = [list(row) for row in state.grid]
        new_fruit_count = state.answer
        if action == 'LEFT':
            new_grid[x][y]='.'
            if new_grid[x-1][y] == 'F':
                new_fruit_count -= 1
            new_grid[x-1][y]='P'
        if action == 'RIGHT':
            new_grid[x][y]='.'
            if new_grid[x+1][y] == 'F':
                new_fruit_count -= 1
            new_grid[x+1][y]='P'
        if action == 'UP':
            new_grid[x][y]='.'
            if new_grid[x][y-1] == 'F':
                new_fruit_count -= 1
            new_grid[x][y-1]='P'
        if action == 'DOWN':
            new_grid[x][y]='.'
            if new_grid[x][y+1] == 'F':
                new_fruit_count -= 1
            new_grid[x][y+1]='P'
        # for i in new_grid:
        #     print(i)
        # print("\n")

        return State(state.shape, new_grid, new_fruit_count, action)

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
            'Instances/i10')
    # shape, initial_grid, initial_fruit_count = read_instance_file(filepath)
    init_state = State(shape, tuple(initial_grid), initial_fruit_count, ["Init"])
    problem = Pacman(init_state)

    # Example of search
    start_timer = time.perf_counter()
    node, nb_explored, remaining_nodes =  depth_first_graph_search(problem)
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
