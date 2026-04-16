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
        """Insert a new node at the beginning (O(1))"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end (O(n))"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # --------------------------
    # RECURSIVE SUM
    # --------------------------
    def sum_list(self):
        """Public method to start recursion"""
        return self._sum_recursive(self.head)

    def _sum_recursive(self, node):
        """
        Base case: if node is None → return 0
        Recursive case: node.data + sum of rest
        """
        if node is None:
            return 0
        return node.data + self._sum_recursive(node.next)

    # --------------------------
    # RECURSIVE SEARCH
    # --------------------------
    def search(self, target):
        """Public method"""
        return self._search_recursive(self.head, target)

    def _search_recursive(self, node, target):
        """
        Base case:
            - node is None → False
            - node.data == target → True
        Recursive case:
            search in next node
        """
        if node is None:
            return False
        if node.data == target:
            return True
        return self._search_recursive(node.next, target)

    # --------------------------
    # RECURSIVE REVERSE
    # --------------------------
    def reverse(self):
        """Reverse the linked list in-place"""
        self.head = self._reverse_recursive(self.head)

    def _reverse_recursive(self, node):
        """
        Base case:
            - empty list OR last node → return node
        Recursive case:
            reverse rest and fix pointers
        """
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
        """Print list in readable format"""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")


# --------------------------
# MAIN / TESTING
# --------------------------
if __name__ == "__main__":
    ll = LinkedList()

    # Insert sample data
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_front(30)
    ll.insert_at_end(5)

    print("Initial list:")
    ll.print_list()

    # Sum
    print("\nSum of all IDs:", ll.sum_list())

    # Search
    print("\nSearch for 20:", ll.search(20))
    print("Search for 99:", ll.search(99))

    # Reverse
    ll.reverse()
    print("\nReversed list:")
    ll.print_list()