#-*- coding=utf-8 -*-

def isMatch(s, p):
    length = len(s)
    if len(p) - p.count('*') > length:
        return False
    dp = [True] + [False]*length
    for i in p:
    	print i 
    	
        if i != '*':
            for n in reversed(range(length)):
                dp[n+1] = dp[n] and (i == s[n] or i == '?')
        else:
            for n in range(1, length+1):
                dp[n] = dp[n-1] or dp[n]
        dp[0] = dp[0] and i == '*'
        print dp
    return dp[-1]

s = "abefcdgiescdfimde"
p = "ab*cd?i*de"
r = isMatch(s,p)
print r