#Problem link: https://codeforces.com/contest/734/problem/A
#Status: Accepted
n = int(input())
str = input()
acount = 0
dcount = 0
for i in range(n):
    if str[i] == "A":
        acount += 1
    elif str[i] == "D":
        dcount += 1
if acount > dcount:
    print("Anton")
elif acount < dcount:
    print("Danik")
else:
    print("Friendship")
