#-*- coding=utf-8 -*-
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_num = len(nums)
        a = []
        k = k%len_num
        nums[:] = nums[len_num-k:]+nums[0:len_num-k]
        print nums
        


solution = Solution()
nums = [1,2,3]
k = 1
for i in range(0,1):
	print "i",i
r = solution.rotate(nums,k)
print "r:",r