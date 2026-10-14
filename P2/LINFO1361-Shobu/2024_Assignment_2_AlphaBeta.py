from agent import Agent

class AlphaBetaAgent(Agent):

    def __init__(self, player, game, max_depth):

        super().__init__(player, game)
        self.max_depth = max_depth

    def play(self, state, remaining_time):

        return self.alpha_beta_search(state)
    
    def is_cutoff(self, state, depth):
 
        return depth >= self.max_depth or self.game.is_terminal(state)
    
    def eval(self, state):

        minW=float("inf")
        minB=float("inf")
        player=self.player
        opponent=1-player
        
        for i in range(4):
            for j in range(2):
                seet=state.board[i][j]
                tmin=len(seet)
                
                if j==0:
                    if tmin < minW:
                        minW=tmin
                elif j==1:
                    if tmin < minB:
                        minB=tmin
        pieces=[minW,minB]
        return pieces[player]-pieces[opponent]
        


    def alpha_beta_search(self, state):

        _, action = self.max_value(state, -float("inf"), float("inf"), 0)
        return action

    def max_value(self, state, alpha, beta, depth):
        if self.is_cutoff(state, depth):
            return self.eval(state), None
        v, best_action = -float("inf"), -float("inf")
        for action in self.game.actions(state):
            new_state = self.game.result(state, action)
            new_v, new_action = self.min_value(new_state, alpha, beta, depth + 1)
            if new_v > v:
                v, best_action = new_v, action
                alpha = max(alpha, v)
            if v >= beta:
                return (v, best_action)
        return v, best_action


    def min_value(self, state, alpha, beta, depth):
        if self.is_cutoff(state, depth):
            return self.eval(state), None
        v, best_action = float("inf"), float("inf")
        for action in self.game.actions(state):
            new_state = self.game.result(state, action)
            new_v, new_action = self.max_value(new_state, alpha, beta, depth + 1)
            if new_v < v:
                v, best_action = new_v, action
                beta = min(beta, v)
            if v <= alpha:
                return (v, best_action)
        return (v, best_action)
    
    def favoriser_mouvements(state, player):
        favorable_moves = []
        num_player_stones = sum([len(cell) for row in state.next_board for cell in row if player in cell])
        num_opponent_stones = sum([len(cell) for row in state.next_board for cell in row if 1 - player in cell])
        if num_player_stones > num_opponent_stones:
            # Recherche des mouvements pour sortir l'adversaire ou le coincer
            for i in range(len(state.next_board)):
                for j in range(len(state.next_board[0])):
                    if player in state.next_board[i][j]:
                        # Vérifier si l'adversaire peut être poussé hors du plateau
                        if j == 0:
                            if i < len(state.next_board) - 1 and state.next_board[i + 1][j] == set():
                                favorable_moves.append((i, j, i + 1, j))
                        elif j == 1:
                            if i > 0 and state.next_board[i - 1][j] == set():
                                favorable_moves.append((i, j, i - 1, j))
                        # Vérifier si l'adversaire peut être bloqué
                        if i == 0 or i == len(state.next_board) - 1:
                            continue  # Éviter les mouvements aux bords
                        if j == 0:
                            if state.next_board[i + 1][j] == set():
                                favorable_moves.append((i, j, i + 1, j))
                        elif j == 1:
                            if state.next_board[i - 1][j] == set():
                                favorable_moves.append((i, j, i - 1, j))
                        # Vérifier si mes propres pierres ne sont pas vulnérables à l'éjection
                        if j == 0:
                            if i > 0 and 1 - player in state.next_board[i - 1][j]:
                                continue  # Éviter les mouvements qui éjectent mes pierres
                        elif j == 1:
                            if i < len(state.next_board) - 1 and 1 - player in state.next_board[i + 1][j]:
                                continue  # Éviter les mouvements qui éjectent mes pierres
        return favorable_moves
