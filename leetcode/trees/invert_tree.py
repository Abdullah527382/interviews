# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        head = root
        def dfs(root):
            if root == None:
                return
            temp = root.left 
            root.left = root.right
            root.right = temp
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return head