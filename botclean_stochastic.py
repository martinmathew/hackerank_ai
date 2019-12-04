def nextMove(posr, posc, board):

    dirt_cord = None
    for idx, row in enumerate(board):
        if 'd' in row:
            dirt_cord = (idx , row.index('d'))
    if (posr,posc) == dirt_cord:
        return 'CLEAN'
    leng,path = displayPathtoPrincess((posr,posc),dirt_cord)
    if len(path) == 0:
        return ""
    direction = path[0:path.index('\n')]
    return direction



def displayPathtoPrincess(bot,dirt):
    diff_rows = bot[0] - dirt[0]
    diff_cols = bot[1] - dirt[1]
    return (abs(diff_rows)+abs(diff_cols),''.join(['DOWN\n' * abs(diff_rows) if diff_rows < 0 else 'UP\n' * diff_rows,
                    'RIGHT\n' * abs(diff_cols) if diff_cols < 0 else 'LEFT\n' * diff_cols]))

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(nextMove(pos[0], pos[1], board))