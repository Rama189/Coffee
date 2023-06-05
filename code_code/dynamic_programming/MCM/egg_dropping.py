
# https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/
# https://www.youtube.com/watch?v=UvksR0hR9nA
# https://leetcode.com/problems/super-egg-drop/discuss/159079/Python-DP-from-kn2-to-knlogn-to-kn
# check above link for optimisation on leetcode
import sys
# def eggDrop(n, k):
#     if n == 1:
#         return k
#     if k == 0 or k == 1:
#         return k

#     mn = sys.maxsize
#     for i in range(1, k + 1):
#         temp = 1 + max(eggDrop(n - 1, i - 1), eggDrop(n, k - i))
#         mn = min(temp, mn)
#     return mn

INT_MAX = 32767
def eggDrop(n, k, dp):
    for i in range(1, n + 1):
        dp[i][0] = 0
        dp[i][1] = 1

    for j in range(1, k + 1):
        dp[1][j] = j
    
    for i in range(2, n + 1):   
        for j in range(2, k + 1):
            # dp[i][j] = INT_MAX
            mn = INT_MAX
            for x in range(1, j + 1):
                v1 = dp[i - 1][x - 1]
                v2 = dp[i][j - x]
                res = max(v1, v2)

                mn = min(mn, res)
            dp[i][j] = mn + 1
        
                # res = 1 + max(dp[i - 1][x - 1], dp[i][j - x]) # You can write the samething like this also
                # if res < dp[i][j]:
                #     dp[i][j] = res
    return dp[n][k]

# Driver Code
if __name__ == "__main__":
 
    n = 2
    k = 10
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    print("Minimum number of trials in worst case with",
           n, "eggs and", k, "floors is", eggDrop(n, k, dp))