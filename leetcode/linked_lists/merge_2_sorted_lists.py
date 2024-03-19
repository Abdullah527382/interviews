# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummyNode = ListNode()
        newHead = dummyNode
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:

            if curr1.val < curr2.val:
                temp = curr1
                dummyNode.next = temp
                curr1 = curr1.next
            else:
                temp = curr2
                dummyNode.next = temp
                curr2 = curr2.next

            dummyNode = dummyNode.next
        if curr1:
            dummyNode.next = curr1
        elif curr2:
            dummyNode.next = curr2
            
        return newHead.next