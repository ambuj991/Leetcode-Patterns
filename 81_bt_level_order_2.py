# bt level order traversal 2

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
                res.insert(0, level)
        return res
     