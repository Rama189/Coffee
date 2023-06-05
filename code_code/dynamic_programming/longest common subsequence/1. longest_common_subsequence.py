#recursive case
def lcs(X , Y, n, m):
    if(n == 0 or m == 0):
        return 0
    
    if(X[n - 1] == Y[m - 1]):
        return 1 + lcs(X , Y, n - 1, m - 1)
    else:
        return max(lcs(X , Y, n, m - 1), lcs(X , Y, n - 1, m))

# recursive case with memoization
# def lcs(X , Y, n, m):
#     if(n == 0 or m == 0):
#         return 0
#     if dp[n][m] != -1:
#         return dp[n][m]
#     if(X[n - 1] == Y[m - 1]):
#         dp[n][m] = 1 + lcs(X , Y, n - 1, m - 1)
#         return dp[n][m]
#     else:
#         dp[n][m] = max(lcs(X , Y, n, m - 1), lcs(X , Y, n - 1, m))
#         return dp[n][m]

#Bottom up approach dp
# def lcs(X , Y, n, m):
#     for i in range(n + 1):
#         for j in range(m + 1):
#             if i == 0 or j == 0 :
#                 dp[i][j] = 0
#             elif X[i-1] == Y[j-1]:
#                 dp[i][j] = dp[i-1][j-1]+1
#             else:
#                 dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

#     return dp[n][m]

X = "AGGTAB"
Y = "GXTXAYB"
n = len(X) + 1
m = len(Y) + 1
dp = [[-1 for _ in range(m)] for _ in range(n)]
print ("Length of LCS is ", lcs(X , Y, n - 1, m - 1))