class Solution(object):
    def buildArray(self, target, n):
        result = []
        stack = []

        for i in range(1, n + 1):
            if not target:
                break

            if i == target[0]:
                result.append("Push")
                target.pop(0)
            else:
                result.append("Push")
                result.append("Pop")

        return result
