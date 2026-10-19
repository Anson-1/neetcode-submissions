# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_arr = []
        tail = head
        while tail:
            node_arr.append(tail)
            tail = tail.next
        dummy = ListNode()
        dummy_tail = dummy
        even = 0
        odd = 1
        for i in range(len(node_arr)):
            if i % 2 == 0:
                dummy_tail.next = node_arr[even]
                dummy_tail = dummy_tail.next
                even += 1
            else:
                dummy_tail.next = node_arr[len(node_arr)-odd]
                dummy_tail = dummy_tail.next
                odd += 1
        dummy_tail.next = None
        head = dummy.next





        