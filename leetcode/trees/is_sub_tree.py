# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        # If theres no root tree, then the sub wont be a subtree
        if not root:
            return False
        # If theres no sub, then it is null which is a subtreee
        if not subRoot:
            return True
        if self.isTreeEqual(root, subRoot):
            return True
        isLeftTree = (self.isSubtree(root.left, subRoot))
        isRightTree = (self.isSubtree(root.right, subRoot))
        # Either in the left or right subtrees might contain our subroot
        return isLeftTree or isRightTree

    # Helper function to compare subtree from root to subRoot tree
    def isTreeEqual(self, subtree, subroot):
        if not subtree and not subroot:
            return True
        if (subtree and not subroot) or (subroot and not subtree) or (subtree.val != subroot.val):
            return False
        return self.isTreeEqual(subtree.left, subroot.left) and self.isTreeEqual(subtree.right, subroot.right)