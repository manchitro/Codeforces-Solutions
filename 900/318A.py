#Problem link: https://codeforces.com/contest/318/problem/A
#Status: Accepted
import math

n, k = list(map(int, input().split(" ", 2)))
# if n = 10
# 1 3 5 7 9|2 4 6 8 10

if n % 2 == 0:
    if k <= n / 2:
        # k is in the odd half
        # kth odd number is k*2-1. i.e. 2nd odd number 2*2-1=3, 3rd odd number 3*2-1=5
        print(k * 2 - 1)
    else:
        # k is in the even half
        # if we shift the list backwards by n/2, the list will start from even numbers
        # 1 3 5 7 9 2 4 6 8 10 (n=10) becomes 2 4 6 8 10 (n=5)
        # so (k - n/2) will give us the position of the even number we're looking for as the (k - n/2)th even number
        # i.e. if k=7 then we want the 7th number in our list which is 4. (k- n/2) = 7-5 = 2, 4 is indeed the 2nd even number
        # i.e. if k=9 then we want the 9th number in our list which is 8. (k- n/2) = 9-5 = 4, 8 is indeed the 4th even number
        # i.e. if k=6 then we want the 6th number in our list which is 2. (k- n/2) = 6-5 = 1, 2 is indeed the 1st even number
        pos = k - (n / 2)
        print(int(pos * 2))
else:
    # if n is odd, there will be 1 more odd number than even numbers
    # to know if k is in the odd half, we need to take ceiling of n/2, that will include the last odd number
    if k <= math.ceil(n / 2):
        # k is in the odd half, same formula as before
        print(k * 2 - 1)
    else:
        # k is in thek even half
        # if we shift the list backwards by math.ceil(n/2), the list will start from even numbers
        # 1 3 5 7 9 2 4 6 8 (n=9) becomes 2 4 6 8 (n=4) because math.ceil(9/2) = 4
        # so (k - math.ceil(n/2)) will give us the position of the even number we're looking for as the (k - math.ceil(n/2))th even number
        pos = k - math.ceil(n / 2)
        print(pos * 2)
