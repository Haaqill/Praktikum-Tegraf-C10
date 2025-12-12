N = 8
moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

def is_valid(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def degree(x, y, board):
    c = 0
    for dx, dy in moves:
        if is_valid(x+dx, y+dy, board):
            c += 1
    return c

def ordered_moves(x, y, board):
    cand = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, board):
            cand.append((degree(nx, ny, board), nx, ny))
    cand.sort(key=lambda x: x[0])
    return [(nx, ny) for _, nx, ny in cand]

def closed_knight_dfs(x, y, movei, board, path, start):
    board[x][y] = movei
    path.append((x, y))

    # Complete
    if movei == N*N - 1:
        sx, sy = start
        if (abs(x - sx), abs(y - sy)) in [(1,2),(2,1)]:
            return True
        board[x][y] = -1
        path.pop()
        return False

    for nx, ny in ordered_moves(x, y, board):
        if closed_knight_dfs(nx, ny, movei + 1, board, path, start):
            return True

    board[x][y] = -1
    path.pop()
    return False

def rotate_path_to_start(path, desired_start):
    idx = path.index(desired_start)
    return path[idx:] + path[:idx]


sx = int(input("Baris X (0-7): "))
sy = int(input("Kolom Y (0-7): "))
start = (sx, sy)

# Optimal DFS
temp_start = (3,3)
board = [[-1]*N for _ in range(N)]
path = []

closed_knight_dfs(temp_start[0], temp_start[1], 0, board, path, temp_start)

# Rotate
rotated = rotate_path_to_start(path, start)

# Map
final_board = [[-1]*N for _ in range(N)]
for i, (x, y) in enumerate(rotated):
    final_board[x][y] = i

print("\nClosed Knight's Tour", start)
print("-----------------------------------------------------")
for row in final_board:
    print(" ".join(f"{x:2d}" for x in row))
