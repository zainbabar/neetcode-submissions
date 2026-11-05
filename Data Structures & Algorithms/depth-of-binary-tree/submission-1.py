# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepthHelper(self, root, depth):
        max_depth = depth
        if root.left:
            left_depth = depth + 1
            left_depth = self.maxDepthHelper(root.left, left_depth)
            max_depth = max(left_depth, max_depth)
        if root.right:
            right_depth = depth + 1
            right_depth = self.maxDepthHelper(root.right, right_depth)
            max_depth = max(right_depth, max_depth)
        return max_depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.maxDepthHelper(root, 1)
    