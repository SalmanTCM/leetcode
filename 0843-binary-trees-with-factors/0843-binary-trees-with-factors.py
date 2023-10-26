class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        
        for num in arr:
            dp[num] = 1 

            for factor in arr:
                if factor >= num:
                    break  
                    
                if num % factor == 0:
                    complement = num // factor

                    if complement in dp:
                        dp[num] += dp[factor] * dp[complement]

            dp[num] %= MOD

        # Calculate the total number of binary trees that can be formed
        total = 0
        for num in dp:
            total += dp[num]
            total %= MOD

        return total