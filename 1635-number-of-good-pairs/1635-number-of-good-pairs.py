class Solution(object):
    def numIdenticalPairs(self, nums):
        num_count = {}
        identical_pairs = 0
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                identical_pairs += num_count[num]
                num_count[num] += 1

        return identical_pairs