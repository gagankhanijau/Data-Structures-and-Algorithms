# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        res=[]
        i=0
        while i<len(nums):
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    res.append([nums[i],nums[j],nums[k]])
                    if j<k and nums[j+1]==nums[j]:
                        j+=1
                        while j<k and nums[j]==nums[j-1]:
                            j+=1
                    else:
                        k-=1
                        while j<k and nums[k]==nums[k+1]:
                            k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0: 
                    k-=1
            i+=1
            while i<len(nums) and nums[i]==nums[i-1]:
                i+=1
        return res
            