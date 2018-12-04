'''Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            queue=[root,'#']
            curr=[]
            level_order_traversal=[]
            while len(queue)!=1:
                temp=queue.pop(0)
                if temp=='#':
                    level_order_traversal.append(curr)
                    curr=[]
                    queue.append(temp)
                else:
                    if temp.left:
                        queue.append(temp.left)
                    if temp.right:
                        queue.append(temp.right)
                    curr.append(temp.val)
            level_order_traversal.append(curr)
            return level_order_traversal
        else :
            return []