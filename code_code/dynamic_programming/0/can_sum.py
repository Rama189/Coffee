# Python3 implementation to count
# ways to sum up to a given value N

# Function to count the total
# number of ways to sum up to 'N'
# def countWays(arr, m, N):
#     dp = [[0 for _ in range(N + 1)] for _ in range(m + 1)]

#     for i in range(m + 1):
#         for j in range(N + 1):
#             if i == 0 or j == 0:
#                 dp[i][j] = 0
#             else:
#                 if arr[i - 1] <= j:
#                     dp[i][j] = dp[i][j - arr[i - 1]] + dp[i - 1][j]
#                 else:
#                     dp[i][j] = dp[i - 1][j]
#     return dp[m][N]

# Recursive
def canSum(arr, N):
    if N == 0:
        return True
    if N < 0:
        return False

    for i in range(len(arr)):
        target = N - arr[i] 
        if canSum(arr, target) == True:
            return True

    return False
	
# Driver Code
# arr = [2,3,5]
# arr = [1,3,5]
arr = [7, 14]
m = len(arr)
# N = 300 
N = 250
print("Can sum",
		canSum(arr, N))
			
# This code is contributed by Anant Agarwal.
