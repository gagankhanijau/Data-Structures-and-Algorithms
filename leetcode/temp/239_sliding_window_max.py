# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space.

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not list or k<=1:
            return nums
        dequeue= list()
        res=list()
        for i in xrange(k):
            while dequeue and nums[dequeue[-1]] < nums[i]:
                dequeue.pop(-1)
            dequeue.append(i)

        for i in xrange(k, len(nums)):
            res.append(nums[dequeue[0]]) 
            while dequeue and i-dequeue[0]>=k:
                dequeue.pop(0)
            while dequeue and nums[dequeue[-1]] < nums[i]:
                dequeue.pop(-1)                
            dequeue.append(i)
        res.append(nums[dequeue[0]])    
        return res

if __name__ == "__main__":
    x= Solution()
    print x.maxSlidingWindow([10,2,5,3],3)        