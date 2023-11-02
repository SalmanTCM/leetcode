class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def calculateSubtreeAverage(node):
            if not node:
                return 0, 0 
            
            left_sum, left_count = calculateSubtreeAverage(node.left)
            right_sum, right_count = calculateSubtreeAverage(node.right)
            
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            
            return total_sum, total_count

        def isSubtreeAverageEqual(node):
            if not node:
                return False
            
            subtree_sum, subtree_count = calculateSubtreeAverage(node)
            average = subtree_sum // subtree_count
            
            return node.val == average

        def countNodesWithSubtreeAverage(node):
            if not node:
                return 0
            
            count = isSubtreeAverageEqual(node)
            left_count = countNodesWithSubtreeAverage(node.left)
            right_count = countNodesWithSubtreeAverage(node.right)
            
            return count + left_count + right_count

        return countNodesWithSubtreeAverage(root)