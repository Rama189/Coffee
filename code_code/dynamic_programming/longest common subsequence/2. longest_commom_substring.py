
# https://www.codingninjas.com/blog/2021/08/11/what-is-the-longest-common-substring/
# https://www.youtube.com/watch?v=AO1wlMJoxBk&t=1056s

#Bottom up approach dp
# def lcs(X , Y, n, m):
#     result = 0
#     for i in range(n + 1):
#         for j in range(m + 1):
#             if i == 0 or j == 0 :
#                 dp[i][j] = 0
#             elif X[i-1] == Y[j-1]:
#                 dp[i][j] = dp[i-1][j-1]+1
#                 result = max(result, dp[i][j])
#             else:
#                 dp[i][j] = 0

#     return result

#Recursive solution
# def lcs(X , Y, n, m, result):
#     if(n == 0 or m == 0):
#         return result
    
#     if(X[n - 1] == Y[m - 1]):
#         result = lcs(X , Y, n - 1, m - 1, result + 1)

#     result = max(result, max(lcs(X , Y, n - 1, m, 0), lcs(X , Y, n, m - 1, 0)))
#     return result

#Recursive solution with memoization, check this one later
def lcs(X , Y, n, m, result):
    if(n == 0 or m == 0):
        return result

    if dp[n][m] != -1:
        return dp[n][m]

    if(X[n - 1] == Y[m - 1]):
        dp[n][m] = lcs(X , Y, n - 1, m - 1, result + 1)
        # dp[n][m] = result
        return dp[n][m]

    dp[n][m] = max(lcs(X , Y, n - 1, m, 0), lcs(X , Y, n, m - 1, 0))
    return dp[n][m]
 

X = "AGGXTAAC"
# X = "ABCDE"
Y = "GGXXTXAYAC"
# Y = "ABFCE"
n = len(X) + 1
m = len(Y) + 1
result = 0
dp = [[-1 for _ in range(m)] for _ in range(n)]
print ("Length of Longest common substring is ", lcs(X , Y, n - 1, m - 1, result))