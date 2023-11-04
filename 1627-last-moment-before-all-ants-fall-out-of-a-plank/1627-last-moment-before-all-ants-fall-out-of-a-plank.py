class Solution(object):
    def getLastMoment(self, n, left, right):
        left_times = [pos for pos in left]
        right_times = [n - pos for pos in right]

        max_time = max(left_times + right_times)

        return max_time
