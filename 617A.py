#Problem link: https://codeforces.com/contest/617/problem/A
#Status: Accepted
n = int(input())
steps = 0
while n != 0:
    if n >= 5:
        n -= 5
        steps += 1
        continue
    if n >= 4:
        n -= 4
        steps += 1
        continue
    if n >= 3:
        n -= 3
        steps += 1
        continue
    if n >= 2:
        n -= 2
        steps += 1
        continue
    if n >= 1:
        n -= 1
        steps += 1
        continue
print(steps)
