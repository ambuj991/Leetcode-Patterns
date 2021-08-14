# linked list cycle 

def hasCycle(self, head: ListNode) -> bool:        
        curr = head
        
        while curr:
            if curr.val is None:
                return True
            curr.val = None
            curr = curr.next
        
        return False

