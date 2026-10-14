import random
import time
import math
import sys

 

def objective_score(board):
    score = 0

    # Check rows
    for row in range(9):
        score -= len(set(board[row]))

    # Check columns
    for col in range(9):
        column_values = [board[row][col] for row in range(9)]
        score -= len(set(column_values))

    # Check subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid_values = [board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
            score -= len(set(subgrid_values))

    return score



def simulated_annealing_solver(initial_board):
    current_solution = [row[:] for row in initial_board]
    best_solution = current_solution
    current_score = objective_score(current_solution)
    best_score = current_score

    temperature = 1.0
    cooling_rate = 0.99999  # Adjust this parameter to control the cooling rate

    while temperature > 0.0001:
        try:
            # Generate a neighbor
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            while initial_board[row][col] != 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
            neighbor = [row[:] for row in current_solution]
            neighbor[row][col] = random.randint(1, 9)

            # Evaluate the neighbor
            neighbor_score = objective_score(neighbor)

            # Calculate acceptance probability
            delta = float(current_score - neighbor_score)
            
            # Accept the neighbor with a probability based on the acceptance probability
            if  (math.exp((delta/temperature)) - random.random()) > 0:
                current_solution = neighbor
                current_score = neighbor_score

            if current_score < best_score:
                best_solution = current_solution
                best_score = current_score

            # Cool down the temperature
            temperature *= cooling_rate
            
        except:
            print("Break asked")
            break
        
    return best_solution, best_score

 
def print_board(board):

    """Print the Sudoku board."""

    for row in board:
        print("".join(map(str, row)))

 

def read_sudoku_from_file(file_path):
    """Read Sudoku puzzle from a text file."""
    
    with open(file_path, 'r') as file:
        sudoku = [[int(num) for num in line.strip()] for line in file]

    return sudoku
 

if __name__ == "__main__":

    # Reading Sudoku from file
    initial_board = read_sudoku_from_file(sys.argv[1])

    # Solving Sudoku using simulated annealing
    start_timer = time.perf_counter()

    solved_board, current_score = simulated_annealing_solver(initial_board)

    end_timer = time.perf_counter()

    print_board(solved_board)
    print("\nValue(C):", current_score)

    # print("\nTime taken:", end_timer - start_timer, "seconds")