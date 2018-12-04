'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]
        else:
            return []
    '''
    #iterative 2 stacks
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            stack=[root]
            postorder=[]
            while stack:
                temp=stack.pop(-1)
                postorder.append(temp.val)
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
            postorder.reverse()         
            return postorder      
        else:
            return []

    '''
    #iterative 1 stack
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            stack=[]
            postorder=[]
            while root or stack:
                while root:
                    if root.right:
                        stack.append(root.right)
                    stack.append(root)
                    root=root.left
                temp=stack.pop(-1)
                if temp.right and ( len(stack) and temp.right.val==stack[-1].val):
                    stack.pop(-1)
                    stack.append(temp)
                    root=temp.right
                else:
                    postorder.append(temp.val)
                    root=None
            return postorder
        else:
            return []
        '''