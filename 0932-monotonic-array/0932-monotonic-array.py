class Solution(object):
    def isMonotonic(self, nums):
        increasing = decreasing = True
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                increasing = False
                break
  
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
                break
  
        return increasing or decreasing