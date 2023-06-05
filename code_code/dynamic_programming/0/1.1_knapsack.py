# A naive recursive implementation
# of 0-1 Knapsack Problem
 
# Returns the maximum value that
# can be put in a knapsack of
# capacity W

# The time complexity of this naive recursive solution is exponential (2^n)
def knapSack(W, wt, val, n):
 
    # Base Case
    if n == 0 or W == 0:
        return 0
 
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))
 
# end of function knapSack

#Recursive + Memoization (equivalent to DP except recursive stack space)
def knapSack(W, wt, val, n):
    if W == 0 or n == 0:
        return 0

    if t[n][W] != -1:
        return t[n][W]
    
    if wt[n - 1] <= W:
        t[n][W] = max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1), 
                    knapSack(W, wt, val, n - 1)) 
        return t[n][W]
    else:
        t[n][W]= knapSack(W, wt, val, n - 1)
        return t[n][W]

#Bottom up approach (Actual dp kind)
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] #Turn your recursive base condition to initialization.

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif wt[i-1] <= j:
                K[i][j] = max(val[i-1]
                          + K[i-1][j-wt[i-1]], 
                              K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
    return K[n][W]

# val = [60, 100, 120]
val = [100, 120, 60]
wt = [20, 30, 10]
W = 50
n = len(val)

# We initialize the matrix with -1 at first.
t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
print(knapSack(W, wt, val, n))