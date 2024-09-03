# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next # draw the line for 2nd half
        prev = slow.next = None # end of first half will point to null
        while second: # time to reverse
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            # linked list reversed
        
        # merging 2 halves
        second = prev
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

            
