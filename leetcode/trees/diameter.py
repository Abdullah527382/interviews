# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return -1
            depth = max(dfs(root.left), dfs(root.right))
            return depth + 1 if root.left or root.right else 0
        return dfs(root.left) + dfs(root.right) + 2 
    # This passes 101/106 tests


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxVal = [0]
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)

            maxVal[0] = max(maxVal[0], left + right + 2)
            return 1 + max(left, right)
        dfs(root)
        return maxVal[0]