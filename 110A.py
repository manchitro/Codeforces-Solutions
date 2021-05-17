#Problem link: https://codeforces.com/contest/110/problem/A
#Status: Accepted
n = input()
fourCount = 0
seventCount = 0
for i in range(len(n)):
    if n[i] == "4":
        fourCount += 1
    elif n[i] == "7":
        seventCount += 1
luckyCount = fourCount + seventCount
if luckyCount == 4 or luckyCount == 7:
    print("YES")
else:
    print("NO")
