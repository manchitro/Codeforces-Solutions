n = int(input())
array = list(map(int, input().split(" ", n)))
lengths = []
length = 1
for i in range(n - 1):
    if array[i] <= array[i + 1]:
        length += 1
    else:
        lengths.append(length)
        length = 1
    if i == n - 2:
        lengths.append(length)
    # print('length:', length)
    # print('lengths:', lengths)

maxlength = 1
for i in range(len(lengths)):
    if lengths[i] > maxlength:
        maxlength = lengths[i]
print(maxlength)
