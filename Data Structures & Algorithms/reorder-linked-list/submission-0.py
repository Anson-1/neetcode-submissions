# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        tail = dummy
        move = head
        n = 0
        while move:
            move = move.next
            n += 1
        move = head
        step = 1
        for i in range(n):
            if i % 2 == 0:
                tail.next = move
                move = move.next
                tail = tail.next
            else:
                last = move
                for j in range(n-i-1):
                    last = last.next
                tail.next = last
                tail = tail.next
        tail.next = None
        head = dummy.next



        