class Solution:
    def reorderList(self, head) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        
        while second:
            t = second.next
            second.next = prev
            prev = second
            second = t
        second = prev
        while second:
            t1, t2 = head.next, second.next
            head.next = second
            second.next = t1
            head, second = t1, t2
            
            
       