class Solution(object):
    def integerBreak(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0] * (n + 1)

        dp[2] = 2
        dp[3] = 3

        for i in range(4, n + 1):
            for j in range(2, i // 2 + 1):
                dp[i] = max(dp[i], dp[j] * dp[i - j])

        return dp[n]

