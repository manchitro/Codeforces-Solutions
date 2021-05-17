#Problem link: https://codeforces.com/contest/208/problem/A
#Status: Accepted
import re

song = input()
newsong = re.sub("WUB", " ", song)
print(*newsong.split())
