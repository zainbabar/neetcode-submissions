class Solution:
    def dfs(self, root, traversal):
        if not root:
            return

        self.dfs(root.left, traversal)
        traversal.append(root.val)
        self.dfs(root.right, traversal)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        self.dfs(root, traversal)
        return traversal