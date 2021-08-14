class Solution:
    def hasPathSum(self, root,targetSum):
        if not root:
            return False
        if root.left is None and root.right is None and targetSum == root.val:
            return True
        return (self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val))