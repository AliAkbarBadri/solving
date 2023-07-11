# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        curr = self
        string = ""
        while curr:
            string += f"{curr.val} -> "
            curr = curr.next
        return string


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


sol = Solution()
print(sol.reverseList(head=ListNode(val=1, next=ListNode(val=2, next=ListNode(
    val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))))
print(sol.reverseList(head=ListNode(val= 1, next= ListNode(val= 2, next= None))))
print(sol.reverseList(head=None))

