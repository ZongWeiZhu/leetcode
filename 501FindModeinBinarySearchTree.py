#-*- coding=utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        myStack = []
        node = root
        d = {}
        while node or myStack:
            while node:                    
                if node.val not in d:
                	d[node.val] = 1
                else:
                	d[node.val] = d[node.val] +1
                myStack.append(node)
                node = node.left
            node = myStack.pop()            
            node = node.right                 
        r = []

        max_d = d[sorted(d,key=lambda x:d[x])[-1]]
        for key,value in d.items():
        	if value == max_d:
        		print key
        		r.append(key)
        return r

t = TreeNode(2147483647)


solution = Solution()
r = solution.findMode(t)
print r
