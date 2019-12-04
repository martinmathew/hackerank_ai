def displayPathtoPrincess(n,grid):
    princess_crd = None
    prince_crd = None
    for idx, row in enumerate(grid):
        if 'p' in row:
            princess_crd= (idx , row.rindex('p'))
        if 'm' in row:
            prince_crd = (idx, row.rindex('m'))


    if princess_crd is not None:
        diff_rows = prince_crd[0] - princess_crd[0]
        diff_cols = prince_crd[1] - princess_crd[1]

        return ''.join(['DOWN\n'*abs(diff_rows) if diff_rows < 0 else 'UP\n'*diff_rows, 'RIGHT\n'*abs(diff_cols) if diff_cols <0 else 'LEFT'*diff_cols])








m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

print(displayPathtoPrincess(m,grid))