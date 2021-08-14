# remove duplicates from ll 
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
            if not head:
                return None
    
            pre = head
            cur = head.next
    
            while cur:
                if cur.val == pre.val:
                    pre.next = cur.next
                    cur = cur.next
                else:
                    cur = cur.next
                    pre = pre.next
            return head
        