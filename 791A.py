a, b = input().split(" ", 2)
a = int(a)
b = int(b)
year = 0
while True:
    if a <= b:
        a *= 3
        b *= 2
        year += 1
        # print('a: ' + a + 'b: ' + b + ' year: ' + year)
    else:
        print(year)
        break
