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
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def __init__(self):
        self.mapping={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000 :"M"} 
        self.key_list=self.mapping.keys()
        self.key_list.sort(reverse=True)
        
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num is 0 :
            return ""
        else :
            ndx=0
            res=[]
            key= self.key_list[ndx]
            while num and key:
                per = [0.9,2] if key !=1 and key/2 in self.key_list else [0.8,1]
                if num >= key:
                    quo= num/key
                    num %= key
                    res+= [self.mapping[key] for i in xrange(quo)]
                elif num>= key*per[0]: 
                    quo= num/int(key*per[0])
                    num%=int(key*per[0])
                    res+=[self.mapping[self.key_list[ndx+per[1]]]+self.mapping[key] for i in  xrange(quo)]
                else:
                    ndx+=1
                    key= self.key_list[ndx]
            return "".join(res)
                    
            

        