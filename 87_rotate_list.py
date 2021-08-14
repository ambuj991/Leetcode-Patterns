def rotateRight( head, k):
        if not head:
            return None
        length, tail = 1, head
        while tail.next:
            length += 1
            tail = tail.next
        k = k % length
        if k ==0: return head
        curr = head
        for i in range(length -k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        tail.next = head
        return new_head