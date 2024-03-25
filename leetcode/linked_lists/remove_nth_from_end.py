# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # First get the length of the list
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        if length == n:
            return head.next
        curr = head
        count = 0
        while curr:
            count += 1
            if count == length - n:
                tmp = curr.next.next if curr.next else None
                curr.next = tmp
            curr = curr.next

        return head
        # Loop till we reach (length - n)
        # Remove the node  and return head