import numpy as np
matrice =  np.full((10, 10), ".")

def print_possible_moves(matrix, amazon_position,next_col):
        position=[]
        n = len(matrix)
        x, y = amazon_position
        matrix[x, y]="A"
        matrix[5, 0]="A"
        matrix[0, 1]="A"
        """diagonal movements"""
        for move in range(1,5):

            dia_x, dia_y = x + move, y + move
            # if list(matrix[dia_x]).count("A") >=2:
            #     break
            if(x + move  < n and y + move < n):
                # matrix[dia_x, dia_y]="M"
                if(matrix[dia_x, dia_y]!="A"):
                    position.append((dia_x,dia_y))
                    matrix[dia_x, dia_y]="M"
            if (dia_x - 1>0 and move == 3 and dia_y<10 ):
                # matrix[dia_x-1, dia_y]="M"
                if(matrix[dia_x-1, dia_y]!="A" ):
                    position.append((dia_x-1,dia_y))
                    matrix[dia_x-1, dia_y]="M"
            if (dia_y - 1>0 and move == 3 and dia_x<10 ):
                # matrix[dia_x, dia_y-1]="M"
                if(matrix[dia_x, dia_y-1]!="A" ):
                    position.append((dia_x,dia_y-1))
                    matrix[dia_x, dia_y-1]="M"



        for move in range(1,5):
            dia_x, dia_y = x - move, y - move
            # if list(matrix[dia_x]).count("A") >=2:
            #     break
            if(x - move  >= 0 and y - move >=0):
                # matrix[dia_x, dia_y]="M"
                if(matrix[dia_x, dia_y]!="A" ):
                    position.append((dia_x,dia_y))
                    matrix[dia_x, dia_y]="M"
            if (dia_x + 1<10 and move == 3 and dia_y<10 and dia_y>=0 and dia_x+1>=0 ):
                # matrix[dia_x+1, dia_y]="M"
                if(matrix[dia_x+1, dia_y]!="A"):
                    position.append((dia_x+1,dia_y))
                    matrix[dia_x+1, dia_y]="M"
            if (dia_y + 1<10 and move == 3 and dia_x<10  and dia_y+1>=0 and dia_x>=0  ):
                # matrix[dia_x, dia_y+1]="M"
                if(matrix[dia_x, dia_y+1]!="A" ):
                    position.append((dia_x,dia_y+1))
                    matrix[dia_x, dia_y+1]="M"


        for move in range(1,5):
            dia_x, dia_y = x + move, y - move
            # if list(matrix[dia_x]).count("A") >=2:
            #     break
            if(x + move  >= 0 and y - move >=0 and x + move  < 10 and y - move <10):
                # matrix[dia_x, dia_y]="M"
                if(matrix[dia_x, dia_y]!="A" ):
                    position.append((dia_x,dia_y))
                    matrix[dia_x, dia_y]="M"
            if (dia_x - 1<10 and move == 3 and dia_y<10 and dia_y>=0 and dia_x-1>=0 ):
                # matrix[dia_x-1, dia_y]="M"
                if(matrix[dia_x-1, dia_y]!="A" ):
                    position.append((dia_x-1,dia_y))
                    matrix[dia_x-1, dia_y]="M"
            if (dia_y + 1<10 and move == 3 and dia_x<10  and dia_y+1>=0 and dia_x>=0  ):
                # matrix[dia_x, dia_y+1]="M"
                if(matrix[dia_x, dia_y+1]!="A" ):
                    position.append((dia_x,dia_y+1))
                    matrix[dia_x, dia_y+1]="M"

        for move in range(1,6):
            dia_x, dia_y = x - move, y + move
            # if list(matrix[dia_x]).count("A") >=2:
            #     break
            if(x - move  >= 0 and y + move >=0 and x - move  < 10 and y + move <10):
                # matrix[dia_x, dia_y]="M"
                if(matrix[dia_x, dia_y]!="A" ):
                    position.append((dia_x,dia_y))
                    matrix[dia_x, dia_y]="M"

            if (dia_x + 1<10 and move == 3 and dia_y<10 and dia_y>=0 and dia_x+1>=0 ):
                # matrix[dia_x+1, dia_y]="M"
                if(matrix[dia_x+1, dia_y]!="A" ):
                    position.append((dia_x+1,dia_y))
                    matrix[dia_x+1, dia_y]="M"

            if (dia_y - 1<10 and move == 3 and dia_x<10  and dia_y-1>=0 and dia_x>=0  ):
                # matrix[dia_x, dia_y-1]="M"
                if(matrix[dia_x, dia_y-1]!="A"):
                    position.append((dia_x,dia_y-1))
                    matrix[dia_x, dia_y-1]="M"

        """Vertical movements"""
        for move in range(1,5):
            new_x = x + move
            # if list(matrix[new_x]).count("A") >=2:
            #     break
            if(x + move  >= 0 and x + move  < 10):
                # matrix[new_x, y]="M"
                if(matrix[new_x, y]!="A" ):
                    position.append((new_x,y))
                    matrix[new_x, y]="M"
            if (y + 1<10 and move == 4 and new_x<10 and new_x>=0 and y+1>=0 ):
                # matrix[new_x, y+1]="M"
                if(matrix[new_x, y+1]!="A" ):
                    position.append((new_x,y+1))
                    matrix[new_x, y+1]="M"
            if (y - 1<10 and move == 4 and new_x<10  and new_x>=0 and y-1>=0  ):
                # matrix[new_x, y-1]="M"
                if(matrix[new_x,  y-1]!="A" ):
                    position.append((new_x, y-1))
                    matrix[new_x, y-1]="M"

        for move in range(1,6):
            new_x = x - move
            # if list(matrix[new_x]).count("A") >=2:
            #     break
            if(x - move  >= 0 and x - move  < 10):
                # matrix[new_x, y]="M"
                if(matrix[new_x, y]!="A" ):
                    position.append((new_x,y))
                    matrix[new_x, y]="M"
            if (y + 1<10 and move == 4 and new_x<10  and new_x>=0 and y+1>=0  ):
                # matrix[new_x, y+1]="M"
                if(matrix[new_x, y+1]!="A" ):
                    position.append((new_x,y+1))
                    matrix[new_x, y+1]="M"
            if (y - 1<10 and move == 4 and new_x<10  and new_x>=0 and y-1>=0  ):
                # matrix[new_x, y-1]="M"
                if(matrix[new_x, y-1]!="A" ):
                    position.append((new_x,y-1))
                    matrix[new_x, y-1]="M"


        """horizontal movements"""
        for move in range(1,6):
            # if list(matrix[x]).count("A") >=2:
            #     break
            new_y = y + move
            if(y+ move  >= 0 and y+ move  < 10):
                # matrix[x, new_y]="M"
                if(matrix[x, new_y]!="A" ):
                    position.append((x,new_y))
                    matrix[x, new_y]="M"
            if (x - 1<10 and move == 4 and new_y<10  and new_y>=0 and x-1>=0  ):
                # matrix[x-1, new_y]="M"
                if(matrix[x-1, new_y]!="A" ):
                    position.append((x-1,new_y))
                    matrix[x-1, new_y]="M"
            if (x + 1<10 and move == 4 and new_y<10  and new_y>=0 and x+1>=0  ):
                # matrix[x+1, new_y]="M"
                if(matrix[x, new_y]!="A" ):
                    position.append((x+1,new_y))
                    matrix[x+1, new_y]="M"

        for move in range(1,5):
            new_y = y - move
            # if list(matrix[x]).count("A") >=2:
            #     break
            if(y- move  >= 0 and y- move  < 10):
                # matrix[x, new_y]="M"
                if(matrix[x, new_y]!="A" ):
                    position.append((x,new_y))
                    matrix[x, new_y]="M"
            if (x - 1<10 and move == 4 and new_y<10  and new_y>=0 and x-1>=0  ):
                # matrix[x-1, new_y]="M"
                if(matrix[x-1, new_y]!="A" ):
                    position.append((x-1,new_y))
                    matrix[x-1, new_y]="M"
            if (x + 1<10 and move == 4 and new_y<10  and new_y>=0 and x+1>=0  ):
                # matrix[x+1, new_y]="M"
                if(matrix[x+1, new_y]!="A" ):
                    position.append((x+1,new_y))
                    matrix[x+1, new_y]="M"

        print(matrix)
        return position



# Exemple d'utilisation :
matrix = [[0] * 5 for _ in range(5)]  # Création d'une matrice 5x5
amazon_position = (6, 2)  # Position de l'amazon (indexée à partir de 0)
initial_state = [["#"] * 10 for _ in range(10)]
# print_possible_moves(matrix, amazon_position,4)

print_possible_moves(matrice, (2, 2),3)
# print_possible_moves(matrice, (6, 3) ,4)
# print_possible_moves(tuple(tuple(row) for row in initial_state), (0 , 1),2)

"""

#A#A#A#A#A
##########
##A#A#A#A#
##########
##########
A#########
##########
##########
##########
##########
"""

#//////////////////////////////////////////////////////////////////////:
from search import *
import time

#################
# Problem class #
#################


class NAmazonsProblem(Problem):
    """The problem of placing N amazons on an NxN board with none attacking
    each other. A state is represented as an N-element array, where
    a value of r in the c-th entry means there is an empress at column c,
    row r, and a value of -1 means that the c-th column has not been
    filled in yet. We fill in columns left to right.
    """

    def __init__(self, N):
        super().__init__(tuple([tuple(["#"] * (N)) for _ in range(N)]), N)
        self.shape = N
        self.goal = N
        self.last_amazone_position = []
        self.col = None
        self.col_index = set()
        self.impossible_pos = set()

    def actions(self, state):
        count = 0
        for row in state:
            count += row.count('A')
        col = count
        self.col = col

        possible_actions = self.positions_colonne(col, state)
        if len(possible_actions) == 0:
            return []
        else:
            # possible_actions.reverse()
            return possible_actions


    def result(self, state, row):
        # print("row", row)
        # # p=[]
        # if (row == (0, 0)):
        #     print(2)
        #     print((6,7) in self.impossible_pos)
        #     for i,j in self.impossible_pos:
        #         if(j==7):
        #             p.append(i)
        #     print(sorted(p))
        #     for rox in state : 
        #         print(rox )
            
        updated_grid = [list(row) for row in state]
        x, y = row
        if y == 0 and y not in self.col_index:
            tt=[]
            self.col_index.add(y)
            updated_grid[x][y] = "A"
            _, pos=self.print_possible_moves(updated_grid, (x,y))
            for i in self.impossible_pos:
                if i[1]==1:
                    tt.append(i)
                    
            self.last_amazone_position.insert(0,(x, y))
            return tuple(map(tuple, updated_grid))

        self.print_possible_moves(updated_grid, self.last_amazone_position[0])
        if row not in self.impossible_pos and y not in self.col_index:
                self.col_index.add(y)
                updated_grid[x][y] = "A"
                self.last_amazone_position.insert(0,(x, y))
                return tuple(map(tuple, updated_grid))
        return state

    def goal_test(self, state):
        nbrA = 0
        for row in state:
            nbrA += list(row).count("A")
        return nbrA == self.goal

    def positions_colonne(self, col, state):
        positions = []
        for i, ligne in enumerate(state):
            positions.append((i, col))
        return positions

    def print_possible_moves(self, matrix, amazon_position,update=True):
        position = set()
        x, y = amazon_position
        matrix[x][y] = "A"
        """diagonal movements"""
        for move in range(1, 5):

            dia_x, dia_y = x + move, y + move

            if (x + move >= 0 and y + move >= 0 and x + move < self.shape and y + move < self.shape):
                if (matrix[dia_x][dia_y] != "A"):
                    
                    if(update):
                        self.impossible_pos.add((dia_x, dia_y))
                    position.add((dia_x, dia_y))
                    # x + move >= 0 and y + move >= 0 and x + \
                    #     move < self.shape and y + move < self.shape
            if (dia_x - 1 >= 0 and move == 3 and dia_y < self.shape and dia_x - 1 < self.shape and dia_y >= 0):
                if (matrix[dia_x-1][dia_y] != "A"):
                    if(update):
                        self.impossible_pos.add((dia_x-1, dia_y))
                    position.add((dia_x-1, dia_y))

            if (dia_y - 1 >= 0 and move == 3 and dia_x < self.shape and dia_y - 1 < self.shape and dia_x >= 0):
                if (matrix[dia_x][dia_y-1] != "A"):
                    if(update):
                        self.impossible_pos.add((dia_x, dia_y-1))
                    position.add((dia_x, dia_y-1))

        for move in range(1, 5):
            dia_x, dia_y = x - move, y - move
            if (x - move >= 0 and y - move >= 0 and x - move < self.shape and y - move < self.shape):
                if (matrix[dia_x][dia_y] != "A"):
                    if(update):
                        self.impossible_pos.add((dia_x, dia_y))
                    position.add((dia_x, dia_y))
            if (dia_x + 1 < self.shape and move == 3 and dia_y < self.shape and dia_y >= 0 and dia_x+1 >= 0):
                if (matrix[dia_x+1][dia_y] != "A"):
                    if(update):
                        self.impossible_pos.add((dia_x+1, dia_y))
                    position.add((dia_x+1, dia_y))
            if (dia_y + 1 < self.shape and move == 3 and dia_x < self.shape and dia_y+1 >= 0 and dia_x >= 0):
                if (matrix[dia_x][dia_y+1] != "A"):
                    if(update):
                        self.impossible_pos.add((dia_x, dia_y+1))
                    position.add((dia_x, dia_y+1))

        for move in range(1, 5):
            dia_x, dia_y = x + move, y - move
            if (x + move >= 0 and y - move >= 0 and x + move < self.shape and y - move < self.shape):
                if (matrix[dia_x][dia_y] != "A"):
                    if(update):
                        self.impossible_pos.add((dia_x, dia_y))
                    position.add((dia_x, dia_y))
            if (dia_x - 1 < self.shape and move == 3 and dia_y < self.shape and dia_y >= 0 and dia_x-1 >= 0):
                if (matrix[dia_x-1][dia_y] != "A"):
                    if(update):
                        self.impossible_pos.add((dia_x-1, dia_y))
                    position.add((dia_x-1, dia_y))
            if (dia_y + 1 < self.shape and move == 3 and dia_x < self.shape and dia_y+1 >= 0 and dia_x >= 0):
                if (matrix[dia_x][dia_y+1] != "A"):
                    if(update):
                        self.impossible_pos.add((dia_x, dia_y+1))
                    position.add((dia_x, dia_y+1))

        for move in range(1, 6):
            dia_x, dia_y = x - move, y + move
            if (x - move >= 0 and y + move >= 0 and x - move < self.shape and y + move < self.shape):
                if (matrix[dia_x][dia_y] != "A"):
                    if(update):
                        self.impossible_pos.add((dia_x, dia_y))
                    position.add((dia_x, dia_y))

            if (dia_x + 1 < self.shape and move == 3 and dia_y < self.shape and dia_y >= 0 and dia_x+1 >= 0):
                if (matrix[dia_x+1][dia_y] != "A"):
                    if(update):
                        self.impossible_pos.add((dia_x+1, dia_y))
                    position.add((dia_x+1, dia_y))

            if (dia_y - 1 < self.shape and move == 3 and dia_x < self.shape and dia_y-1 >= 0 and dia_x >= 0):
                if (matrix[dia_x][dia_y-1] != "A"):
                    if(update):
                        self.impossible_pos.add((dia_x, dia_y-1))
                    position.add((dia_x, dia_y-1))

        """Vertical movements"""
        for move in range(1, 5):
            new_x = x + move
            if (x + move >= 0 and x + move < self.shape):
                if (matrix[new_x][y] != "A"):
                    if(update):
                        self.impossible_pos.add((new_x, y))
                    position.add((new_x, y))
            if (y + 1 < self.shape and move == 4 and new_x < self.shape and new_x >= 0 and y+1 >= 0):
                if (matrix[new_x][y+1] != "A"):
                    if(update):
                        self.impossible_pos.add((new_x, y+1))
                    position.add((new_x, y+1))
                        
            if (y - 1 < self.shape and move == 4 and new_x < self.shape and new_x >= 0 and y-1 >= 0):
                if (matrix[new_x][y-1] != "A"):
                    if(update):
                        self.impossible_pos.add((new_x, y-1))
                    position.add((new_x, y-1))

        for move in range(1, 6):
            new_x = x - move
            if (x - move >= 0 and x - move < self.shape):
                if (matrix[new_x][y] != "A"):
                    if(update):
                        self.impossible_pos.add((new_x, y))
                    position.add((new_x, y))
                        
            if (y + 1 < self.shape and move == 4 and new_x < self.shape and new_x >= 0 and y+1 >= 0):
                if (matrix[new_x][y+1] != "A"):
                    if(update):
                        self.impossible_pos.add((new_x, y+1))
                    position.add((new_x, y+1))
            if (y - 1 < self.shape and move == 4 and new_x < self.shape and new_x >= 0 and y-1 >= 0):
                if (matrix[new_x][y-1] != "A"):
                    if(update):
                        self.impossible_pos.add((new_x, y-1))
                    position.add((new_x, y-1))

        """horizontal movements"""
        for move in range(1, 6):
            new_y = y + move
            if (y + move >= 0 and y + move < self.shape):
                if (matrix[x][new_y] != "A"):
                    if(update):
                        self.impossible_pos.add((x, new_y))
                    position.add((x, new_y))
            if (x - 1 < self.shape and move == 4 and new_y < self.shape and new_y >= 0 and x-1 >= 0):
                if (matrix[x-1][new_y] != "A"):
                    if(update):
                        self.impossible_pos.add((x-1, new_y))
                    position.add((x-1, new_y))
            if (x + 1 < self.shape and move == 4 and new_y < self.shape and new_y >= 0 and x+1 >= 0):
                if (matrix[x][new_y] != "A"):
                    if(update):
                        self.impossible_pos.add((x+1, new_y))
                    position.add((x+1, new_y))

        for move in range(1, 5):
            new_y = y - move
            if (y - move >= 0 and y - move < self.shape):
                if (matrix[x][new_y] != "A"):
                    if(update):
                        self.impossible_pos.add((x, new_y))
                    position.add((x, new_y))
            if (x - 1 < self.shape and move == 4 and new_y < self.shape and new_y >= 0 and x-1 >= 0):
                if (matrix[x-1][new_y] != "A"):
                    if(update):
                        self.impossible_pos.add((x-1, new_y))
                    position.add((x-1, new_y))
            if (x + 1 < self.shape and move == 4 and new_y < self.shape and new_y >= 0 and x+1 >= 0):
                if (matrix[x+1][new_y] != "A"):
                    if(update):
                        self.impossible_pos.add((x+1, new_y))
                    position.add((x+1, new_y))
        return len(position), position

    # def h(self, node):
    #     h = 0.0

    #     return h
    def h(self, node):
        state = node.state
        conflicts = 0

        # Filter out invalid positions (e.g., 'A')
        valid_positions = [(i, j) for i, row in enumerate(state) for j, col in enumerate(row) if col.isdigit()]

        # Check for conflicts between queens
        for i in range(len(valid_positions)):
            for j in range(i + 1, len(valid_positions)):
                # Check if queens are in the same column or diagonal
                if valid_positions[i][1] == valid_positions[j][1] or abs(valid_positions[i][1] - valid_positions[j][1]) == abs(i - j):
                    conflicts += 1

        # Heuristic value is the number of conflicts
        return conflicts




#####################
# Launch the search #
#####################
def hill_climbing(problem):
    current = Node(problem.initial)
    while True:
        neighbors = current.expand(problem)
        if not neighbors:
            break
        neighbor = min(neighbors, key=lambda node: problem.h(node))
        if problem.h(neighbor) >= problem.h(current):
            break
        current = neighbor
    return current.state


# problem = NAmazonsProblem(int(sys.argv[1]))
problem = NAmazonsProblem(13)
start_timer = time.perf_counter()
node = astar_search(problem, problem.h, display=False)
end_timer = time.perf_counter()
solution = hill_climbing(problem)
print("solution", solution)


# example of print

path = node.path()

print('Number of moves: ', str(node.depth))

for n in path:

    # assuming that the _str_ function of state outputs the correct format
    # print(n.state)
    state_str = ""
    for row in n.state:
        state_str += ''.join(row) + '\n'
    print(state_str)

# print("Time: ", end_timer - start_timer)