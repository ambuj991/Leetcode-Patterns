# bt level order traversal
import collections
class Solution:
    def levelOrderBottom(self, root) :
        q = collections.deque()
        res = []
        q.append(root)
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

# O(n)