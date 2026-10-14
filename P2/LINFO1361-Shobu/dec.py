def read_logs(file):
    actions = []
    with open(file, "r") as f:
        lines = f.readlines()[0].split("|")
        for line in lines[:-1]:
            n_move, action = convert_log_to_action(line.strip())
            actions.append((action, n_move))
    return actions