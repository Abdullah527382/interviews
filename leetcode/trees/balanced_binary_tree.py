class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
https://www.youtube.com/watch?v=QfJsau0ItOY&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&ab_channel=NeetCode

Complete this problem through recursion, a bottom up approach. Though
we could do a DFS search every single subtrees -> It would not be efficient. 

Given a tree, we will start from the right or left-most subtree and
return whether it is balanced and its height [T/F, 0..N]

The base case will return [T, 0]
We will call the function on the left and right nodes
We check if we get [F, ] on either subtrees but also check
if we get a height diff > 1 between left and right subtrees
In that case, the function will return False. In our recursive func
we return the height as 1 + the max(left, right) height 

Efficiency and Time complexity:
This algorithm will run in O(1) time since it visits each node atleast
once

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def dfs(root):
            if (root == None):
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)

            if not (left[0] and right[0] and abs(left[1] - right[1] <= 1)):
                return [False, 0]
            return [True, 1 + max(left[1], right[1])]
        return dfs(root)[0]

