# O(n) and O(n)
class Solution:
    def detectCycle(self, head):
        curr = head
        lookup = set()
        while curr:
            if curr in lookup:
                return curr
            lookup.add(curr)
            curr = curr.next
        return None


#O(n) and O(1)
def detectCycle( head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast: break
        print('----------',slow.data,'-------',fast.data,'-----')
                
        if not fast or not fast.next: return None
        slow = head
        print(slow.data,'-', fast.data)
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow