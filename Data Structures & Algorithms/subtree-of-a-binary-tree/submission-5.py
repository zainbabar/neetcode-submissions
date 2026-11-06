# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# start with looking at root vals, they have to be same for the subroot 
# so keep going down the tree until we hit one with same vals 
# if we are at a leaf then not possible to be a subroot anymore ? 

class Solution:   
    def sameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            left = self.sameTree(p.left, q.left)
            right = self.sameTree(p.right, q.right)
            return (left and right)
        else:
            return False
    
    def validStart(self, root, subroot):
        if root and subroot:
            same = False
            if root.val == subroot.val:
                same = self.sameTree(root, subroot)
            if same:
                return True
            if not same:
                left = self.validStart(root.left, subroot)
                right = self.validStart(root.right, subroot)
                return (left or right)
        return False
            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.validStart(root, subRoot)