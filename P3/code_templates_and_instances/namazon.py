from search import *
import time
class NAmazonsProblem(Problem):
    def __init__(self, N):
        super().__init__(tuple([-1] * N))
        self.N = N

    def actions(self, state):
        """In the leftmost empty column, try all non-conflicting rows."""
        if state[-1] != -1:
            return []  # All columns filled; no successors
        else:
            col = state.index(-1)
            return [row for row in range(self.N)
                    if not self.conflicted(state, row, col)]

    def result(self, state, row):
        """Place the next queen at the given row."""
        col = state.index(-1)
        new = list(state[:])
        new[col] = row
        return tuple(new)

    def conflicted(self, state, row, col):
        """Would placing a queen at (row, col) conflict with anything?"""
        return any(self.conflict(row, col, state[c], c)
                   for c in range(col))

    def conflict(self, row1, col1, row2, col2):
        """Would putting two queens in (row1, col1) and (row2, col2) conflict?"""
        # return (row1 == row2 or  # same row
        #         col1 == col2 or  # same column
        #         row1 - col1 == row2 - col2 or  # same \ diagonal
        #         row1 + col1 == row2 + col2)  # same / diagonal
        return row1 == row2 or col1 == col2 or \
           abs(row1 - row2) == abs(col1 - col2) or \
           (abs(row1 - row2) == 2 and abs(col1 - col2) == 3) or \
            (abs(row1 - row2) == 3 and abs(col1 - col2) == 2) or \
           (abs(row1 - row2) == 1 and abs(col1 - col2) == 4) or \
           (abs(row1 - row2) == 4 and abs(col1 - col2) == 1) 
        #    (abs(row1 - row2) == 3 and abs(col1 - col2) == 2) or \
        #    (abs(row1 - row2) == 2 and abs(col1 - col2) == 3) or \
        #    (abs(row1 - row2) == 4 and abs(col1 - col2) == 1) or \
        #    (abs(row1 - row2) == 1 and abs(col1 - col2) == 4)

    def goal_test(self, state):
        """Check if all columns filled, no conflicts."""
        if state[-1] == -1:
            return False
        return not any(self.conflicted(state, state[col], col)
                       for col in range(len(state)))

    def h(self, node):
        """Return number of conflicting queens for a given node"""
        num_conflicts = 0
        for (r1, c1) in enumerate(node.state):
            for (r2, c2) in enumerate(node.state):
                if (r1, c1) != (r2, c2):
                    num_conflicts += self.conflict(r1, c1, r2, c2)

        return num_conflicts


problem = NAmazonsProblem(int(sys.argv[1]))
# problem = NAmazonsProblem(30)
start_timer = time.perf_counter()

node = astar_search(problem, problem.h, display=False)

end_timer = time.perf_counter()


# example of print
path = node.path()

print('Number of moves: ', str(node.depth))

# for n in path:
    # assuming that the _str_ function of state outputs the correct format
    # print(n.state)
for n in path:
    state_str = ""
    for col in range(len(n.state)):
        row_str = ""
        for row in range(len(n.state)):
            if n.state[col] == row:
                row_str += "A"  # Amazon present at this position
            else:
                row_str += "#"  # Empty cell
        state_str += row_str + '\n'
    print(state_str)
# print("Time: ", end_timer - start_timer)
    # state_str = ""
    # for row in n.state:
    #     state_str += ''.join(row) + '\n'
    # print(state_str)
    
