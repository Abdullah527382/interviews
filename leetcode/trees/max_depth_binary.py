# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, depth):
            if root == None:
                return 0
            depth = max(dfs(root.left, depth + 1),dfs(root.right, depth + 1))
            return depth + 1
        return dfs(root, 0)