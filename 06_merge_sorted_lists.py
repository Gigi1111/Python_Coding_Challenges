# https://leetcode.com/problems/merge-two-sorted-lists/submissions/
## method 1: 64% 35% O(min(m,n)), O(min(m,n))
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        ans = ListNode(-1)
        current = ans
        while list1 and list2:
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return ans.next
## method 2:
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        ans = ListNode(-1)
        current = ans
        while list1 and list2:
            current.next = ListNode(list1.val) if list1.val <= list2.val else ListNode(list2.val)
            tmp1 = list1.val
            list1 = list1.next if list1.val <= list2.val else list1
            list2 = list2.next if tmp1 > list2.val else list2

            current = current.next

        current.next = list1 if list1 else list2

        return ans.next
