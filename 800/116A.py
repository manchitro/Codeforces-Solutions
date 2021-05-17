#Problem link: https://codeforces.com/contest/116/problem/A
#Status: Accepted
numStops = int(input())
array = []
for i in range(numStops):
    row = input().split(" ", 2)
    array.append(row)
maxPassenger = int(array[0][1])
currentPassenger = int(array[0][1])
for i in range(1, len(array)):
    currentPassenger = currentPassenger - int(array[i][0]) + int(array[i][1])
    if currentPassenger > maxPassenger:
        maxPassenger = currentPassenger
    # print(currentPassenger)
print(maxPassenger)
