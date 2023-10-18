from collections import defaultdict, deque

class Solution(object):
    def minimumTime(self, n, relations, time):
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        for prev, next_course in relations:
            graph[prev].append(next_course)
            in_degree[next_course] += 1

        course_time = [0] + time

        queue = deque()
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                queue.append(i)

        total_time = 0

        while queue:
            course = queue.popleft()
            total_time = max(total_time, course_time[course])

            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
                course_time[next_course] = max(course_time[next_course], course_time[course] + time[next_course - 1])

        return total_time
