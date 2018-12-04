# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time

###########recursive
# def possible_steps(N,A=[1,2],steps={}):
#     if not N :
#         return 1
#     if steps.get(N,None):
#         # print "repeat"
#         return steps[N]
#     minA=min(A)
#     res=0
#     for i in A: 
#         if N>i or N-i==0 or N-i>=minA:
#             steps_N_less_i= possible_steps(N-i, A, steps)
#             res+= steps_N_less_i
#     steps[N]= res
#     # print N, steps[N]
#     return steps[N]


# print possible_steps(30)

#########iterative
class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps=[0]*(n+1)
        steps[0]=1
        steps[1]=1
        if n >1:
            for i in xrange(2,n+1):
                steps[i]=steps[i-1]+steps[i-2]
        return steps[n]