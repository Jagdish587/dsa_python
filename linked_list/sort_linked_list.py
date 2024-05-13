class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_elements(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end=" ")
            current_node = current_node.next

    def add_at_end(self, data):
        new_node = Node(data)
        if(self.head == None):
            self.head = new_node
        else:
            current_node = self.head
            while(current_node.next):
                current_node = current_node.next
            current_node.next = new_node

    def sort_linked_list(self):
        current_node = self.head

        while(current_node.next):
            next_node = current_node.next
            while(next_node):
                if (current_node.data > next_node.data):
                    current_node.data,next_node.data = next_node.data,current_node.data
                next_node = next_node.next
            current_node = current_node.next

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_at_end(1)
    linked_list.add_at_end(9)
    linked_list.add_at_end(2)
    linked_list.add_at_end(8)
    linked_list.add_at_end(3)
    linked_list.add_at_end(7)
    linked_list.add_at_end(4)
    linked_list.print_elements()
    linked_list.sort_linked_list()
    print()
    linked_list.print_elements()


