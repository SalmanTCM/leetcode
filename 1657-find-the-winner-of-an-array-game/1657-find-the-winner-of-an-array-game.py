class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        current_winner = arr[0]
        win_count = 0

        for i in range(1, len(arr)):
            if arr[i] > current_winner:
                current_winner = arr[i]
                win_count = 1
            else:
                win_count += 1

            if win_count == k:
                return current_winner

        return current_winner
