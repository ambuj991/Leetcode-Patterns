
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head


head = ListNode(1)
print(removeNthFromEnd(head, 1))
# edge case
# n = 3 linked list = [1,2,3]

# When n is same with the length of the list. We need to remove first element, instead remove next element of curr.
# In this case, you can find that hare would be null, because the last element of list points null such as [1,2,3,null]
# complexity

# Time complexity: O(N)
# Space complexity: O(1)
