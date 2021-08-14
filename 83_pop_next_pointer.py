# Populating Next Right Pointers in Each Node   O(n), O(n)
import collections
class Solution:
    def connect(self, root):
        if not root:return None
        q = collections.deque()
        res = []
        q.append(root)
        while q:
            node = q.popleft()
            if node.left:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                q.append(node.left)
                q.append(node.right)
        return root
        
def connect( root):
    while root and root.left:
        next = root.left
        while root:
            root.left.next = root.right
            root.right.next = root.next and root.next.left
            root = root.next
        root = next         
# O (n), O(1)
