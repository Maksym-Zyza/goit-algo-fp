class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values) + " -> None"

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Sort the linked list
    def sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None
        left = self._merge_sort(head)
        right = self._merge_sort(second_half)
        return self._merge(left, right)

    def _merge(self, left, right):
        dummy = Node(0)
        current = dummy
        while left and right:
            if left.data <= right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        current.next = left if left else right
        return dummy.next

    # Merge two sorted linked lists
    def merge_sorted_lists(self, other_list):
        result = LinkedList()
        result.head = self._merge(self.head, other_list.head)
        return result


# Test
def test_linked_list():
    print("Test 1: Reversing a linked list")
    list1 = LinkedList()
    for data in [10, 20, 30, 40, 50]:
        list1.append(data)
    print("Original list:", list1)
    list1.reverse()
    print("Reversed list:", list1)
    print()

    print("Test 2: Sorting a linked list")
    list2 = LinkedList()
    for data in [33, 12, 98, 4, 76, 45]:
        list2.append(data)
    print("Unsorted list:", list2)
    list2.sort()
    print("Sorted list:", list2)
    print()

    print("Test 3: Merging two sorted linked lists")
    list3 = LinkedList()
    for data in [1, 4, 7, 10]:
        list3.append(data)
    list4 = LinkedList()
    for data in [2, 3, 6, 8, 9]:
        list4.append(data)
    print("List 1:", list3)
    print("List 2:", list4)
    merged_list = list3.merge_sorted_lists(list4)
    print("Merged sorted list:", merged_list)


# Run the tests
test_linked_list()
