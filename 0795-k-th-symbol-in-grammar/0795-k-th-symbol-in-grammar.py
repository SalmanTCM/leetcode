class Solution(object):
    def kthGrammar(self, n, k):
        if n == 1:
            return 0
        mid = 2 ** (n - 2)
        if k <= mid:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - mid)
