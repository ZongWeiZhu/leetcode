# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):

        self.head = head

    def getRandom(self):

        import random
        res = -1
        len = 0
        head = self.head
        while head:
            if random.randint(0,len) == 0:
                res = head.val
            head = head.next
            len += 1
        return res
        


# Your Solution object will be instantiated and called as such:
head = ListNode(1);
head.next = ListNode(2);
head.next.next = ListNode(3);
obj = Solution(head)
param_1 = obj.getRandom()
print param_1
