# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow moves 1 and fast moves 2, so the gap between them shrinks by exactly 1
        # each step and can't skip 0, so they meet if there's a cycle
        p1 = head
        p2 = head
        # fast pointer needs two nodes ahead of it to jump twice
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 is p2:
                return True
        return False
