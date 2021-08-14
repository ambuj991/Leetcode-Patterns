# minimum depth of binary tree
# bfs
def minDepth(self, root: TreeNode) -> int:
	if not root: return 0
	queue = deque([(root, 1)])
	while queue:
		node, depth = queue.popleft()
		if not node.left and not node.right: return depth
		for child in [node.left, node.right]:
			if not child: continue
			queue.append((child, depth + 1))

# dfs
class Solution:
    def minDepth(self, root ) -> int:
        #
        ## dfs
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == 0: return right+1
            if right == 0: return left+1
            return min(left,right)+1
        return dfs(root)