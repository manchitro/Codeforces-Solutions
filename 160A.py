n = int(input())
coins = list(map(int, input().split()))
mine = 0
nmine = 0
total = sum(coins)
while mine <= total - mine:
    biggestCoin = coins[0]
    takenIndex = 0
    for i in range(len(coins)):
        if coins[i] > biggestCoin:
            biggestCoin = coins[i]
            takenIndex = i
    mine += biggestCoin
    nmine += 1
    coins.pop(takenIndex)
print(nmine)
