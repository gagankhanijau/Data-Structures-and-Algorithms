# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

def max_overlapping(intervals):
    if not intervals : 
        return 0
    # print intervals
    intervals= sorted(intervals, key = lambda x: x[1], reverse=True )
    # print intervals
    ndx=0
    max_overlap=0
    while ndx<len(intervals):
        curr_st= intervals[ndx][0]
        temp=ndx
        print intervals, ndx, temp, max_overlap, curr_st
        while temp+1<len(intervals) and curr_st<=intervals[temp+1][1]:
            print temp,intervals[temp][1], curr_st
            temp+=1
        if temp-ndx+1>max_overlap:
            print temp,ndx
            max_overlap=temp-ndx+1
        ndx=temp +1 if ndx ==temp else temp
    return max_overlap


print max_overlapping([(30, 75), (0, 50), (60, 150)])
