# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        node = head.next
        head.next = None
        prev_node = head
        while node:
            # wire cur to the prev node and store the old next node
            next_node = node.next
            node.next = prev_node # next ptr
            head = node 

            # update the nodes to wire tg in the next iter
            prev_node = node
            node = next_node 
        return head

