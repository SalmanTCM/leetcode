class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        MOD = 10**9 + 7
        maxPos = min(arrLen, steps // 2 + 1)
        dp = [[0] * maxPos for _ in range(steps + 1)]

        dp[0][0] = 1

        for i in range(1, steps + 1):
            for j in range(maxPos):
                dp[i][j] = dp[i - 1][j]  

                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1]  

                if j < maxPos - 1:
                    dp[i][j] += dp[i - 1][j + 1]

                dp[i][j] %= MOD

        return dp[steps][0]


