# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        root = preorder[0]
        newNode = TreeNode(root)
        mid = inorder.index(preorder[0])
        newNode.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        newNode.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return newNode