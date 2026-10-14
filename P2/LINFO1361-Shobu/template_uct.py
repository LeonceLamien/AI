from agent import Agent
from time import time
import math

class UCTAgent(Agent):
    def __init__(self, player, game):
        super().__init__(player, game)
        self.max_depth = 2
        self.remaining_time = 300
        self.killer_moves = [[] for _ in range(self.max_depth)]  # Initialize killer_moves
        self.transposition_table = {}
        self.history_table = {}

    def alpha_beta_search(self, state, depth, alpha, beta, ancestor_lbound=None):
        if self.is_cutoff(state, depth):
            return self.eval(state), None

        v, best_action = -float("inf"), None
        actions = self.game.actions(state)

        # Order moves based on history heuristic
        actions.sort(key=lambda action: self.history_table.get(action, 0), reverse=True)

        for action in actions:
            new_state = self.game.result(state, action)
            new_v, _ = self.min_value(new_state, depth + 1, alpha, beta, ancestor_lbound)
            if new_v > v:
                v, best_action = new_v, action
                alpha = max(alpha, v)
            if v >= beta:
                self.killer_moves[depth].append(action)  # Update killer move
                break
        return v, best_action

    def min_value(self, state, depth, alpha, beta, ancestor_lbound=None):
        if self.is_cutoff(state, depth):
            return self.eval(state), None

        v, best_action = float("inf"), None
        actions = self.game.actions(state)

        # Order moves based on history heuristic
        actions.sort(key=lambda action: self.history_table.get(action, 0), reverse=True)

        for action in actions:
            new_state = self.game.result(state, action)
            new_v, _ = self.max_value(new_state, depth + 1, alpha, beta, ancestor_lbound)
            if new_v < v:
                v, best_action = new_v, action
                beta = min(beta, v)
            if v <= alpha:
                break
        return v, best_action

    def max_value(self, state, depth, alpha, beta, ancestor_lbound=None):
        if self.is_cutoff(state, depth):
            return self.eval(state), None

        v, best_action = -float("inf"), None
        actions = self.game.actions(state)

        # Order moves based on history heuristic
        actions.sort(key=lambda action: self.history_table.get(action, 0), reverse=True)

        for action in actions:
            new_state = self.game.result(state, action)
            new_v, _ = self.min_value(new_state, depth + 1, alpha, beta, ancestor_lbound)
            if new_v > v:
                v, best_action = new_v, action
                alpha = max(alpha, v)
                
                # Check for deep alpha cut-off
                if ancestor_lbound is not None and v >= ancestor_lbound:
                    break  # Cut-off the search
        return v, best_action

    def play(self, state, remaining_time):
        self.remaining_time = remaining_time
        start_time = time()
        best_action = None

        for depth in range(1, self.max_depth + 1):
            v, action = self.alpha_beta_search(state, depth, -float("inf"), float("inf"))
            if time() - start_time >= self.remaining_time:
                break
            best_action = action

        return best_action
    def is_cutoff(self, state, depth):
        return depth >= self.max_depth or self.game.is_terminal(state)
    def eval(self, state):
        player = self.player
        opponent = 1 - player

        # Old eval logic
        minW = float("inf")
        minB = float("inf")
        for i in range(4):
            for j in range(2):
                seet = state.board[i][j]
                tmin = len(seet)
                if j == 0:
                    if tmin < minW:
                        minW = tmin
                elif j == 1:
                    if tmin < minB:
                        minB = tmin
        pieces = [minW, minB]
        old_eval = pieces[player] - pieces[opponent]

        # New eval logic
        num_stones_player = sum([len(state.board[i][j]) for i in range(4) for j in range(2) if state.board[i][j] == player])
        num_stones_opponent = sum([len(state.board[i][j]) for i in range(4) for j in range(2) if state.board[i][j] == opponent])
        stone_diff = num_stones_player - num_stones_opponent
        num_close_to_edge_player = sum([1 for i in range(4) for j in range(2) if state.board[i][j] == player and (i == 0 or i == 3)])
        num_close_to_edge_opponent = sum([1 for i in range(4) for j in range(2) if state.board[i][j] == opponent and (i == 0 or i == 3)])
        num_moves_player = len(self.game.actions(state))

        # Combine the factors into a single heuristic value
        heuristic_value = old_eval + stone_diff - num_close_to_edge_player + num_close_to_edge_opponent + math.log(num_moves_player + 1)

        return heuristic_value
