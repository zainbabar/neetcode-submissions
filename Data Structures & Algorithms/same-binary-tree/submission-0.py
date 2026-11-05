# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTreeHelper(self, p, q):
        # both null so its fine 
        if not p and not q:
            return True
        # only one is null so they cant be the same
        elif not p or not q:
            return False
        # both exist move on 
        same = False
        if p.val == q.val:
            left_same = self.isSameTreeHelper(p.left, q.left)
            right_same = self.isSameTreeHelper(p.right, q.right)
            if left_same and right_same:
                same = True
        else:
            return False 
        return same
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isSameTreeHelper(p, q)