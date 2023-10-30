class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def count_ones(num):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count

        arr.sort(key=lambda x: (count_ones(x), x))
        return arr
