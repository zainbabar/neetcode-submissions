# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTreeHelper(self, root):
        temp = root.left
        root.left = root.right
        root.right = temp
        if root.left:
            root.left = self.invertTreeHelper(root.left)
        if root.right:
            root.right = self.invertTreeHelper(root.right)
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        else:
            return self.invertTreeHelper(root)
