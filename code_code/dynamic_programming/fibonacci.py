#dynamic programming approach
def fib(n):
    arr = [0] * (n + 1)
    arr[1] = 1
    
    for i in range(2,n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]

print(fib(6))
