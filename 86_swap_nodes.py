# swap nodes in pairs
# O(n), O(1)
class Solution:
    def swapPairs(self, head ):
        dummy = ListNode(0 ,head)
        curr, prev = head, dummy
        
        while curr and curr.next:
            nxtpair = curr.next.next
            second = curr.next
            second.next = curr
            curr.next = nxtpair
            prev.next = second
            
            prev = curr
            curr = nxtpair
        return dummy.next
        