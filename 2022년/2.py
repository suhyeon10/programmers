def solution(n):
    dp = [0 for i in range(n)]
    dp[0], dp[1] = 1,2
    for i in range(2,n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    print(dp[n-1])
    return dp[n-1]

solution(5)