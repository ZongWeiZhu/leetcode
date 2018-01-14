#-*- coding=utf-8 -*-

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        max_k = []
        pre = 0
        if(k == len(num)):
            return "0"
        for i in range(0,k):
        	for j in range(len(num)):
        		if (j == len(num)-1 or num[j] > num[j+1]):
        			num = num[0:j]+num[j+1:]
        			break
        	print num


        while (num[0] == '0'):
            if len(num) == 1:
                return num
            num = num[1:]            
        return num
        


num = "1432219"
k = 3
solution = Solution()
r = solution.removeKdigits(num,k)
print "r:",r