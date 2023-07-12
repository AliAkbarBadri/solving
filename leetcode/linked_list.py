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
        return string[:-3]

def convert_list_to_linkedlist(lst: list) -> ListNode:
    head = dummy = ListNode()
    for item in lst:
        dummy.next = ListNode(item)
        dummy = dummy.next
    return head.next