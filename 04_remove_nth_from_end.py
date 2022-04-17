# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
## method 1: 86% 22%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def listToListNode(self, l: list):
#         head = ListNode(l[0])
#         cur = head
#         for i in range(1,len(l)):
#             cur.next = ListNode(l[i])
#             cur = cur.next
#         return head
#
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         if not head:
#             return head
#         cur = head
#         nodes = []
#         while cur:
#             nodes.append(cur)
#             cur = cur.next
#         if len(nodes) < n or n < 1:
#             return head
#
#         idx = len(nodes) - n
#         if idx < 0 or idx >= len(nodes):
#             return head
#
#         if idx == 0:
#             head = head.next
#         elif idx == len(nodes)-1:
#             nodes[-2].next = None
#         else:
#             nodes[idx-1].next = nodes[idx+1]
#
#         self.printList(head)
#
#     def printList(self, head: ListNode):
#         cur = head
#         while cur:
#             print(cur.val,'-->', end=' ')
#             cur = cur.next
#         print('')
#
# ob = Solution()
# head = ob.listToListNode([1,2,3])
# ob.removeNthFromEnd(head,3)
class Solution:
    def listToListNode(self, l: list):
        head = ListNode(l[0])
        cur = head
        for i in range(1,len(l)):
            cur.next = ListNode(l[i])
            cur = cur.next
        return head

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        count = head
        counter = 0
        while count:
            count = count.next
            counter += 1
        n = counter - n
        if n < 0 or n >= counter:
            return head
        if n == 0:
            return head.next
        cur = head
        i = 0
        while cur and i < counter:
            if i+1 == n and cur.next:
                cur.next = cur.next.next
            cur = cur.next
            i+=1

        return head

    def printList(self, head: ListNode):
        cur = head
        while cur:
            print(cur.val,'-->', end=' ')
            cur = cur.next
        print('')

ob = Solution()
head = ob.listToListNode([1,2,3,4,5])
ob.printList(ob.removeNthFromEnd(head,2))
