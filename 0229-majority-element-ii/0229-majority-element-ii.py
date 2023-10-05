from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        counts = Counter(nums)
        n = len(nums)
        threshold = n // 3
        
        result = [num for num, count in counts.items() if count > threshold]
        
        return result
