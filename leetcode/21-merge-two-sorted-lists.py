# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

from requests import head
from linked_list import ListNode, convert_list_to_linkedlist


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = head = ListNode()
        while list1 or list2:
            if list1 is None or list2 is None:
                temp = list1 or list2
                list3.next = ListNode(temp.val, temp.next)
                break
            elif list1.val <= list2.val:
                list3.next = ListNode(list1.val, list1.next)
                list1 = list1.next
            else:
                list3.next = ListNode(list2.val, list2.next)
                list2 = list2.next
            list3 = list3.next
        return head.next

sol = Solution()
print(sol.mergeTwoLists(convert_list_to_linkedlist(
    [1, 2, 4]), convert_list_to_linkedlist([1, 3])))
print(sol.mergeTwoLists(convert_list_to_linkedlist(
    []), convert_list_to_linkedlist([])))
print(sol.mergeTwoLists(convert_list_to_linkedlist(
    []), convert_list_to_linkedlist([0])))
