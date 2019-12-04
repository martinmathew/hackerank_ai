def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        return 'CLEAN'
    dirs = [(0,1,'RIGHT'),(0,-1,'LEFT'),(-1,0,'UP'),(1,0,'DOWN')]
    dirty_dir = None
    for dir in dirs:
        fposr = posr + dir[0]
        fposc = posc + dir[1]
        if fposr < 0 or fposr >= len(board) or fposc < 0 or fposc >= len(board[fposr]):
            continue
        if board[posr + dir[0]][posc + dir[1]] == 'd':
            dirty_dir = dir[2]
            break
    if dirty_dir is None:
        min_len = 999999999
        direction = None
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'd':
                    leng,path = displayPathtoPrincess((posr,posc),(i,j))
                    if leng < min_len:
                        min_len = leng
                        direction = path[0:path.index('\n')]
        return direction


    else:
        return dirty_dir



def displayPathtoPrincess(bot,dirt):

    diff_rows = bot[0] - dirt[0]
    diff_cols = bot[1] - dirt[1]
    return (abs(diff_rows)+abs(diff_cols),''.join(['DOWN\n' * abs(diff_rows) if diff_rows < 0 else 'UP\n' * diff_rows,
                    'RIGHT\n' * abs(diff_cols) if diff_cols < 0 else 'LEFT\n' * diff_cols]))

# Tail starts here
if __name__ == "__main__":
    pos =[int(i)
    for i in input().strip().split()]
    board =[[j for j in input().strip()] for i in range(5)]
    print(next_move(pos[0], pos[1], board))
