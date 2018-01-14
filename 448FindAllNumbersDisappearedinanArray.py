class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        len_nums = len(nums)
        d = {}
        r = []
        for i in range(1,len_nums+1):
        	d[i] = 0
        for i in nums:
        	d[i] =  i
        for key,value in d.items():
        	if value == 0:
        		r.append(key)

        return r

        
solution = Solution()
nums = [4,3,2,7,8,2,3,1]
r = solution.findDisappearedNumbers(nums)
print r