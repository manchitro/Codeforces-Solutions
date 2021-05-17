word = input()
upCount = 0
loCount = 0
for char in word:
    if str.isupper(char):
        upCount += 1
    elif str.islower(char):
        loCount += 1
if loCount < upCount:
    print(str.upper(word))
else:
    print(str.lower(word))
