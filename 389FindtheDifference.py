#-*- coding=utf-8 -*-
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        len_s = len(s)
        len_t = len(t)
        d_s = {}
        d_t = {}
        for i in range(len_s):
        	if s[i] not in d_s:
        		d_s[s[i]] = 1
        	else:
        		d_s[s[i]] = d_s[s[i]]+1

        for i in range(len_t):
        	if t[i] not in d_t:
        		d_t[t[i]] = 1
        	else:
        		d_t[t[i]] = d_t[t[i]]+1
        for i in d_t:
        	if i not in d_s:
        		return i
        	else:
        		if d_s[i] != d_t[i]:
        			return i


solution = Solution()
s = "abcd"
t = "abcde"
r = solution.findTheDifference(s,t)
print r