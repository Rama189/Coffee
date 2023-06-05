import sys
def minDifference(nums, n):
        total = sum(nums)
        rows = len(nums) + 1
        cols = total + 1
        valid = []
        mini = sys.maxsize
        
        dp = [[False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            dp[i][0] = True
        
        for i in range(1, rows):
            for j in range(1, cols):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
       
        for j in range(cols//2):
            if dp[rows - 1][j]:
                valid.append(j)
                s = total - (2 * j)
                mini = min(mini, s)
        
        return mini
if __name__ == '__main__':
 
    arr = [ 1, 6, 11, 5 ]
    n = len(arr)
    print("The Minimum difference of 2 sets is ", minDifference(arr, n))