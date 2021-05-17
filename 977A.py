n, k = input().split(" ", 2)
n = int(n)
k = int(k)
for i in range(k):
    if n % 10 == 0:
        n /= 10
    else:
        n -= 1
print(int(n))
