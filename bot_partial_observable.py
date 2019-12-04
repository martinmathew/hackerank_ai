
def displayPathtoPrincess(bot,dirt):

    diff_rows = bot[0] - dirt[0]
    diff_cols = bot[1] - dirt[1]
    return (abs(diff_rows)+abs(diff_cols),''.join(['DOWN\n' * abs(diff_rows) if diff_rows < 0 else 'UP\n' * diff_rows,
                    'RIGHT\n' * abs(diff_cols) if diff_cols < 0 else 'LEFT\n' * diff_cols]))
def next_move(posx, posy, board):
    if board[posx][posy] == 'd':
        return 'CLEAN'
    min_len = 999999999
    direction = None
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0),(1,-1),(-1,1),(1,1),(-1,-1)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'd':
                leng, path = displayPathtoPrincess((posx, posy), (i, j))
                if leng < min_len:
                    min_len = leng
                    direction = path[0:path.index('\n')]
    return direction

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)