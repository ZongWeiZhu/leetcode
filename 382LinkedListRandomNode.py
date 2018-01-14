def __init__(self, head):
    """
    @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
    :type head: ListNode
    """
    self.head = head

def getRandom(self):
    """
    Returns a random node's value.
    :rtype: int
    """
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