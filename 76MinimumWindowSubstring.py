#-*- coding = utf-8 -*-
import re
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = len(t)
        minileft = 0
        miniSize = len(s) + 1
        left = 0
        cmap1 = {}
        cmap2 = {}
        for c in t:
            if c not in cmap1:
                cmap1[c] = 1
                cmap2[c] = 1
            else:
                cmap1[c] += 1
                cmap2[c] += 1
        print cmap2
        for right in range(len(s)):

            if s[right] in cmap1:
                cmap2[s[right]] -= 1
                print "come in "
                if cmap2[s[right]] >= 0:
                    count -= 1
                if count == 0:
                        while True:
                            if s[left] in cmap2:
                                if cmap2[s[left]] < 0:
                                    cmap2[s[left]] += 1
                                else:
                                    break 
                            print "left",left
                            left += 1

                        if right - left + 1 < miniSize:
                            minileft = left
                            miniSize = right - minileft + 1

            

        if miniSize < len(s) + 1:
            return s[minileft:minileft + miniSize]
        else:
            return ''
s = "ADOBECODEBANC"
t = "ABC"

#print a
solution = Solution()
r = solution.minWindow(s,t)
print r
