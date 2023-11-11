import heapq

class Graph(object):

    def __init__(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        """
        self.n = n
        self.graph = {}
        
        for edge in edges:
            from_node, to_node, cost = edge
            if from_node not in self.graph:
                self.graph[from_node] = []
            self.graph[from_node].append((to_node, cost))

    def addEdge(self, edge):
        """
        :type edge: List[int]
        :rtype: None
        """
        from_node, to_node, cost = edge
        if from_node not in self.graph:
            self.graph[from_node] = []
        self.graph[from_node].append((to_node, cost))

    def shortestPath(self, node1, node2):
        """
        :type node1: int
        :type node2: int
        :rtype: int
        """
        min_heap = [(0, node1)] 
        distances = {node1: 0}

        while min_heap:
            current_cost, current_node = heapq.heappop(min_heap)

            if current_node == node2:
                return current_cost

            if current_node in self.graph:
                for neighbor, edge_cost in self.graph[current_node]:
                    new_cost = current_cost + edge_cost
                    if neighbor not in distances or new_cost < distances[neighbor]:
                        distances[neighbor] = new_cost
                        heapq.heappush(min_heap, (new_cost, neighbor))

        return -1  
