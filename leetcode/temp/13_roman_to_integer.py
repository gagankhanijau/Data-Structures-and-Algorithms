# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def __init__(self):
        self.map= {"I":   1,"V":   5,"X" :  10,"L" :  50,"C"  : 100,"D"  : 500,"M"   :1000}
        self.keys=self.map.keys()
        self.keys= sorted(self.keys, key=lambda x:self.map[x])
        
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ndx=0
        res=0
        while ndx<len(s):
            if ndx+1<len(s) and self.keys.index(s[ndx]) < self.keys.index(s[ndx+1]):
                res+= self.map[s[ndx+1]]-self.map[s[ndx]]
                ndx+=2
            else:
                res+=self.map[s[ndx]]
                ndx+=1
        return res