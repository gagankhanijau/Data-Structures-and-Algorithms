# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

# Example 1:
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
# Example 2:
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
# Note:
# cost will have a length in the range [2, 1000].
# Every cost[i] will be an integer in the range [0, 999].

class Solution(object): 
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        steps=[0]*(len(cost)+1)
        steps[0]=cost[0]
        steps[1]=cost[1]
        for i in xrange(2,len(steps)-1):
            steps[i]= cost[i]+min(steps[i-1],steps[i-2])
        steps[len(cost)]= min(steps[len(cost)-1], steps[len(cost)-2])    
        return steps[-1]
        

