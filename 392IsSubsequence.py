# -*- coding=utf-8 -*-

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        flag = True
    	len_s = len(s)
    	len_t = len(t)
    	pre = 0
    	for i in range(0,len_s):
    		print "pre",pre
    		print "s[i]",s[i]
    		if s[i] not in t[pre:] :
    			flag = False
    			break

    		index = t[pre:].index(s[i])+pre
    		print "index",index
    		pre = index+1
    	return flag

        

solution = Solution()
s = "abc"
t = "adbbec"
flag = solution.isSubsequence(s,t)

print flag

