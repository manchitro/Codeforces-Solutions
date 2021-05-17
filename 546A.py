#Problem link: https://codeforces.com/contest/546/problem/A
#Status: Accepted
bananaCost, hasMoney, numBananaWant = input().split(" ", 3)
totalCost = 0

for i in range(1, int(numBananaWant) + 1):
    totalCost += i * int(bananaCost)
    # print(total)

needMoney = totalCost - int(hasMoney)
if needMoney < 0:
    print("0")
else:
    print(needMoney)
