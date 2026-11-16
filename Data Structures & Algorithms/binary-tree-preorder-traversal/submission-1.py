# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, traversal):
        if not root:
            return 
        
        traversal.append(root.val)
        self.dfs(root.left, traversal)
        self.dfs(root.right, traversal)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        self.dfs(root, traversal)
        return traversal
