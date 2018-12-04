'''

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    #iterative
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            queue=[root,'#']
            curr=[]
            level_order_traversal=[]
            while len(queue)!=1:
                # print [x.val if x and x!='#' else x  for x in queue]
                temp=queue.pop(0)
                if temp=='#' :
                    # print "#############"
                    # print curr[:len(curr)/2],curr[-1:len(curr)/2-1:-1]
                    if cmp(curr[:len(curr)/2],curr[-1:len(curr)/2-1:-1])==0:
                        curr=[]
                        queue.append('#')
                    else:
                        return False
                else:
                    if temp:
                        if temp.left:
                            queue.append(temp.left)
                        else:
                            queue.append(None)
                        if temp.right:
                            queue.append(temp.right)
                        else:
                            queue.append(None)
                        curr.append(temp.val)
                    else:
                        curr.append(temp)
            return True
        else :
            return True
    
    #recursive
    def mirrorTree(self, root):
        if root and (root.left or root.right):
            root.left,root.right=root.right,root.left
            self.mirrorTree(root.left)
            self.mirrorTree(root.right)
            return root
        else:
            return root
    
    def checkEqualTree(self,root1,root2):
        if root1 and root2 and root1.val== root2.val:
            return self.checkEqualTree(root1.left,root2.left) and self.checkEqualTree(root1.right,root2.right)
        elif not root1 and not root2:
            return True
        else:
            return False
        
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.checkEqualTree(root.left, self.mirrorTree(root.right))
        else: 
            return True
    '''    
    
    #recursive2
    def symUtil(self, l,r):
        if not l and not r:
            return True
        elif (l and r) and l.val==r.val:
            return self.symUtil(l.left,r.right)  and self.symUtil(l.right,r.left)
        else:
            return False
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root :
            return True
        return self.symUtil(root.left, root.right)
            
        
        
        
        
        
        
        
        
        