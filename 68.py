# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #带头节点：用头插法；这里是不带头节点
        p =head
        h = ListNode(0)#建立头结点
        while p:
            q = p.next
            p.next = h.next
            h.next = p
            p = q
        return h.next
