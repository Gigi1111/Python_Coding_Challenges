# https://leetcode.com/problems/add-two-numbers/solution/
## method 1: 88% 64% O(max(m,n)), O(max(m,n)+1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        ans_cur = ans
        carry = 0
        while l1 or l2 or carry:
            ans_cur.next = ListNode()
            ans_cur = ans_cur.next

            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, ans_cur.val = divmod(val1 + val2 + carry, 10)

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return ans.next
### method2: 62% 82%
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
