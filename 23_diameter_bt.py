# diameter of bt

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res =[0]
        def dfs(root):
            if not root:
                return -1
            l =dfs(root.left)
            r =dfs(root.right)
            res[0] = max(res[0], 2+l+r)
            return 1+max(l,r)
        dfs(root)
        return res[0]
            