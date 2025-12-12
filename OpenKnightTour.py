N = 8

moves = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def is_valid(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[y][x] == -1

def count_moves(x, y, board):
    count = 0
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, board):
            count += 1
    return count

def next_move(x, y, board):
    min_deg = 9
    next_x, next_y = None, None
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, board):
            deg = count_moves(nx, ny, board)
            if deg < min_deg:
                min_deg = deg
                next_x, next_y = nx, ny
    return next_x, next_y

def knights_tour(start_x, start_y):
    board = [[-1] * N for _ in range(N)]
    x, y = start_x, start_y
    board[y][x] = 0
    for step in range(1, N * N):
        nx, ny = next_move(x, y, board)
        if nx is None:
            return None
        x, y = nx, ny
        board[y][x] = step
    return board

def print_board(board):
    for row in board:
        print(" ".join(f"{c:2d}" for c in row))

sx = int(input("Baris X (0-7): "))
sy = int(input("Kolom Y (0-7): "))

board = knights_tour(sx, sy)

if board:
    print("\nKnight's Tour :\n")
    print("------------------------")
    print_board(board)
else:
    print("No solution found.")
