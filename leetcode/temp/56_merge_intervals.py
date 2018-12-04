# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals : 
            return []
        intervals= sorted(intervals, key = lambda x: x.end, reverse=True )
        ndx=0
        res=[]
        while ndx<len(intervals):
            curr_st= intervals[ndx].start
            curr_end= intervals[ndx].end
            temp=ndx
            while temp+1<len(intervals) and curr_st<=intervals[temp+1].end:
                temp+=1
                curr_st= min(intervals[temp].start, curr_st)
            res= [intervals[ndx]]+res if ndx==temp else [Interval(curr_st,curr_end)]+res    
            ndx= temp+1   
        return res