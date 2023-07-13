# https://leetcode.com/problems/linked-list-cycle/

from linked_list import ListNode, convert_list_to_linkedlist


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dummy = ListNode()
        while head.next:
            if head.next == dummy:
                return True
            temp = head.next
            head.next = dummy
            head = temp
        return False
    
    def hasCycle2(self, head: ListNode) -> bool:
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
        return False
    
    def hasCycle3(self, head: ListNode) -> bool:
        nodes_set = set()
        if head is None:
            return False
        while head.next:
            if head in nodes_set:
                return True
            nodes_set.add(head)
            head = head.next
        return False

sol = Solution()
node1 = ListNode(1, None)
node2 = ListNode(2, node1)
node3 = ListNode(3, node2)
node4 = ListNode(4, node3)
node1.next = node4
print(sol.hasCycle(node4))
