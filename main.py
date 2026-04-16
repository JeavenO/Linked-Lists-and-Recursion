from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance
    ll = LinkedList()

    # 2) Insert some sample data
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_front(30)
    ll.insert_at_end(5)

    # 3) Display the list
    print("Initial list:")
    ll.print_list()

    # 4) Call recursive_sum and print the result
    total = ll.sum_list()
    print("\nSum of all IDs:", total)

    # 5) Call recursive_search with a target and print result
    target = 20
    print(f"\nSearch for {target}:", ll.search(target))

    target = 99
    print(f"Search for {target}:", ll.search(target))

    # 6) Call recursive_reverse, then display the reversed list
    ll.reverse()
    print("\nReversed list:")
    ll.print_list()