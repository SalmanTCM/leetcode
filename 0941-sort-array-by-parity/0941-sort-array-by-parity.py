class Solution(object):
    def sortArrayByParity(self, nums):
        even_nums = [x for x in nums if x % 2 == 0]
        odd_nums = [x for x in nums if x % 2 != 0]
        sorted_nums = even_nums + odd_nums

        return sorted_nums
