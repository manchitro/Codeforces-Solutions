#Problem link: https://codeforces.com/contest/266/problem/B
#Status: Accepted
n, t = input().split(" ", 2)
n = int(n)
t = int(t)
queue = list(input())
i = 0
j = 0
while i < t:
    j = 0
    while j < len(queue) - 1:
        if queue[j] == "B" and queue[j + 1] == "G":
            queue[j] = "G"
            queue[j + 1] = "B"
            j += 1
        j += 1
    i += 1
print("".join(queue))
