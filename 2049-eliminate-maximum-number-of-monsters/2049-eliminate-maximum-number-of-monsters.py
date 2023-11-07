class Solution(object):
    def eliminateMaximum(self, dist, speed):
        n = len(dist)
        time_to_city = [(dist[i] + speed[i] - 1) // speed[i] for i in range(n)]
        time_to_city.sort()

        max_eliminated = 0

        for i in range(n):
            if time_to_city[i] <= i:
                break
            max_eliminated += 1

        return max_eliminated