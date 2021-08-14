class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        t = root.left
        root.left = root.right
        root.right = t
        self.invertTree( root.left)
        self.invertTree( root.right)
        return root


# tc = O(n)
# sc = O(n) funtion calls