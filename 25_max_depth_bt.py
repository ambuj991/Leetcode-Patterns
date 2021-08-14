class Solution:
    def maxDepth(self, node: TreeNode) -> int:
        if node is None: return 0
        left=self.maxDepth(node.left)
        right=self.maxDepth(node.right)
        return 1+max(left,right)
