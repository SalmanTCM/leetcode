class Solution(object):
    def maximumScore(self, nums, k):
        n = len(nums)
        max_score = nums[k]
        left, right = k, k

        while left > 0 or right < n - 1:
            height = min(nums[left], nums[right])

            while left > 0 and nums[left - 1] >= height:
                left -= 1
            while right < n - 1 and nums[right + 1] >= height:
                right += 1

            max_score = max(max_score, height * (right - left + 1))

            if left == 0:
                right += 1
            elif right == n - 1:
                left -= 1
            elif nums[left - 1] > nums[right + 1]:
                left -= 1
            else:
                right += 1

        return max_score

