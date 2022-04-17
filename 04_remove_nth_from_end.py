# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
## method 1: 94% 22%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
                return head
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
