import sys
class Solution(object):
    
    # def find_max(self, height, l,r, side="R"):
    #     flow = xrange(l,r+1) if side =="R" else xrange(r,l-1,-1)
    #     ndx, max_v= -1 , -1* sys.maxint
    #     for i in flow: 
    #         if height[i] >=max_v:
    #             ndx,max_v= i, height[i]
    #     return ndx

    # def trap_util(self, height, l, r, side):
    #     if l<0 or r>= len(height) or r<0 or l>= len(height) :
    #         return 0
    #     ndx = self.find_max(height,l, r-1, side) if side=="L" else self.find_max(height, l+1, r, side)
    #     vol=0
    #     # print l,r,ndx ,side, height[l],height[r],height[ndx]
    #     flow= xrange(l+1,ndx) if side =="R" else xrange(r-1,ndx,-1)
    #     for i in flow: 
    #         vol+= (height[ndx]-height[i])
    #     if ndx is not 0 and side=='L':
    #         vol+= self.trap_util(height, l,ndx, side)
    #     elif ndx is not len(height)-1 and side=="R":
    #         vol+= self.trap_util(height, ndx,r, side)
    #     # print vol    
    #     return vol

    # def trap(self, height):
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #     # if height and len(height)>1:
    #     ndx= self.find_max(height,0,len(height)-1)
    #     return self.trap_util(height,0,ndx,"L")+ self.trap_util(height, ndx, len(height)-1,"R")
    #     # return 0

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height :
            return 0
        ndx= height.index(max(height))
        # print ndx, height[ndx]
        l_stack,r_stack=[],[]
        if ndx !=0:
            l_stack=[ndx-1]
        if ndx!=len(height)-1:
            r_stack=[ndx+1]
        vol=0
        for i in xrange(ndx-1, -1, -1):
            # print l_stack, height[i]
            # if l_stack  and height[l_stack[-1]]<= height[i]:
            while l_stack and height[l_stack[-1]]<=height[i]:
                l_stack.pop()
            l_stack.append(i)
        # print l_stack,[height[i] for i in l_stack]
        r=ndx
        while l_stack:
            l= l_stack.pop(0)
            # print l, r,vol
            for i in xrange(r-1,l,-1):
                vol+= height[l]-height[i]
            r=l    

        for i in xrange(ndx+1, len(height)):
            # print r_stack, height[i]
            # if r_stack  and height[r_stack[-1]]<= height[i]:
            while r_stack and height[r_stack[-1]]<=height[i]:
                r_stack.pop()
            r_stack.append(i)
        # print r_stack,[height[i] for i in r_stack]
        l=ndx
        while r_stack:
            r= r_stack.pop(0)
            # print l,r,vol
            for i in xrange(l+1,r):
                vol+= height[r]-height[i]
            l=r 
            # print vol
        return vol       


