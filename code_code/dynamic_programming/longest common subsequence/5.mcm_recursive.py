# https://www.techiedelight.com/matrix-chain-multiplication/
import sys
import math
# Recursive implementation
# def MatrixChainOrder(p, i, j):
#     if i == j:
#         return 0

#     _min = sys.maxsize

#     for k in range(i, j):
#         temp_ans = (MatrixChainOrder(p, i, k)
#         + MatrixChainOrder(p, k + 1, j)
#         + p[i - 1] * p[k] * p[j])

#         if temp_ans < _min:
#             _min = temp_ans
#         # _min = min(_min, temp_ans)

#     return _min

# Recursive with memoization implementation, top down
# def MatrixChainOrder(p, i, j, dp):
#     if i == j:
#         return 0

#     if dp[i][j] != -1:
#         return dp[i][j]

#     _min = sys.maxsize

#     for k in range(i, j):
#         temp_ans = (MatrixChainOrder(p, i, k, dp)
#         + MatrixChainOrder(p, k + 1, j, dp)
#         + p[i - 1] * p[k] * p[j])

#         if temp_ans < _min:
#             _min = temp_ans
#         # _min = min(_min, temp_ans)

#     dp[i][j] = _min
#     return _min

#https://www.youtube.com/watch?v=pEYwLmGJcvs
def MatrixChainOrder(arr):
    N = len(arr) - 1
    dp = [[-1 for _ in range(N)] for _ in range(N)]

    for g in range(0, N):
        i = 0
        for j in range(g, N):
            if (g == 0):
                dp[i][j] = 0
            elif (g == 1):
                dp[i][j] = arr[i] * arr[j] * arr[j + 1]
            else:
                mini = sys.maxsize
                for k in range(i, j):
                    lc = dp[i][k]
                    rc = dp[k + 1][j]
                    mc = arr[i] * arr[k + 1] * arr[j + 1]
                    tc = lc + rc + mc
                    mini = min(mini, tc)
                dp[i][j] = mini
            i = i + 1
    return dp[0][N - 1]


# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 3]
    N = len(arr)
    # dp = [[-1 for _ in range(N)] for _ in range(N)]

    # Function call
    # print("Minimum number of multiplications is ",MatrixChainOrder(arr, 1, N-1))
    # print("Minimum number of multiplications is ",MatrixChainOrder(arr, 1, N-1, dp))
    print("Minimum number of multiplications is ", MatrixChainOrder(arr))
