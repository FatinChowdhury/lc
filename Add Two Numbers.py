# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # break the links between l1, same for l2.
        # make l1 nodes link to l2 nodes
        # add up the nodes, self.val + self.next.val
        # if self.val + self.next.val >=10 then return self.val + self.next.val %10
        # and do operation for next set of nodes but add 1
        dummy = ListNode()
        carry=0
        cur=dummy

        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val=v1+v2+carry
            carry = val // 10
            val = val%10
            cur.next = ListNode(val)

            cur=cur.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next


