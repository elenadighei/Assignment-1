n = int(input())

def Fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
       s = Fibo(n- 1) + Fibo(n- 2)
       return s
    
result = Fibo(n)
print(result)
    

