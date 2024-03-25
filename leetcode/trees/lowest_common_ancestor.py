# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class MySolution(object):
    # 16/30 tests pass, it has all the ancestor nodes but doesnt know which one is the lowest. This is recursive
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = []
        def dfs(root, p, q, stack):
            if root == None or (p in stack and q in stack):
                return
            if root == p:
                stack.append(p)
            if root == q:
                stack.append(q)
            if not stack:
                stack.append(root)
            dfs(root.left, p, q, stack)
            dfs(root.right, p, q, stack)
            # The last 2 are p, q so if there are > 2 nodes then we take min(stack:2)
            stack_arr = [x.val for x in stack[:len(stack)-2]] 
            print(stack_arr)
            return stack[stack_arr.index(min(stack_arr))] if len(stack) > 2 else stack[0]
        return dfs(root,p,q,stack)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        cur = root
        while cur:
            # Since this is a proper ordered BST, we use .val to change direction of tree
            if cur.val < p.val and cur.val < q.val:
                # Move to the right part of the tree
                cur = cur.right
            elif cur.val > p.val and cur.val > q.val:
                # Move to the left part of the tree
                cur = cur.left
            else:
                # Some cases include cur.val = p.val, cur.val = q.val, 
                return cur