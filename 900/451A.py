# Problem link: https://codeforces.com/contest/451/problem/A
# Status: Accepted 
n, m = map(int, input().split(" ", 2))
intersections = n * m
winner = "Malvika"
while intersections > 0:
    intersections = intersections - n - m + 1
    n -= 1
    m -= 1
    # print(intersections)
    if winner == "Akshat":
        winner = "Malvika"
    else:
        winner = "Akshat"
print(winner)
