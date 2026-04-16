class Node:
    """A single node in the linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked List with recursive operations"""
    def __init__(self):
        self.head = None

    # --------------------------
    # INSERT METHODS
    # --------------------------
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # --------------------------
    # RECURSIVE SUM (TEST EXPECTS THIS NAME)
    # --------------------------
    def recursive_sum(self):
        return self._sum_recursive(self.head)

    def _sum_recursive(self, node):
        if node is None:
            return 0
        return node.data + self._sum_recursive(node.next)

    # --------------------------
    # RECURSIVE SEARCH (TEST EXPECTS THIS NAME)
    # --------------------------
    def recursive_search(self, target):
        return self._search_recursive(self.head, target)

    def _search_recursive(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        return self._search_recursive(node.next, target)

    # --------------------------
    # RECURSIVE REVERSE (THIS FIXES YOUR ERROR)
    # --------------------------
    def recursive_reverse(self):
        self.head = self._reverse_recursive(self.head)

    def _reverse_recursive(self, node):
        if node is None or node.next is None:
            return node

        new_head = self._reverse_recursive(node.next)

        node.next.next = node
        node.next = None

        return new_head

    # --------------------------
    # PRINT LIST
    # --------------------------
    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")