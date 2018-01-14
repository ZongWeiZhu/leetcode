#-*- coding=utf-8 -*-
class Solution(object):
    def removeDuplicateLetters(self, s):
        for c in sorted(set(s)):
            suffix = s[s.index(c):]
            if set(suffix) == set(s):
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''
solution = Solution()
s = "bacdba"
r = solution.removeDuplicateLetters(s)
print r