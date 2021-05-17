# Problem link: https://codeforces.com/contest/313/problem/A
# Status: Accepted
text = input()
balance = int(text)
if balance < 0:
    choice1 = int(text[0 : len(text) - 1 :])
    choice2 = int(text[0 : len(text) - 2 :] + text[len(text) - 1])
    # print(choice1, choice2)
    if choice1 > choice2:
        print(choice1) 
    else:
        print(choice2)
else:
    print(text)
