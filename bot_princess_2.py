def nextMove(n,r,c,grid):
    princess_crd = None
    for idx, row in enumerate(grid):
        if 'p' in row:
            princess_crd= (idx , row.rindex('p'))
            break

    leng,path = displayPathtoPrincess((r,c),princess_crd)
    direction = path[0:path.index('\n')]
    return direction


def displayPathtoPrincess(bot,dirt):

    diff_rows = bot[0] - dirt[0]
    diff_cols = bot[1] - dirt[1]
    return (abs(diff_rows)+abs(diff_cols),''.join(['DOWN\n' * abs(diff_rows) if diff_rows < 0 else 'UP\n' * diff_rows,
                    'RIGHT\n' * abs(diff_cols) if diff_cols < 0 else 'LEFT\n' * diff_cols]))



n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))