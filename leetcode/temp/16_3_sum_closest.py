# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:

# Given array nums = [-1, 2, 1, -4], and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res=None
        min_diff= sys.maxint
        i=0
        while i<len(nums):
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==target:
                    return target
                curr_diff= abs(nums[i]+nums[j]+nums[k]- target)
                if curr_diff <  min_diff:
                    # print nums[i],nums[j],nums[k]
                    min_diff=curr_diff
                    res= nums[i]+nums[j]+nums[k]
                if nums[i]+nums[j]+nums[k]<target:
                    j+=1
                else:
                    k-=1
            i+=1
            # while i<len(nums) and nums[i]==nums[i-1]:
            #     i+=1
        return res