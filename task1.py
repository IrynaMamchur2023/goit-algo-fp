class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev_node = None
    curr_node = head

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node 

def insertion_sort_linked_list(head):
    if not head or not head.next:
        return head

    dummy = ListNode(float("-inf"))
    dummy.next = head
    last_sorted = head

    while last_sorted.next:
        if last_sorted.next.val < last_sorted.val:
            prev = dummy

            while prev.next.val < last_sorted.next.val:
                prev = prev.next

            temp = last_sorted.next
            last_sorted.next = temp.next
            temp.next = prev.next
            prev.next = temp
        else:
            last_sorted = last_sorted.next

    return dummy.next
def merge_two_sorted_lists(l1, l2):
    dummy = ListNode(float("-inf"))
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    current.next = l1 if l1 else l2

    return dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

node1.next = node2
node2.next = node3


reversed_head = reverse_linked_list(node1)


sorted_head = insertion_sort_linked_list(reversed_head)


while sorted_head:
    print(sorted_head.val)
    sorted_head = sorted_head.next