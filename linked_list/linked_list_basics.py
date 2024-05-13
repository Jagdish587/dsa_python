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

    def add_at_front(self, data):
        new_node = Node(data)
        # if list is empty
        if self.head == None:
            self.head =  new_node
        else:
            # if list is not empty, we need to add emlement at front
            new_node.next = self.head
            self.head = new_node
    
    def add_at_postion(self, index, data):
        current_index = 1
        new_node = Node(data)
        current_node = self.head
        if index == 1:
            new_node.next = self.head
            self.head = new_node
        else:    
            while(current_index != index):
                current_index = current_index + 1
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node

    def print_elements_list(self):
        # print all elements in linked list
        current_node = self.head
        while(current_node != None):
            print(current_node.data, end=" ")
            current_node = current_node.next        

    def delete_node(self, index):
        current_index = 1
        current_node = self.head

        if index == 1:
            self.head = self.head.next
        else:
            while(current_index != index-1):
                current_index = current_index + 1
                current_node = current_node.next
            if current_node.next.next == None:
                current_node.next = None
            else :
                current_node.next = current_node.next.next

    def reverse_linked_list(self):
        current_node = self.head
        prev_node = None

        while(current_node != None):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
    
        self.head = prev_node

if __name__ == '__main__':
    # add elements at end
    linked_list = LinkedList()
    linked_list.add_at_end(3)
    linked_list.add_at_end(5)
    linked_list.add_at_end(7)
    linked_list.add_at_end(11)
    # 3-5>7->11
    linked_list.print_elements_list()
    # add elements at front
    linked_list.add_at_front(1)
    linked_list.add_at_front(33)
    # 33->1->3-5>7->11
    print()
    linked_list.print_elements_list()
    linked_list.delete_node(5)
    print()
    # 33->1->3-5->11
    linked_list.print_elements_list()
    print()
    # add at position
    linked_list.add_at_postion(4, 4)
    # 33->1->3-4->5->11
    linked_list.print_elements_list()
    print()
    # reverse a linked list
    linked_list.reverse_linked_list()
    # 11->5->4->3->1->33
    linked_list.print_elements_list()
