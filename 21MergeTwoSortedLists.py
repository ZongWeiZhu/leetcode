#-*- coding=utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
    	l1_node = l1
    	l2_node = l2
    	l3 = ListNode(-1)
    	l3_node = l3
    	while(l1_node and l2_node):
    		if(l1_node.val <= l2_node.val):
    			l3_node.next = l1_node
    			l1_node = l1_node.next
    			l3_node = l3_node.next

    		else:
    			l3_node.next = l2_node
    			l2_node = l2_node.next
    			l3_node = l3_node.next
    	if(l1_node):
    		l3_node.next = l1_node
    	if(l2_node):
    		l3_node.next = l2_node
    	return l3.next



idx = ListNode(1)
n = idx
n.next = ListNode(2)
n = n.next
n.next = ListNode(4)
n = n.next


idy = ListNode(1)
n = idy
n.next = ListNode(3)
n = n.next
n.next = ListNode(4)
n = n.next


s = Solution()
idz = s.mergeTwoLists(idx,idy)
while(idz):
	print idz.val
	idz = idz.next
