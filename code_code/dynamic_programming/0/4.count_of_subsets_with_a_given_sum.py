
def subset_sum(a: list, n: int, summ: int):
    rows = n + 1
    cols = summ + 1
    # dp = [[0 for _ in range(rows)] for _ in range(cols)]
    dp = [[0] * (cols) for i in range(rows)]
    dp[0][0] = 1
    for i in range(1, sum + 1):
        dp[0][i] = 0
    print(dp)
    for i in range(1, rows):
        for j in range(1, cols):
            if j < a[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - a[i - 1]]
    
    return dp[n][summ]

if __name__ == '__main__':
    a = [3, 3, 3, 3]
    n = 4
    sum = 6
    print(subset_sum(a, n, sum))