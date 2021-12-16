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

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, data):
        if not prev_node:
            print("Node does not exist")

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_by_value(self, value):
        curr_node = self.head

        if curr_node and curr_node.data == value:
            self.head = curr_node.next
            curr_node = None
        else:
            prev_node = None

            while curr_node and curr_node.data != value:
                prev_node = curr_node
                curr_node = curr_node.next

            if curr_node is None:
                return

            prev_node.next = curr_node.next
            curr_node = None

    def delete_by_key(self, key):
        if self.head:
            curr_node = self.head
            if key == 0:
                self.head = curr_node.next
                curr_node = None
            else:
                prev_node = None
                check = 0

                while curr_node and check != key:
                    prev_node = curr_node
                    curr_node = curr_node.next
                    check += 1

                if curr_node is None:
                    return

                prev_node.next = curr_node.next

                curr_node = None

    def length(self):
        l = 0
        node = self.head
        while node:
            l += 1
            node = node.next
        print(l)

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, node_1, node_2):
        if node_1 == node_2:
            return

        curr_node = self.head
        prev_node = None
        while curr_node and node_1 != curr_node.data:
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node == None:
            return

        curr_node_2 = self.head
        prev_node_2 = None
        while curr_node_2 and node_2 != curr_node_2.data:
            prev_node_2 = curr_node_2
            curr_node_2 = curr_node_2.next

        if curr_node_2 == None:
            return

        if prev_node is None:
            self.head = curr_node_2
        else:
            prev_node.next = curr_node_2
        # curr_node_2.next = curr_node.next

        if prev_node_2 is None:
            self.head = curr_node
        else:
            prev_node_2.next = curr_node
        # curr_node.next = curr_node_2.next

        curr_node.next, curr_node_2.next = curr_node_2.next, curr_node.next

    def print(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


linked_list = LinkedList()
linked_list.append("Alpha")
linked_list.append("Beta")
linked_list.append("Gamma")
linked_list.prepend("Algo")
linked_list.insert(linked_list.head.next, "Foxtrot")
linked_list.delete_by_value("Gamma")
linked_list.append("Gamma2")
linked_list.swap_nodes("Beta", "Gamma2")

linked_list.print()
