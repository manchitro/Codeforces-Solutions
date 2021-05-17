# Problem link: https://codeforces.com/contest/1343/problem/A
# Status: Accepted
t = int(input())
for i in range(t):
    n = int(input())
    k = 2
    while True:
        x = n / ((2 ** k) - 1)
        if x % 1 == 0 and x != n:
            print(int(x))
            break
        k += 1
