def reverseList(self, head: ListNode) -> ListNode:
       # print(head)
        if head is None:
            return None
        curr = head
        prev = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        return head