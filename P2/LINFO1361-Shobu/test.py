# from agent import Agent


# class AlphaBetaAgent(Agent):
#     def __init__(self, player, game):
#         super().__init__(player, game)
#         self.max_depth = 2
#         self.beam_width= 20

#     def play(self, state, remaining_time):
#         return self.alpha_beta_search(state)
#     def alpha_beta_search(self, state):
#         _, action = self.max_value(state, -float("inf"), float("inf"), 0)
#         return action
#     def is_cutoff(self, state, depth):
#         return depth >= self.max_depth or self.game.is_terminal(state)
    
    
#     def eval(self, state):
#         player = self.player
#         opponent = 1 - player
#         player_score = 0
#         opponent_score = 0
        
#         for i in range(4):
#             for j in range(2):
#                 for piece in state.board[i][j]:
#                     if j == player: 
#                         player_score += self.get_piece_value(piece, i)
#                     elif j == opponent:   
#                         opponent_score += self.get_piece_value(piece, i)

#         return player_score - opponent_score

#     def get_piece_value(self, piece, row):
#         if row == 0:
#             return 2 if piece == 'P' else 5 
#         elif row == 1:
#             return 3 if piece == 'P' else 4 
#         else:
#             return 1 

#     def max_value(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = -float("inf"), -float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, new_action = self.min_value(new_state, alpha, beta, depth + 1)
#             if new_v > v:
#                 v, best_action = new_v, action
#                 alpha = max(alpha, v)
#             if v >= beta:
#                 return (v, best_action)
#         return v, best_action

#     def min_value(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = float("inf"), float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, new_action = self.max_value(new_state, alpha, beta, depth + 1)
#             if new_v < v:
#                 v, best_action = new_v, action
#                 beta = min(beta, v)
#             if v <= alpha:
#                 return (v, best_action)
#         return (v, best_action)

#     def alpha_beta_search(self, state):
#         _, action = self.max_value(state, -float("inf"), float("inf"), 0)
#         return action

#     def quiescence_search(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v = self.eval(state)
#         if v >= beta:
#             return beta, None
#         alpha = max(alpha, v)
#         for action in self.game.quiet_actions(state):
#             new_state = self.game.result(state, action)
#             new_v, _ = self.quiescence_search(new_state, -beta, -alpha, depth + 1)
#             v = max(v, -new_v)
#             alpha = max(alpha, v)
#             if v >= beta:
#                 return beta, None
#         return v, None

#     def max_value_quiescence(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = -float("inf"), -float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, _ = self.quiescence_search(new_state, alpha, beta, depth + 1)
#             if new_v > v:
#                 v, best_action = new_v, action
#                 alpha = max(alpha, v)
#             if v >= beta:
#                 return (v, best_action)
#         return v, best_action

#     def min_value_quiescence(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = float("inf"), float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, _ = self.quiescence_search(new_state, alpha, beta, depth + 1)
#             if new_v < v:
#                 v, best_action = new_v, action
#                 beta = min(beta, v)
#             if v <= alpha:
#                 return (v, best_action)
#         return (v, best_action)
    
    
# from agent import Agent

# class AlphaBetaAgent(Agent):
#     """An agent that uses the alpha-beta pruning algorithm to determine the best move.

#     This agent extends the base Agent class, providing an implementation of the play
#     method that utilizes the alpha-beta pruning technique to make decisions more efficiently.

#     Attributes:
#         max_depth (int): The maximum depth the search algorithm will explore.
#     """

#     def __init__(self, player, game):
#         """Initializes an AlphaBetaAgent instance with a specified player, game, and maximum search depth.

#         Args:
#             player (int): The player ID this agent represents (0 or 1).
#             game (ShobuGame): The Shobu game instance the agent will play on.
#             max_depth (int): The maximum depth of the search tree.
#         """
#         super().__init__(player, game)
#         self.max_depth = 2

#     def play(self, state, remaining_time):
#         """Determines the best action by applying the alpha-beta pruning algorithm.

#         Overrides the play method in the base class.

#         Args:
#             state (ShobuState): The current state of the game.
#             remaining_time (float): The remaining time in seconds that the agent has to make a decision.

#         Returns:
#             ShobuAction: The action determined to be the best by the alpha-beta algorithm.
#         """
#         return self.alpha_beta_search(state)
    
#     def is_cutoff(self, state, depth):
#         """Determines if the search should be cut off at the current depth.

#         Args:
#             state (ShobuState): The current state of the game.
#             depth (int): The current depth in the search tree.

#         Returns:
#             bool: True if the search should be cut off, False otherwise.
#         """
#         return depth >= self.max_depth or self.game.is_terminal(state)
    
#     def eval(self, state):
#         """Evaluates the given state and returns a score from the perspective of the agent's player.

#         Args:
#             state (ShobuState): The game state to evaluate.

#         Returns:
#             float: The evaluated score of the state.
#         """
#         minW=float("inf")
#         minB=float("inf")
#         player=self.player
#         opponent=1-player
        
#         for i in range(4):
#             for j in range(2):
#                 seet=state.board[i][j]
#                 tmin=len(seet)
                
#                 if j==0:
#                     if tmin < minW:
#                         minW=tmin
#                 elif j==1:
#                     if tmin < minB:
#                         minB=tmin
#         pieces=[minW,minB]
#         return pieces[player]-pieces[opponent]
        


#     def alpha_beta_search(self, state):
#         """Implements the alpha-beta pruning algorithm to find the best action.

#         Args:
#             state (ShobuState): The current game state.

#         Returns:
#             ShobuAction: The best action as determined by the alpha-beta algorithm.
#         """
#         _, action = self.max_value(state, -float("inf"), float("inf"), 0)
#         return action

#     def max_value(self, state, alpha, beta, depth):
#         """Computes the maximum achievable value for the current player at a given state using the alpha-beta pruning.

#         This method recursively explores all possible actions from the current state to find the one that maximizes
#         the player's score, pruning branches that cannot possibly affect the final decision.

#         Args:
#             state (ShobuState): The current state of the game.
#             alpha (float): The current alpha value, representing the minimum score that the maximizing player is assured of.
#             beta (float): The current beta value, representing the maximum score that the minimizing player is assured of.
#             depth (int): The current depth in the search tree.

#         Returns:
#             tuple: A tuple containing the best value achievable from this state and the action that leads to this value.
#                 If the state is a terminal state or the depth limit is reached, the action will be None.
#         """
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = -float("inf"), -float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, new_action = self.min_value(new_state, alpha, beta, depth + 1)
#             if new_v > v:
#                 v, best_action = new_v, action
#                 alpha = max(alpha, v)
#             if v >= beta:
#                 return (v, best_action)
#         return v, best_action


#     def min_value(self, state, alpha, beta, depth):
#         """Computes the minimum achievable value for the opposing player at a given state using the alpha-beta pruning.

#         Similar to max_value, this method recursively explores all possible actions from the current state to find
#         the one that minimizes the opponent's score, again using alpha-beta pruning to cut off branches that won't
#         affect the outcome.

#         Args:
#             state (ShobuState): The current state of the game.
#             alpha (float): The current alpha value, representing the minimum score that the maximizing player is assured of.
#             beta (float): The current beta value, representing the maximum score that the minimizing player is assured of.
#             depth (int): The current depth in the search tree.

#         Returns:
#             tuple: A tuple containing the best value achievable from this state for the opponent and the action that leads to this value.
#                 If the state is a terminal state or the depth limit is reached, the action will be None.
#         """
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = float("inf"), float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, new_action = self.max_value(new_state, alpha, beta, depth + 1)
#             if new_v < v:
#                 v, best_action = new_v, action
#                 beta = min(beta, v)
#             if v <= alpha:
#                 return (v, best_action)
#         return (v, best_action)
# from agent import Agent


# class AlphaBetaAgent(Agent):
#     def __init__(self, player, game):
#         super().__init__(player, game)
#         self.max_depth = 2
#         self.beam_width= 20

#     def play(self, state, remaining_time):
#         return self.alpha_beta_search(state)
#     def alpha_beta_search(self, state):
#         _, action = self.max_value(state, -float("inf"), float("inf"), 0)
#         return action
#     def is_cutoff(self, state, depth):
#         return depth >= self.max_depth or self.game.is_terminal(state)
    
    
#     def eval(self, state):
#         player = self.player
#         opponent = 1 - player
#         player_score = 0
#         opponent_score = 0
        
#         for i in range(4):
#             for j in range(2):
#                 for piece in state.board[i][j]:
#                     if j == player: 
#                         player_score += self.get_piece_value(piece, i)
#                     elif j == opponent:   
#                         opponent_score += self.get_piece_value(piece, i)

#         return player_score - opponent_score

#     def get_piece_value(self, piece, row):
#         if row == 0:
#             return 2 if piece == 'P' else 5 
#         elif row == 1:
#             return 3 if piece == 'P' else 4 
#         else:
#             return 1 

#     def max_value(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = -float("inf"), -float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, new_action = self.min_value(new_state, alpha, beta, depth + 1)
#             if new_v > v:
#                 v, best_action = new_v, action
#                 alpha = max(alpha, v)
#             if v >= beta:
#                 return (v, best_action)
#         return v, best_action

#     def min_value(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = float("inf"), float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, new_action = self.max_value(new_state, alpha, beta, depth + 1)
#             if new_v < v:
#                 v, best_action = new_v, action
#                 beta = min(beta, v)
#             if v <= alpha:
#                 return (v, best_action)
#         return (v, best_action)

#     def alpha_beta_search(self, state):
#         _, action = self.max_value(state, -float("inf"), float("inf"), 0)
#         return action

#     def quiescence_search(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v = self.eval(state)
#         if v >= beta:
#             return beta, None
#         alpha = max(alpha, v)
#         for action in self.game.quiet_actions(state):
#             new_state = self.game.result(state, action)
#             new_v, _ = self.quiescence_search(new_state, -beta, -alpha, depth + 1)
#             v = max(v, -new_v)
#             alpha = max(alpha, v)
#             if v >= beta:
#                 return beta, None
#         return v, None

#     def max_value_quiescence(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = -float("inf"), -float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, _ = self.quiescence_search(new_state, alpha, beta, depth + 1)
#             if new_v > v:
#                 v, best_action = new_v, action
#                 alpha = max(alpha, v)
#             if v >= beta:
#                 return (v, best_action)
#         return v, best_action

#     def min_value_quiescence(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = float("inf"), float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, _ = self.quiescence_search(new_state, alpha, beta, depth + 1)
#             if new_v < v:
#                 v, best_action = new_v, action
#                 beta = min(beta, v)
#             if v <= alpha:
#                 return (v, best_action)
#         return (v, best_action)

from agent import Agent

# class AlphaBetaAgent(Agent):
#     """An agent that uses the alpha-beta pruning algorithm to determine the best move.

#     This agent extends the base Agent class, providing an implementation of the play
#     method that utilizes the alpha-beta pruning technique to make decisions more efficiently.

#     Attributes:
#         max_depth (int): The maximum depth the search algorithm will explore.
#     """

#     def __init__(self, player, game):
#         """Initializes an AlphaBetaAgent instance with a specified player, game, and maximum search depth.

#         Args:
#             player (int): The player ID this agent represents (0 or 1).
#             game (ShobuGame): The Shobu game instance the agent will play on.
#             max_depth (int): The maximum depth of the search tree.
#         """
#         super().__init__(player, game)
#         self.max_depth = 2

#     def play(self, state, remaining_time):
#         """Determines the best action by applying the alpha-beta pruning algorithm.

#         Overrides the play method in the base class.

#         Args:
#             state (ShobuState): The current state of the game.
#             remaining_time (float): The remaining time in seconds that the agent has to make a decision.

#         Returns:
#             ShobuAction: The action determined to be the best by the alpha-beta algorithm.
#         """
#         return self.alpha_beta_search(state)
    
#     def is_cutoff(self, state, depth):
#         """Determines if the search should be cut off at the current depth.

#         Args:
#             state (ShobuState): The current state of the game.
#             depth (int): The current depth in the search tree.

#         Returns:
#             bool: True if the search should be cut off, False otherwise.
#         """
#         return depth >= self.max_depth or self.game.is_terminal(state)
    
#     def eval(self, state):
#         """Evaluates the given state and returns a score from the perspective of the agent's player.

#         Args:
#             state (ShobuState): The game state to evaluate.

#         Returns:
#             float: The evaluated score of the state.
#         """
#         minW=float("inf")
#         minB=float("inf")
#         player=self.player
#         opponent=1-player
        
#         for i in range(4):
#             for j in range(2):
#                 seet=state.board[i][j]
#                 tmin=len(seet)
                
#                 if j==0:
#                     if tmin < minW:
#                         minW=tmin
#                 elif j==1:
#                     if tmin < minB:
#                         minB=tmin
#         pieces=[minW,minB]
#         return pieces[player]-pieces[opponent]
        


#     def alpha_beta_search(self, state):
#         """Implements the alpha-beta pruning algorithm to find the best action.

#         Args:
#             state (ShobuState): The current game state.

#         Returns:
#             ShobuAction: The best action as determined by the alpha-beta algorithm.
#         """
#         _, action = self.max_value(state, -float("inf"), float("inf"), 0)
#         return action

#     def max_value(self, state, alpha, beta, depth):
#         """Computes the maximum achievable value for the current player at a given state using the alpha-beta pruning.

#         This method recursively explores all possible actions from the current state to find the one that maximizes
#         the player's score, pruning branches that cannot possibly affect the final decision.

#         Args:
#             state (ShobuState): The current state of the game.
#             alpha (float): The current alpha value, representing the minimum score that the maximizing player is assured of.
#             beta (float): The current beta value, representing the maximum score that the minimizing player is assured of.
#             depth (int): The current depth in the search tree.

#         Returns:
#             tuple: A tuple containing the best value achievable from this state and the action that leads to this value.
#                 If the state is a terminal state or the depth limit is reached, the action will be None.
#         """
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = -float("inf"), -float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, new_action = self.min_value(new_state, alpha, beta, depth + 1)
#             if new_v > v:
#                 v, best_action = new_v, action
#                 alpha = max(alpha, v)
#             if v >= beta:
#                 return (v, best_action)
#         return v, best_action


#     def min_value(self, state, alpha, beta, depth):
#         """Computes the minimum achievable value for the opposing player at a given state using the alpha-beta pruning.

#         Similar to max_value, this method recursively explores all possible actions from the current state to find
#         the one that minimizes the opponent's score, again using alpha-beta pruning to cut off branches that won't
#         affect the outcome.

#         Args:
#             state (ShobuState): The current state of the game.
#             alpha (float): The current alpha value, representing the minimum score that the maximizing player is assured of.
#             beta (float): The current beta value, representing the maximum score that the minimizing player is assured of.
#             depth (int): The current depth in the search tree.

#         Returns:
#             tuple: A tuple containing the best value achievable from this state for the opponent and the action that leads to this value.
#                 If the state is a terminal state or the depth limit is reached, the action will be None.
#         """
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = float("inf"), float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, new_action = self.max_value(new_state, alpha, beta, depth + 1)
#             if new_v < v:
#                 v, best_action = new_v, action
#                 beta = min(beta, v)
#             if v <= alpha:
#                 return (v, best_action)
#         return (v, best_action)

# from agent import Agent


# class AlphaBetaAgent(Agent):
#     def __init__(self, player, game):
#         super().__init__(player, game)
#         self.max_depth = 2
#         self.beam_width= 20

#     def play(self, state, remaining_time):
#         return self.alpha_beta_search(state)
#     def alpha_beta_search(self, state):
#         _, action = self.max_value(state, -float("inf"), float("inf"), 0)
#         return action
#     def is_cutoff(self, state, depth):
#         return depth >= self.max_depth or self.game.is_terminal(state)
    
    
#     def eval(self, state):
#         player = self.player
#         opponent = 1 - player
#         player_score = 0
#         opponent_score = 0
        
#         for i in range(4):
#             for j in range(2):
#                 for piece in state.board[i][j]:
#                     if j == player: 
#                         player_score += self.get_piece_value(piece, i)
#                     elif j == opponent:   
#                         opponent_score += self.get_piece_value(piece, i)

#         return player_score - opponent_score

#     def get_piece_value(self, piece, row):
#         if row == 0:
#             return 2 if piece == 'P' else 5 
#         elif row == 1:
#             return 3 if piece == 'P' else 4 
#         else:
#             return 1 

#     def max_value(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = -float("inf"), -float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, new_action = self.min_value(new_state, alpha, beta, depth + 1)
#             if new_v > v:
#                 v, best_action = new_v, action
#                 alpha = max(alpha, v)
#             if v >= beta:
#                 return (v, best_action)
#         return v, best_action

#     def min_value(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = float("inf"), float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, new_action = self.max_value(new_state, alpha, beta, depth + 1)
#             if new_v < v:
#                 v, best_action = new_v, action
#                 beta = min(beta, v)
#             if v <= alpha:
#                 return (v, best_action)
#         return (v, best_action)

#     def alpha_beta_search(self, state):
#         _, action = self.max_value(state, -float("inf"), float("inf"), 0)
#         return action

#     def quiescence_search(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v = self.eval(state)
#         if v >= beta:
#             return beta, None
#         alpha = max(alpha, v)
#         for action in self.game.quiet_actions(state):
#             new_state = self.game.result(state, action)
#             new_v, _ = self.quiescence_search(new_state, -beta, -alpha, depth + 1)
#             v = max(v, -new_v)
#             alpha = max(alpha, v)
#             if v >= beta:
#                 return beta, None
#         return v, None

#     def max_value_quiescence(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = -float("inf"), -float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, _ = self.quiescence_search(new_state, alpha, beta, depth + 1)
#             if new_v > v:
#                 v, best_action = new_v, action
#                 alpha = max(alpha, v)
#             if v >= beta:
#                 return (v, best_action)
#         return v, best_action

#     def min_value_quiescence(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = float("inf"), float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, _ = self.quiescence_search(new_state, alpha, beta, depth + 1)
#             if new_v < v:
#                 v, best_action = new_v, action
#                 beta = min(beta, v)
#             if v <= alpha:
#                 return (v, best_action)
#         return (v, best_action)

# from agent import Agent

# class AlphaBetaAgent(Agent):
#     def __init__(self, player, game):
#         super().__init__(player, game)
#         self.max_depth = 2
#         self.beam_width= 20

#     def play(self, state, remaining_time):
#         return self.alpha_beta_search(state)
#     def alpha_beta_search(self, state):
#         _, action = self.max_value(state, -float("inf"), float("inf"), 0)
#         return action
#     def is_cutoff(self, state, depth):
#         return depth >= self.max_depth or self.game.is_terminal(state)
    
    
#     def eval(self, state):
#         player = self.player
#         opponent = 1 - player
#         player_score = 0
#         opponent_score = 0
        
#         for i in range(4):
#             for j in range(2):
#                 for piece in state.board[i][j]:
#                     if j == player: 
#                         player_score += self.get_piece_value(piece, i)
#                     elif j == opponent:   
#                         opponent_score += self.get_piece_value(piece, i)

#         return player_score - opponent_score

#     def get_piece_value(self, piece, row):
#         if row == 0:
#             return  5 
#         elif row == 1:
#             return 4 
#         else:
#             return 1 

#     def max_value(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = -float("inf"), -float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, new_action = self.min_value(new_state, alpha, beta, depth + 1)
#             if new_v > v:
#                 v, best_action = new_v, action
#                 alpha = max(alpha, v)
#             if v >= beta:
#                 return (v, best_action)
#         return v, best_action

#     def min_value(self, state, alpha, beta, depth):
#         if self.is_cutoff(state, depth):
#             return self.eval(state), None
#         v, best_action = float("inf"), float("inf")
#         for action in self.game.actions(state):
#             new_state = self.game.result(state, action)
#             new_v, new_action = self.max_value(new_state, alpha, beta, depth + 1)
#             if new_v < v:
#                 v, best_action = new_v, action
#                 beta = min(beta, v)
#             if v <= alpha:
#                 return (v, best_action)
#         return (v, best_action)
