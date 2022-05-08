# https://leetcode.com/problems/swap-nodes-in-pairs/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # add a previous dummy node
        cur = dummy = ListNode(0)
        cur.next = head
        # check if next 2 nodes exist and ready for swap
        while cur.next and cur.next.next:
            first = cur.next
            second = first.next
            next_pair = second.next
            cur.next, second.next, first.next = second, first, next_pair 
            cur = first
        return dummy.next