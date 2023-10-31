class Solution(object):
    def findArray(self, pref):
        n = len(pref)
        arr = [0] * n

        for i in range(n):
            if i == 0:
                arr[i] = pref[i]
            else:
                arr[i] = pref[i] ^ pref[i - 1]

        return arr
