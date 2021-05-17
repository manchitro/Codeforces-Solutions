import itertools
import sys

n, m = map(int, input().split(" ", 2))
puzzles = list(map(int, input().split(" ", m)))
puzzles.sort()
print(puzzles)
maxDiff = puzzles[m - 1] - puzzles[0]
for i in (n, m):
    ans = puzzles[i - 1] - puzzles[i - n]
    print(puzzles[i - 1], "-", puzzles[i - n], "-", ans)
    if ans < maxDiff:
        maxDiff = ans
print(maxDiff)
