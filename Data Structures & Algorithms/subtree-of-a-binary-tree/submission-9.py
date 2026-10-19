# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.sameTree(root, subRoot):
            return True
        if root is None:
            return False
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right 


    def sameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if tree1 == None and tree2 == None:
            return True
        if tree1 == None or tree2 == None:
            return False
        root = tree1.val == tree2.val
        left = self.sameTree(tree1.left, tree2.left)
        right = self.sameTree(tree1.right, tree2.right)
        return root and left and right
        
        
        