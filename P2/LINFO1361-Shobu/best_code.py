class AI(Agent):

    def __init__(self, player, game):
        super().__init__(player, game)
        self.max_depth = 2
        self.remaining_time = 300
        self.killer_moves = [None for _ in range(self.max_depth)] 
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
        _, action = self.max_value(
            state, -float("inf"), float("inf"), 0, depth)
        return _, action

    def max_value(self, state, alpha, beta, depth, max_depth):
        if self.is_cutoff(state, depth) or self.is_quiescent(state) or depth == max_depth:
            return self.eval(state), None

        v, best_action = -float("inf"), None
        actions = self.game.actions(state)
        actions.sort(key=lambda action: -1 if action in self.killer_moves else 1)

        for action in actions:
            new_state = self.game.result(state, action)
            new_v, _ = self.min_value(
                new_state, alpha, beta, depth + 1, max_depth)
            if new_v > v:
                v, best_action = new_v, action
                hash_key = self.compute_zobrist_hash(new_state)
                if hash_key in self.transposition_table:
                    entry = self.transposition_table[hash_key]
                    if entry[0] < v:
                        self.transposition_table[hash_key] = (
                            v, best_action, entry[2])
                    else:
                        self.transposition_table[hash_key] = (v, best_action, entry[2])
                else:
                    if (self.is_quiescent(new_state)):
                        self.transposition_table[hash_key] = (
                            v, best_action, 1)
                    else:
                        self.transposition_table[hash_key] = (
                            v, best_action, 0)
                alpha = max(alpha, v)
            if v >= beta:
                self.killer_moves[depth] = action 
                hash_key = self.compute_zobrist_hash(new_state)
                if hash_key in self.transposition_table:
                    entry = self.transposition_table[hash_key]
                    if entry[0] < v:
                        self.transposition_table[hash_key] = (
                            v, best_action, entry[2])
                else:
                    if (self.is_quiescent(new_state)):
                        self.transposition_table[hash_key] = (
                            v, best_action, 1)
                    else:
                        self.transposition_table[hash_key] = (
                            v, best_action, 0)
        entries_1 = [] 
        entries_0 = [] 

        for entry in self.transposition_table.values():
            if entry[2] == 1:
                entries_1.append(entry)
            else:
                entries_0.append(entry)

        entries_1.sort(key=lambda entry: entry[0], reverse=True)
        entries_0.sort(key=lambda entry: entry[0], reverse=True)
    
        if len(entries_1) == 0:
            return (entries_0[0][0], entries_0[0][1])

        # sorted_entries = sorted(self.transposition_table.values(), key=lambda entry: entry[0], reverse=True)
        return (entries_1[0][0], entries_1[0][1])

    def min_value(self, state, alpha, beta, depth, max_depth):
        if self.is_cutoff(state, depth) or self.is_quiescent(state) or depth == max_depth:
            return self.eval(state), None

        v, best_action = float("inf"), float("inf")
        actions = self.game.actions(state)

        # Reorder actions so that killer moves are first
        actions.sort(key=lambda action: -
                     1 if action in self.killer_moves else 1)

        for action in actions:
            new_state = self.game.result(state, action)
            new_v, _ = self.max_value(
                new_state, alpha, beta, depth + 1, max_depth)
            if new_v < v:
                v, best_action = new_v, action
                beta = min(beta, v)
            if v <= alpha:
                self.killer_moves[depth] = action  # Update killer move
                return v, best_action
        return v, best_action

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
        num_stones_player = sum([len(state.board[i][j]) for i in range(
            4) for j in range(2) if state.board[i][j] == player])
        num_stones_opponent = sum([len(state.board[i][j]) for i in range(
            4) for j in range(2) if state.board[i][j] == opponent])
        stone_diff = num_stones_player - num_stones_opponent
        num_close_to_edge_player = sum([1 for i in range(4) for j in range(
            2) if state.board[i][j] == player and (i == 0 or i == 3)])
        num_close_to_edge_opponent = sum([1 for i in range(4) for j in range(
            2) if state.board[i][j] == opponent and (i == 0 or i == 3)])
        num_moves_player = len(self.game.actions(state))

        # Combine the factors into a single heuristic value
        heuristic_value = old_eval + stone_diff - num_close_to_edge_player + \
            num_close_to_edge_opponent + math.log(num_moves_player + 1)

        return heuristic_value

    def compute_zobrist_hash(self, state):
        hash_value = 0
        for i in range(len(state.board)):
            for j in range(len(state.board[0])):
                piece = state.board[i][j]
                if piece in [0, 1, -1]:  # Ensure piece is a valid player identifier
                    hash_value ^= self.zobrist_keys[(i, j, piece)]
        return hash_value

    def favoriser_mouvements(self, state, player):
        # favorable_moves = []
        # New eval logic
        num_player_stones = sum([len(state.board[i][j]) for i in range(
            4) for j in range(2) if state.board[i][j] == player])
        num_opponent_stones = sum([len(state.board[i][j]) for i in range(
            4) for j in range(2) if state.board[i][j] == 1-player])
        if num_player_stones > num_opponent_stones:
            for i in range(len(state.board)):
                for j in range(len(state.board[0])):
                    if player in state.board[i][j]:
                        if j == 0:
                            if i < len(state.board) - 1 and state.board[i + 1][j] == set():
                                return True
                        elif j == 1:
                            if i > 0 and state.board[i - 1][j] == set():
                                return True
                                # favorable_moves.append((i, j, i - 1, j))
                        # Vérifier si l'adversaire peut être bloqué
                        if i == 0 or i == len(state.board) - 1:
                            continue  # Éviter les mouvements aux bords
                        if j == 0:
                            if state.board[i + 1][j] == set():
                                # favorable_moves.append((i, j, i + 1, j))
                                return True
                        elif j == 1:
                            if state.board[i - 1][j] == set():
                                # favorable_moves.append((i, j, i - 1, j))
                                return
                        # Vérifier si mes propres pierres ne sont pas vulnérables à l'éjection
                        if j == 0:
                            if i > 0 and 1 - player in state.board[i - 1][j]:
                                continue  # Éviter les mouvements qui éjectent mes pierres
                        elif j == 1:
                            if i < len(state.board) - 1 and 1 - player in state.board[i + 1][j]:
                                continue  # Éviter les mouvements qui éjectent mes pierres
        return False

    def is_quiescent(self, state):
        # if self.is_stable_position(state):
        #     return True

        # if self.has_immediate_capture_or_threat(state):
        #     return False

        # return True
        if self.favoriser_mouvements(state,self.player):
            return True
        return False

    def is_stable_position(self, state):
        for player in range(2):
            player_stones = []
            for i in range(len(state.board)):
                for j in range(len(state.board[0])):
                    if player in state.board[i][j]:
                        player_stones.append((i, j))
            if len(player_stones) < 2:
                return False

        for player in range(2):
            # Adjusted the range to avoid index out of range error
            for i in range(1, len(state.board) - 1):
                for j in range(len(state.board[0])):
                    if player in state.board[i][j]:
                        if j == 0:
                            if player not in state.board[i + 1][j]:
                                return False
                        elif j == 1:
                            if player not in state.board[i - 1][j]:
                                return False

        return True

    def has_immediate_capture_or_threat(self, state):
        for i in range(len(state.board)):
            for j in range(len(state.board[0])):
                if state.board[i][j] != set():
                    # Get the player from the set
                    player = next(iter(state.board[i][j]))
                    if j == 0:
                        if i < len(state.board) - 1 and state.board[i + 1][j] == set():
                            return True
                        if i < len(state.board) - 1 and player in state.board[i + 1][j] and player != state.board[i + 1][j]:
                            return True
                    elif j == 1:
                        if i > 0 and state.board[i - 1][j] == set():
                            return True
                        if i > 0 and player in state.board[i - 1][j] and player != state.board[i - 1][j]:
                            return True

        return False