# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        id_set = set()
        tail = head
        while tail:
            if id(tail) not in id_set:
                id_set.add(id(tail))
                tail = tail.next
            else:
                return True
        return False
            



        