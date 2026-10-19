# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None and q:
            return False
        elif p and q == None:
            return False
        else:
            if p.right == None and p.left == None and q.right == None and q.left == None:
                if p.val == q.val:
                    return True
                else:
                    return False
            else:
                left = self.isSameTree(p.left, q.left)
                right = self.isSameTree(p.right, q.right)
                return left and right
        
        