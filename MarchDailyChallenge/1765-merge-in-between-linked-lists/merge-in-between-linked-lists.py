# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # 10->1->3->6->9->5
        # a = 3
        # b = 4
        # 1000-> 10001->10002
        # 10->1->3->1000-> 10001->10002->5
        temp1 = list1
        for i in range(a-1):
            temp1 = temp1.next
        temp2 = temp1.next
        # temp1.next = list2
        for i in range(b-a+1):
            temp2 = temp2.next
            # list2 = list2.next
        # dummy = temp2
        temp1.next = list2
        while list2 and list2.next:
            list2 = list2.next
        list2.next = temp2
        return list1