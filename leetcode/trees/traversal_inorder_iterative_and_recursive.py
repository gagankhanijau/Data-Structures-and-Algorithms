'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    #recursive
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root :
            return self.inorderTraversal(root.left) +[root.val]+self.inorderTraversal(root.right)
        else :
            return []
    '''
    #iterative 1
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """    
        if root:
            stack=[root]
            stack_vis=[0]
            inorder=[]
            while stack:
                if stack_vis[-1]==0 and stack[-1].left:
                    stack_vis[-1]=1
                    stack.append(stack[-1].left)
                    stack_vis.append(0)
                elif stack_vis[-1] == 1:
                    temp=stack.pop(-1)
                    stack_vis.pop(-1)
                    inorder.append(temp.val)
                    if temp.right:
                        stack.append(temp.right)
                        stack_vis.append(0)
                else:
                    stack_vis[-1]=1
            return inorder        
        else:
            return []

    
    '''
     #iterative 2
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """    
        if root:
            stack=[]
            curr = root
            # stack_vis=[0]
            inorder=[]
            while stack or curr:
                while curr:
                    stack.append(curr)
                    curr= curr.left
                curr=stack.pop(-1)
                inorder.append(curr.val)
                curr= curr.right
            return inorder      
        else:
            return []
    '''
        