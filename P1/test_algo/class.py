def dfs(matrix, visited, row, col, path, target_F):
    # Vérifie les limites de la matrice et si la cellule est déjà visitée ou un mur
    if (row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or
            visited[row][col] or matrix[row][col] == '#'):
        return False

    # Ajoute la cellule actuelle au chemin
    path.append((row, col))

    # Marque la cellule comme visitée
    visited[row][col] = True

    # Si une position 'F' est atteinte, marquez-la comme visitée
    if matrix[row][col] == 'F':
        target_F.remove((row, col))

    # Si toutes les positions 'F' ont été visitées, imprime le chemin et arrête la recherche
    if not target_F:
        print("Chemin trouvé :", path)
        return True

    # Recherche récursive vers le haut, le bas, la gauche et la droite
    if (dfs(matrix, visited, row - 1, col, path, target_F) or
            dfs(matrix, visited, row + 1, col, path, target_F) or
            dfs(matrix, visited, row, col - 1, path, target_F) or
            dfs(matrix, visited, row, col + 1, path, target_F)):
        return True

    # Retour en arrière si aucun chemin valide n'a été trouvé
    path.pop()
    return False

def find_path(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialise la matrice de visite à False
    visited = [[False] * cols for _ in range(rows)]

    # Trouve toutes les positions 'F'
    target_F = set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'F':
                target_F.add((i, j))

    # Trouve la position de départ 'P'
    start_row, start_col = None, None
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'P':
                start_row, start_col = i, j
                break

    # Vérifie si la position de départ 'P' est trouvée
    if start_row is None or start_col is None:
        print("Position de départ 'P' non trouvée.")
        return

    # Appel de la fonction DFS pour trouver un chemin
    dfs(matrix, visited, start_row, start_col, [], target_F)

# Matrice d'exemple
matrix = [
    "..P.....",
    "...#....",
    ".#..F...",
    ".####...",
    "F.....#.",
    "#...F..."
]

# Appel de la fonction pour trouver un chemin
find_path(matrix)
