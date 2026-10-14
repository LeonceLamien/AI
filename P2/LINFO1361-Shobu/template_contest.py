from agent import Agent
from time import time
import random
import math



class AI(Agent):

    def __init__(self, player, game):
        super().__init__(player, game)
        self.max_depth = 3
        self.beam_width=70
        self.remaining_time = 300
        self.killer_moves = [None for _ in range(self.max_depth)]  # Initialize killer_moves
        self.transposition_table = {}  # Initialize transposition table
        self.zobrist_keys = self.init_zobrist_keys()  # Initialize Zobrist keys

   

    def init_zobrist_keys(self):
        zobrist_keys = {}
        for position in range(16):  # There are 16 positions on each board
            for player in range(2):  # There are 2 players
            # Assign a random 64-bit integer to each (position, player) pair
                zobrist_keys[(position, player)] = random.getrandbits(64)
        return zobrist_keys
    def clear_transposition_table(self):
        self.transposition_table = {}


    def play(self, state, remaining_time):
        self.remaining_time = remaining_time
        start_time = time()
        best_action = None
        for depth in range(1, self.max_depth + 1):
            v, action = self.alpha_beta_search(state, depth)
            if time() - start_time >= self.remaining_time:
                break
            best_action = action
        return best_action
    
    def alpha_beta_search(self, state, depth):
        _, action = self.max_value(state, -float("inf"), float("inf"), 0, depth)
        return _, action

    def max_value(self, state, alpha, beta, depth, max_depth):
        if self.is_cutoff(state, depth) or depth == max_depth:
            return self.eval(state), None 

        v, best_action = -float("inf"), None
        actions = self.game.actions(state)
        if(self.game.max_count_boring_actions%10==0):
            self.beam_width+=10
            if self.beam_width > 200:
                self.beam_width =200
        # Reorder actions so that killer moves are first
        actions.sort(key=lambda action: -1 if action in self.killer_moves else 1)
        actions.sort(key=lambda action: -self.eval(self.game.result(state, action)))
        actions = actions[:self.beam_width]
        for action in actions:
            new_state = self.game.result(state, action)
            new_v, _ = self.min_value(new_state, alpha, beta, depth + 1, max_depth)
            if new_v > v:
                v, best_action = new_v, action
                alpha = max(alpha, v)
            if v >= beta:
                self.killer_moves[depth] = action # Update killer move
                return v, best_action
        return v, best_action


    def min_value(self, state, alpha, beta, depth, max_depth):
        if self.is_cutoff(state, depth) or depth == max_depth:
            return self.eval(state), None


        v, best_action = float("inf"), float("inf")
        actions = self.game.actions(state)
        if(self.game.max_count_boring_actions%10==0):
            self.beam_width+=10
            if self.beam_width > 200:
                self.beam_width =200
        # Reorder actions so that killer moves are first
        actions.sort(key=lambda action: 1 if action in self.killer_moves else 1)
        actions.sort(key=lambda action: -self.eval(self.game.result(state, action)))
        actions = actions[:self.beam_width]
        for action in actions:
            new_state = self.game.result(state, action)
            new_v, _ = self.max_value(new_state, alpha, beta, depth + 1, max_depth)
            if new_v < v:
                v, best_action = new_v, action
                beta = min(beta, v)
            if v <= alpha:
                self.killer_moves[depth] = action  # Update killer move
                return v, best_action
        return v, best_action

    
    def is_cutoff(self, state, depth):
        return depth >= self.max_depth or self.game.is_terminal(state)
    
    def compute_zobrist_hash(self, state):
        hash_value = 0
        for board in state.board:
            for player in range(2):
                for position in board[player]:
                    hash_value ^= self.zobrist_keys[(position, player)]
        return hash_value


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
        num_stones_player = sum(len(state.board[i][j]) for i in range(4) for j in range(2) if j == player)
        num_stones_opponent = sum(len(state.board[i][j]) for i in range(4) for j in range(2) if j == opponent)
        stone_diff = num_stones_player - num_stones_opponent
        num_close_to_edge_player = 0
        num_close_to_edge_opponent = 0
        mid_player = 0
        mid_opponent = 0
        for i in range(4):
            for j in range(2):
                if i == 2 or i == 3:
                    player= 1-player
                    opponent= 1-opponent
                if j == player and len({8,11,4,7,12,15,13,14} & state.board[i][j]) != 0:
                    num_close_to_edge_player+=1
                elif j == opponent and len({8,11,4,7,12,15,13,14} & state.board[i][j]) != 0:
                    num_close_to_edge_opponent+=1
                elif j == opponent and len({9,10,6,5} & state.board[i][j]) != 0:
                    mid_opponent+=30
                elif j == player and len({9,10,6,5} & state.board[i][j]) != 0:
                    mid_player+=30
        num_moves_player = len(self.game.actions(state))
        # Combine the factors into a single heuristic value
        heuristic_value =  (math.log(num_moves_player + 1)+old_eval+stone_diff) -num_close_to_edge_opponent + num_close_to_edge_player
        return heuristic_value