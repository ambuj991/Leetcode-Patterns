# subtree of another tree

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t is None: return True
        def dfs(p, q):
            if not p and not q: return True
            if not p or not q or p.val != q.val: return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)        
        
        def find(s, t):
            if s is None:
                return False
            if dfs(s, t): return True
            return find(s.left, t) or find(s.right, t)
        
        return find(s, t)