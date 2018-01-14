#-*- coding=utf-8 -*-
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        len_nums = len(nums)
        if len_nums == 0:
        	return []
        nums = sorted(nums)
        dp = [1]*len_nums
        pre = [None]*len_nums
        for x in range(len_nums):
        	for y in range(x):
        		if nums[x] % nums[y] == 0 and dp[y]+1 > dp[x]:
        			dp[x] = dp[y]+1
        			pre[x] = y
        r = []
       	idx = dp.index(max(dp))
       	while idx is not None:
       		r.append(nums[idx])
       		idx = pre[idx]
       	return r
        
solution = Solution()
nums  = [2,2,4,8,9,10,12]
r = solution.largestDivisibleSubset(nums) 
print r