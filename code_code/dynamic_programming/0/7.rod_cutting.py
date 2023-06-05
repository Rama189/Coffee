def un_kp(price, length, n, Max_len):
    rows = n + 1
    cols = n + 1
    dp = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(1, rows):
        for j in range(1, cols):
            if length[i - 1] <= j:
                # dp[i][j] = max(price[i - 1] + dp[i][j - length[i - 1]], dp[i - 1][j]) #My initial code thuss
                dp[i][j] = max(price[i - 1] + dp[i][j - i], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][n]

if __name__ == '__main__':
 
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    n =len(price)
    length = [0]*n
    print(length)
    for i in range(n):
        length[i] = i + 1
     
    Max_len = n
    print("Maximum obtained value is " ,un_kp(price, length, n, Max_len))