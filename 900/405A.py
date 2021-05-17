#Problem link: https://codeforces.com/contest/405/problem/A
#Status: Accepted
n = int(input())
columns = list(map(int, input().split(" ", n)))
tallestCol = 0
for i in range(n):
    if columns[i] > tallestCol:
        tallestCol = columns[i]
# now we have tallest column
# simulate the box
rows, cols = (tallestCol, n)
box = [[0 for i in range(cols)] for j in range(rows)]
# box[tallestCol-1][0] = 1
for i in range(0, n):
    for j in range(tallestCol - 1, tallestCol - 1 - columns[i], -1):
        box[j][i] = 1
# for each row
for i in range(tallestCol):
    # take number of cubes in that row
    nCubes = 0
    for j in range(n):
        if box[i][j] == 1:
            nCubes += 1
            box[i][j] = 0
    for k in range(n - 1, -1, -1):
        if nCubes != 0:
            box[i][k] = 1
            nCubes -= 1
# counting cubes in each column in new box
newCols = [0] * n
# for each column
for i in range(n):
    # for each row
    nCubesinCol = 0
    for j in range(tallestCol):
        if box[j][i] == 1:
            nCubesinCol += 1
    newCols[i] = nCubesinCol
print(*newCols)
