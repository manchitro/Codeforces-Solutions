#Problem link: https://codeforces.com/contest/337/problem/A
#Status: Accepted
n, m = map(int, input().split(" ", 2))
puzzles = list(map(int, input().split(" ", m)))
puzzles.sort()
# print(puzzles)
maxDiff = puzzles[n - 1] - puzzles[0]
for i in range(m-n+1):
    # print(i)
    currentMin = puzzles[i + n - 1] - puzzles[i]
    if currentMin < maxDiff:
        maxDiff = currentMin
print(maxDiff)
