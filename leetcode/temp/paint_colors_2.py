# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

import sys
class Solution(object):
    def min_cost_paint(self, cost_matrix):
        if not cost_matrix:
            return 0 
        N= len(cost_matrix)
        K= len(cost_matrix[0])
        last_min= 0
        second_last_min=0
        last_ndx=-1
        # cost=[[0]*K for x in xrange(N)]
        for i in xrange(0,N):
            curr_min=sys.maxint
            second_curr_min= sys.maxint
            curr_ndx=-1
            for j in xrange(0,K):
                cost_matrix[i][j]+= second_last_min if j==last_ndx else last_min

                if cost_matrix[i][j]< curr_min:
                    second_curr_min= curr_min
                    curr_min=cost_matrix[i][j]
                    curr_ndx=j
                elif cost_matrix[i][j]<second_curr_min:
                    second_curr_min= cost_matrix[i][j]
            last_min,second_last_min,last_ndx = curr_min,second_curr_min, curr_ndx

        return min(cost_matrix[N-1])
        