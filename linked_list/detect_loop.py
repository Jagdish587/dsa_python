# let's construct a node class first
class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

# class for linked list
class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_end(self, data):
        new_node = Node(data)
        # if list is empty
        if self.head is None:
            self.head = new_node
        else:
            # if list is not empty
            current_node = self.head
            while(current_node.next != None):
                current_node = current_node.next
            current_node.next = new_node
    
    def create_loop(self):
        current_node = self.head

        while(current_node.next != None):
            current_node = current_node.next
        print(current_node.data)

        current_node.next = self.head.next.next
        print()
        print(current_node.next.data)
    
    def detect_loop(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while (slow_ptr and fast_ptr and fast_ptr!= None):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if (slow_ptr == fast_ptr):
                print("detected loop")
                return 1
        return 0

    def print_elements_list(self):
        # print all elements in linked list
        current_node = self.head
        while(current_node != None):
            print(current_node.data, end=" ")
            current_node = current_node.next        




if __name__ == '__main__':
    # add elements at end
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
    
    linked_list.print_elements_list()
    print()
    linked_list.create_loop()
    print(linked_list.detect_loop())