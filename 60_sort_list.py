
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next :
            return head
        left = head
        right = self.getMid(head)
        t = right.next
        right.next = None
        right = t
        
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)
    
    def getMid(self, head):
        slow,fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow
    
    def merge(self, l1, l2):
        tail = dummy = ListNode()
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
                 
                
                