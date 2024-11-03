
def fib_rabbits(n, k):
    
    F = [0]*(n+1)
    F[1] = 1
    
    if n > 1:
        F[2]= 1

    for month in range(3, n+1):
        F[month] = F[month - 1] + k * F[month - 2]

    
    return F[n]

n, k = map(int, input().split())
result = fib_rabbits(n, k)
print(result)
    