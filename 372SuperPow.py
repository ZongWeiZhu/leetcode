# -*- coding=utf-8 -*-

class Solution(object):
     def superPow(self, a, b):

     	circle = self.circle_r(a)
     	circle_len = len(circle)
     	r = 0
     	print circle
     	print circle_len
     	for i in b:
     		
     		r = (r*10+i) % circle_len
     		print r
     	return circle[r-1]
     def circle_r(self, a):
     	r = a % 1337
     	circle = []
     	while(r not in circle):
     		circle.append(r)
     		r = a*r%1337
     	return circle
solution = Solution()
a = 2
b = [1,0]
r = solution.superPow(a,b)
print "r:",r