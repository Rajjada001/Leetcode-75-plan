# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # None 1->2->3->4->5
    #      h
    #      c
    # Prev
    #     1->2->3->4->5
    #         t  
    #             c
    #         p

        if not head:
            return head
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
            