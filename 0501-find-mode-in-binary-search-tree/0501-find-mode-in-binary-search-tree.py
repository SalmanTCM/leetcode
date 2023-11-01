class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        self.prev = None
        self.max_freq = 0
        self.curr_freq = 0
        self.modes = []

        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)
                process_node(node.val)
                inorder_traversal(node.right)

        def process_node(val):
            if val == self.prev:
                self.curr_freq += 1
            else:
                self.curr_freq = 1

            if self.curr_freq > self.max_freq:
                self.max_freq = self.curr_freq
                self.modes = [val]
            elif self.curr_freq == self.max_freq:
                self.modes.append(val)

            self.prev = val

        inorder_traversal(root)

        return self.modes


