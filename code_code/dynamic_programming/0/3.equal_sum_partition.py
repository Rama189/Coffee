# def isSubsetSum(arr, n, sum):
#     if sum == 0:
#         return True
#     if n == 0 and sum != 0:
#         return False
    
#     return isSubsetSum(arr, n - 1, sum) or isSubsetSum(arr, n - 1, sum - arr[n - 1])

def isSubsetSum(arr, n, sum, dp):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    
    if (dp[n][sum] != -1):
        return dp[n][sum]
    
    dp[n][sum] = isSubsetSum(arr, n - 1, sum, dp) or isSubsetSum(arr, n - 1, sum - arr[n - 1], dp)
    return dp[n][sum]

#Based on tushar roys solution
#https://github.com/mission-peace/interview/blob/master/python/dynamic/subset_sum.py
def findPartion(arr, n):
    sum_value = sum(arr)
    i, j = 0, 0
 
    if sum_value % 2 != 0:
        return False
    
    rows = len(arr) + 1
    cols = sum_value + 1    
    dp = [[False for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        dp[i][0] = True
    
    for i in range(1, rows):
        for j in range(1, cols):
            if j >= arr[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[rows - 1][cols - 1]


def findPartion(arr, n):
    sum = 0
    for i in range(n):
        sum += arr[i]
    
    if sum % 2 != 0:
        return False
    
    # To store overlapping subproblems
    dp = [[-1]*(sum+1)]*(n+1)
    
    return isSubsetSum(arr, n, sum // 2, dp)


# Driver code
arr = [3, 1, 5, 9, 12]
n = len(arr)
 
# Function call
if findPartion(arr, n) == True:
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")