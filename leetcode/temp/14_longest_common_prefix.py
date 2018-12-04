# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: 
            return ""
        longest_pre= strs[0]
        longest_len=len(strs[0])
        for i in xrange(1,len(strs)):
            ndx=0
            while (ndx<longest_len and ndx< len(strs[i])) and strs[i][ndx]== longest_pre[ndx]:
                ndx+=1
            longest_len=ndx
        return longest_pre[:longest_len]