# Binary tree right side
def rightSideView(self, root):
        res = []
        q  = []
        q.append(root)
        while q:
            l = []
            qlen = len(q)
            for i in range(qlen):
                node = q.pop(0)
                if node:
                    l.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if l:
                res.append(l[-1])
        return res
        
def rightSideView(root):
        res = []
        q  = []
        q.append(root)
        while q:
            l = None
            qlen = len(q)
            for i in range(qlen):
                node = q.pop(0)
                if node:
                
                    l = node.data
                    q.append(node.left)
                    q.append(node.right)
                
            if l:
                res.append(l)
        return res