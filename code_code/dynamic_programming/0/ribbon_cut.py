
def maximumSegments(n, a, b, c):
    dp = [[0 for _ in range(n+1)] for _ in range(4)]
    w = [a, b, c]

    for i in range(1, 4):
        for j in range(1, n + 1):
            if(w[i - 1] <= j):

                if j - w[i - 1] != 0 and dp[i][j - w[i - 1]] == 0:
                    val_1 = 0
                else:
                    val_1 = 1 + dp[i][j - w[i - 1]]
                dp[i][j] = max(val_1, dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[3][n]

# Driver code
n = 16
a = 7
b = 5
c = 3
print (maximumSegments(n, a,b, c))