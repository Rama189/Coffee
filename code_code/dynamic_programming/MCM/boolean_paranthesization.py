#Recursive
# def countParenth(statement, i, j, iSue):
#     if i > j:
#         return 0
    
#     if i == j:
#         if (iSue == 1) :
#             return 1 if statement[i] == 'T' else 0
#         else :
#             return 1 if statement[i] == 'F' else 0
#     temp_ans = 0
#     for k in range(i+1, j, 2):
#         lt = countParenth(statement, i, k - 1, True)
#         lf = countParenth(statement, i, k - 1, False)
#         rt = countParenth(statement, k + 1, j, True)
#         rf = countParenth(statement, k + 1, j, False)

#         if statement[k] == "|":
#             if (iSue == 1) :
#                 temp_ans += lt * rt + lt * rf + lf * rt
#             else :
#                 temp_ans += lf *  rf
#         elif statement[k] == "&":
#             if (iSue == 1) :
#                 temp_ans += lt * rt
#             else :
#                 temp_ans += lt *  rf + lf * rt + lf * rf
#         else:
#             if (iSue == 1) :
#                 temp_ans += lt *  rf + lf * rt 
#             else :
#                 temp_ans += lt *  rt + lf * rf
        
#     return temp_ans


#Top down(memoization)
def countParenth(statement, i, j, iSue, dp):
    if i > j:
        return 0
    
    if dp[i][j][iSue] != -1:
        return dp[i][j][iSue]
    
    if i == j:
        if (iSue == 1) :
            return 1 if statement[i] == 'T' else 0
        else :
            return 1 if statement[i] == 'F' else 0
    temp_ans = 0
    for k in range(i+1, j, 2):
        if (dp[i][k - 1][1] != -1) :
            lt = dp[i][k - 1][1]
        else :
            # Count number of True in left Partition
            lt = countParenth(statement, i, k - 1, 1, dp)
            
        if (dp[i][k - 1][0] != -1) :
            lf = dp[i][k - 1][0]
        else :
            # Count number of False in left Partition
            lf = countParenth(statement, i, k - 1, 0, dp)
        
        if (dp[k + 1][j][1] != -1) :
            rt = dp[k + 1][j][1]
        else :
            # Count number of True in right Partition
            rt = countParenth(statement, k + 1, j, 1, dp)
        
        if (dp[k + 1][j][0] != -1) :
            rf = dp[k + 1][j][0]
        else :
            # Count number of False in right Partition
            rf = countParenth(statement, k + 1, j, 0, dp)

        if statement[k] == "|":
            if (iSue == 1) :
                temp_ans += lt * rt + lt * rf + lf * rt
            else :
                temp_ans += lf *  rf
        elif statement[k] == "&":
            if (iSue == 1) :
                temp_ans += lt * rt
            else :
                temp_ans += lt *  rf + lf * rt + lf * rf
        else:
            if (iSue == 1) :
                temp_ans += lt *  rf + lf * rt 
            else :
                temp_ans += lt *  rt + lf * rf
        dp[i][j][iSue] = temp_ans
    return temp_ans


# Driver Code
# symbols = "TTFT"
# operators = "|&^"
statement = "T|F&T^F"
n = len(statement)
j = n - 1
 
# There are 4 ways
# ((T|T)&(F^T)), (T|(T&(F^T))),
# (((T|T)&F)^T) and (T|((T&F)^T))
dp = [[[-1 for k in range(2)] for i in range(n + 1)] for j in range(n + 1)]
# print(countParenth(statement, 0, j, True))
print(countParenth(statement, 0, j, True, dp))