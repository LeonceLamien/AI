from clause import *

"""
For the n-amazon problem, the only code you have to do is in this file.

You should replace

# your code here

by a code generating a list of clauses modeling the n-amazons problem
for the input file.

You should build clauses using the Clause class defined in clause.py

Here is an example presenting how to create a clause:
Let's assume that the length/width of the chessboard is 4.
To create a clause X_0_1 OR ~X_1_2 OR X_3_3
you can do:

clause = Clause(4)
clause.add_positive(0, 1)
clause.add_negative(1, 2)
clause.add_positive(3, 3)

The clause must be initialized with the length/width of the chessboard.
The reason is that we use a 2D index for our variables but the format
imposed by MiniSAT requires a 1D index.
The Clause class automatically handle this change of index, but needs to know the
number of column and row in the chessboard.

X_0_0 is the literal representing the top left corner of the chessboard
"""


# def get_expression(size: int, placed_amazons: list[(int, int)]) -> list[Clause]:
#     """
#     Defines the clauses for the N-amazons problem
#     :param size: length/width of the chessboard
#     :param placed_amazons: a list of the already placed amazons
#     :return: a list of clauses
#     """

#     expression = []
#     # your code here

#     return expression
def get_expression(size: int, placed_amazons: list[(int, int)]) -> list[Clause]:
    """
    Defines the clauses for the N-amazons problem
    :param size: length/width of the chessboard
    :param placed_amazons: a list of the already placed amazons
    :return: a list of clauses
    """

    expression = []

    # At least one Amazon per row and column
    for i in range(size):
        clause_row = Clause(size)
        clause_col = Clause(size)
        for j in range(size):
            clause_row.add_positive(i, j)
            clause_col.add_positive(j, i)
        expression.append(clause_row)
        expression.append(clause_col)

    # At most one Amazon per cell
    for i in range(size):
        for j in range(size):
            for k in range(j + 1, size):
                clause_row = Clause(size)
                clause_col = Clause(size)
                clause_row.add_negative(i, j)
                clause_row.add_negative(i, k)
                clause_col.add_negative(j, i)
                clause_col.add_negative(k, i)
                expression.append(clause_row)
                expression.append(clause_col)

    # No two Amazons can attack each other
    for i1 in range(size):
        for j1 in range(size):
            for i2 in range(i1, size):
                for j2 in range(j1 + 1 if i1 == i2 else 0, size):
                    if i1 != i2 or j1 != j2:  # Not the same cell
                        # Same row or column
                        if i1 == i2 or j1 == j2:
                            clause = Clause(size)
                            clause.add_negative(i1, j1)
                            clause.add_negative(i2, j2)
                            expression.append(clause)
                        # Diagonal
                        if abs(i1 - i2) == abs(j1 - j2):
                            clause = Clause(size)
                            clause.add_negative(i1, j1)
                            clause.add_negative(i2, j2)
                            expression.append(clause)
                        # 3x2 move
                        if abs(i1 - i2) == 3 and abs(j1 - j2) == 2 or abs(i1 - i2) == 2 and abs(j1 - j2) == 3:
                            clause = Clause(size)
                            clause.add_negative(i1, j1)
                            clause.add_negative(i2, j2)
                            expression.append(clause)
                        # 4x1 move
                        if abs(i1 - i2) == 4 and abs(j1 - j2) == 1 or abs(i1 - i2) == 1 and abs(j1 - j2) == 4:
                            clause = Clause(size)
                            clause.add_negative(i1, j1)
                            clause.add_negative(i2, j2)
                            expression.append(clause)

    # Amazons already placed
    for i, j in placed_amazons:
        clause = Clause(size)
        clause.add_positive(i, j)
        expression.append(clause)

    return expression
