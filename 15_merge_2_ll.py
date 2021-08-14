# merge 2 sorted linked list

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = dummy = ListNode(0) # Creating a dummy node
       #Check for the edge cases
        if(l1 is None) or l2 is None:
            return l2 or l1
        
        while(l1 and l2):
            if(l1.val < l2.val):
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
            
        if l1 or l2:
            temp.next = l1 or l2