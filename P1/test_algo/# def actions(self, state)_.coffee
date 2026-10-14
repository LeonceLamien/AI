    # def actions(self, state):
    #     actions = []
    #     pacman_x, pacman_y = None, None
    #     for x, row in enumerate(state.grid):
    #         for y, cell in enumerate(row):
    #             if cell == 'P':
    #                 pacman_x, pacman_y = x, y
    #                 break

    #     if pacman_x > 0 and state.grid[pacman_x - 1][pacman_y] != '#':
    #         actions.append('UP')
    #     if pacman_x < state.shape[0] - 1 and state.grid[pacman_x + 1][pacman_y] != '#':
    #         actions.append('DOWN')
    #     if pacman_y > 0 and state.grid[pacman_x][pacman_y - 1] != '#':
    #         actions.append('LEFT')
    #     if pacman_y < state.shape[1] - 1 and state.grid[pacman_x][pacman_y + 1] != '#':
    #         actions.append('RIGHT')

    #     return actions

    # def result(self, state, action):
    #     pacman_x, pacman_y = None, None

    #     for x, row in enumerate(state.grid):
    #         for y, cell in enumerate(row):
    #             if cell == 'P':
    #                 pacman_x, pacman_y = x, y
    #                 break

    #     new_grid = [list(row) for row in state.grid]

    #     if action == 'UP':
    #         if pacman_x > 0 and new_grid[pacman_x - 1][pacman_y] != '#':
    #             if new_grid[pacman_x - 1][pacman_y] == 'F':
    #                 state.answer -= 1
    #             new_grid[pacman_x][pacman_y] = '.'
    #             new_grid[pacman_x - 1][pacman_y] = 'P'
    #     elif action == 'DOWN':
    #         if pacman_x < state.shape[0] - 1 and new_grid[pacman_x + 1][pacman_y] != '#':
    #             if new_grid[pacman_x + 1][pacman_y] == 'F':
    #                 state.answer -= 1
    #             new_grid[pacman_x][pacman_y] = '.'
    #             new_grid[pacman_x + 1][pacman_y] = 'P'
    #     elif action == 'LEFT':
    #         if pacman_y > 0 and new_grid[pacman_x][pacman_y - 1] != '#':
    #             if new_grid[pacman_x][pacman_y - 1] == 'F':
    #                 state.answer -= 1
    #             new_grid[pacman_x][pacman_y] = '.'
    #             new_grid[pacman_x][pacman_y - 1] = 'P'
    #     elif action == 'RIGHT':
    #         if pacman_y < state.shape[1] - 1 and new_grid[pacman_x][pacman_y + 1] != '#':
    #             if new_grid[pacman_x][pacman_y + 1] == 'F':
    #                 state.answer -= 1
    #             new_grid[pacman_x][pacman_y] = '.'
    #             new_grid[pacman_x][pacman_y + 1] = 'P'

    #     return State(state.shape, new_grid, state.answer, action)

    # def goal_test(self, state):
    #     return state.answer == 0
