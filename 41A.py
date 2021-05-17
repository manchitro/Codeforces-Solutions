#Problem link: https://codeforces.com/contest/41/problem/A
#Status: Accepted
s = input()
t = input()
t2 = s[::-1]
if t == t2:
    print("YES")
else:
    print("NO")
