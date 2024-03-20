# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # preorder traversal
        def dfs(root, maxVal):
            if root == None:
                return 0
            goodNodes = 0
            if root.val >= maxVal:
                goodNodes = 1
            else:
                goodNodes = 0
            maxVal = max(maxVal, root.val)
            goodNodes += dfs(root.left, maxVal)
            goodNodes += dfs(root.right, maxVal)
            return goodNodes
        return dfs(root, root.val)
        