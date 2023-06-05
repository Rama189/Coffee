import sys
#Naive recursive
def isPalindrome(s):
    return s == s[::-1]


# def minPalPartion(s, i,j):
#     if i >= j:
#         return 0
    
#     if isPalindrome(s[i:j+1]):
#         return 0

#     mini = float('inf')
#     for k in range(i, j):
#         temp = minPalPartion(s, i,k) + minPalPartion(s, k + 1,j) + 1
#         mini = min(mini, temp)
#     return mini

def minPalPartion(s, i,j, dp):
    if i >= j:
        return 0
    
    if isPalindrome(s[i:j+1]):
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
        
    mini = float('inf')
    for k in range(i, j):
        temp = minPalPartion(s, i,k, dp) + minPalPartion(s, k + 1,j, dp) + 1
        mini = min(mini, temp)

    dp[i][j] = mini
    return dp[i][j]


def main():
    string = "ababbbabbababa"
    j = len(string) - 1
    dp = [[-1 for _ in range(j + 1)] for _ in range(j + 1)]
    print("Min cuts needed for Palindrome Partitioning is ", minPalPartion(string, 0, j, dp),
    )
 
if __name__ == "__main__":
    main()
 