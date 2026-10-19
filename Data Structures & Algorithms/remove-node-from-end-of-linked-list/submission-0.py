# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_arr = []
        tail = head
        while tail:
            node_arr.append(tail)
            tail = tail.next
        dummy = ListNode()
        tail = dummy
        for i in range(len(node_arr)):
            if i == len(node_arr) - n:
                continue
            else:
                tail.next = node_arr[i]
                tail = tail.next
        tail.next = None
        return dummy.next

        