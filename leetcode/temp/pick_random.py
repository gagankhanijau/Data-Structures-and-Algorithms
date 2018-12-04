# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
import random
class Solution(object):
    def __init__(self):
        self.count =0
        self.res=0
    def pick_random(self,num):
        self.count+=1
        if self.count==1:
            self.res=num
            return num
        rand= random.randint(0,self.count-1)
        if rand==self.count-1:
            self.res= num
        return self.res

obj= Solution()
x= range(10)
random.shuffle(x)
print x
for i in x:
    print obj.pick_random(i)
