# 

import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums= nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count= 0
        res=0
        for i in xrange(len(self.nums)):
            if target==self.nums[i]:
                count+=1
            if count==1:
                res=i
            elif count>1 and random.randint(0,count-1)==0:
                res=i
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)