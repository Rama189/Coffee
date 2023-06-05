
def isSubsetSum(set, n, sum):
    if sum == 0:
        return True
    if n == 0:
        return False

    if set[n - 1] <= sum:
        return isSubsetSum(set, n - 1, sum - set[n - 1]) or isSubsetSum(set, n - 1, sum)
    else:
        return isSubsetSum(set, n - 1, sum)

#Recursive solution + memoization solution below.
def isSubsetSum(set, n, sum):
    if sum == 0:
        return True
    if n == 0:
        return False

    # If the value is not -1 it means it already call the function 
    # with the same value. it will save our from the repetition.    
    if dp[n][sum] != -1:
        return dp[n - 1][sum]
    
    # Here we do two calls because we don't know which value is 
    # full-fill our criteria that's why we doing two calls
    if set[n - 1] <= sum:
        dp[n - 1][sum] = isSubsetSum(set, n - 1, sum - set[n - 1]) or isSubsetSum(set, n - 1, sum)
        return dp[n-1][sum]
    else:
        # if the value of a[n-1] is greater than the sum.
        # we call for the next value
        dp[n - 1][sum] = isSubsetSum(set, n - 1, sum)
        return dp[n - 1][sum]
    
def isSubsetSum(set, n, sum):
    # The value of subset[i][j] will be 
    # true if there is a
    # subset of set[0..j-1] with sum equal to i
    subset =([[False for i in range(sum + 1)] 
            for i in range(n + 1)])
      
    # If sum is 0, then answer is true 
    for i in range(n + 1):
        subset[i][0] = True
          
    # If sum is not 0 and set is empty, 
    # then answer is false 
    for i in range(1, sum + 1):
         subset[0][i]= False
              
    # Fill the subset table in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j<set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j>= set[i-1]:
                subset[i][j] = (subset[i-1][j] or 
                                subset[i - 1][j-set[i-1]])
     # uncomment this code to print table 
    # for i in range(n + 1):
    # for j in range(sum + 1):
    # print (subset[i][j], end =" ")
    # print()
    return subset[n][sum]
# Driver code
set = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(set)
dp = [[-1 for x in range(sum + 1)] for y in range(n + 1)] #For recursive + memoization matrix, initialize to -1
# dp = [[]]
# print(dp)
if (isSubsetSum(set, n, sum) == True):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")