class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        
        dp = [0] * n
        max_sum_deque = []
        max_sum = nums[0]

        for i in range(n):
            if max_sum_deque and i - max_sum_deque[0] > k:
                max_sum_deque = max_sum_deque[1:]

            if max_sum_deque:
                dp[i] = max(dp[i], dp[max_sum_deque[0]] + nums[i])

            else:
                dp[i] = max(dp[i], nums[i])

            max_sum = max(max_sum, dp[i])
            while max_sum_deque and dp[i] >= dp[max_sum_deque[-1]]:
                max_sum_deque.pop()
                
            max_sum_deque.append(i)
        if max_sum == 0:
            max_sum = max(nums)

        return max_sum
