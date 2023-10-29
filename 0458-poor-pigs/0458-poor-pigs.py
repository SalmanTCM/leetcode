class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        tests_per_pig = minutesToTest // minutesToDie + 1
        pigs = 0
        while tests_per_pig ** pigs < buckets:
            pigs += 1
        return pigs
