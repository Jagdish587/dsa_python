class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_end(self, data):
        new_node = Node(data)
        current_node = self.head

        # if there is no element in list
        if (self.head == None):
            self.head = new_node
        else:
            # reach to end node of list
            while(current_node.next):
                current_node = current_node.next
            current_node.next = new_node

    def return_middle_element(self):
        slow_ptr = self.head
        fast_ptr = self.head

        # fast_ptr reaches NULL for even nodes 
        # fast_ptr reaches last for odd nodes
        while(fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        return slow_ptr.data

    def print_elements(self):
        current_node = self.head

        while(current_node):
            print(current_node.data, end=" ")
            current_node = current_node.next

if __name__ == '__main__':
    # construct the linked list
    linked_list = LinkedList()
    linked_list.add_at_end(1)
    linked_list.add_at_end(2)
    linked_list.add_at_end(3)
    linked_list.add_at_end(4)
    linked_list.add_at_end(5)
    linked_list.add_at_end(6)
    linked_list.add_at_end(7)
    linked_list.add_at_end(8)
    linked_list.add_at_end(9)

    # print the elements in list
    linked_list.print_elements()

    middle_element = linked_list.return_middle_element()

    print("\nmiddle element = ", middle_element)

