# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        while left<right:
            values[left-1],values[right-1] = values[right-1],values[left-1]
            left += 1
            right -= 1
        dummy = ListNode(0)
        curr = dummy
        for value in values:
            curr.next = ListNode(value)
            curr = curr.next
        return dummy.next