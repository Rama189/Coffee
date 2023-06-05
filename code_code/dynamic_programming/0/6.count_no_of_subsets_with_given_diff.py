def count_subsets(arr, t):
    n = len(arr)
    rows = n + 1
    cols = t + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        dp[i][0] = 1
    print(dp)

    for i in range(1, rows):
        for j in range(1, cols):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]
                
    print(dp)
    return dp[n][t]

if __name__ == '__main__':
    arr = [1, 2, 3, 1, 2]
    N = 5
    diff = 1
    s = sum(arr)
    
    t = int((diff + s) / 2)
    print(t)
    print("The no of subsets with diff is ", count_subsets(arr, t))