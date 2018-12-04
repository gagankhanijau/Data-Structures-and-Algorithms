'''
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL



'''

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:

    # def connectUtil(self, l, r):
    #     l.next=r
    #     pvs=None
    #     if l.left:
    #         pvs= l.left
    #     if l.right:
    #         if pvs:
    #             self.connectUtil(l.left,l.right)
    #         pvs= l.right
    #     if r.left:
    #         if pvs:
    #             self.connectUtil(pvs,r.left)
    #         pvs=r.left
    #     if r.right and pvs:    
    #         self.connectUtil(pvs,r.right)
        
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root :
            return
        queue=[root,'#']
        while len(queue)>1:
            temp= queue.pop(0)
            if temp=='#':
                queue.append(temp)
            else:
                if queue[0]!='#':
                    temp.next=queue[0]
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                
                
                
                
                
                
                