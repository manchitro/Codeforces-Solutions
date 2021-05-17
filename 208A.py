import re

song = input()
newsong = re.sub("WUB", " ", song)
print(*newsong.split())
