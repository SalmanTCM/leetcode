class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        n = mountain_arr.length()
        peak_index = self.find_peak(mountain_arr, 0, n - 1)
        
        result = self.binary_search_increasing(mountain_arr, target, 0, peak_index)
        
        if result != -1:
            return result
        
        result = self.binary_search_decreasing(mountain_arr, target, peak_index, n - 1)
        
        return result
    
    def find_peak(self, mountain_arr, left, right):
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        return left
    
    def binary_search_increasing(self, mountain_arr, target, left, right):
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def binary_search_decreasing(self, mountain_arr, target, left, right):
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
