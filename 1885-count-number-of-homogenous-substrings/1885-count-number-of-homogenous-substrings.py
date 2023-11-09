class Solution(object):
    def countHomogenous(self, s):
        MOD = 10**9 + 7
        result = 0
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                result = (result + (count * (count + 1) // 2) % MOD) % MOD
                count = 1

        result = (result + (count * (count + 1) // 2) % MOD) % MOD

        return result