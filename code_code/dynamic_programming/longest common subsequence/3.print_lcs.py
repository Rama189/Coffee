#Bottom up approach dp
def lcs(X , Y, n, m):
    res = ""
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0 :
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

    #code for printing the lcs string (Longest common subsequence)
    i = n
    j = m
    while(i > 0 and j > 0):
        if(X[i-1] == Y[j-1]):
            res = res + X[i-1]
            i -= 1
            j -= 1
        else:
            if(dp[i][j - 1] > dp[i - 1][j]):
                j -= 1
            else:
                i -= 1
    return res[::-1]

X = "AGGTAB"
Y = "GXTXAYB"
n = len(X) + 1
m = len(Y) + 1
dp = [[-1 for _ in range(m)] for _ in range(n)]
print ("Length of LCS is ", lcs(X , Y, n - 1, m - 1))