n = int(input())
m = int(input())
k = int(input())
if (k % m == 0) and (k // m) <= n:
    print("YES")
elif (k % n == 0) and (k // n <= m):
    print("YES")
else:
    print("NO")