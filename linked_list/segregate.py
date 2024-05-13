class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.zero_head = None
        self.zero_end = None
        self.one_head = None
        self.one_end = None
        self.two_head = None
        self.two_end = None

    def print_elements(self):
        current_node = self.head

        while(current_node):
            print(current_node.data, end=" ")
            current_node = current_node.next

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


    def add_at_zero_list(self, zero_node):
        # if there is no element in list
        if (self.zero_head == None):
            self.zero_head = zero_node
            self.zero_end = zero_node
        else:
            # reach to end node of zero list
            self.zero_end.next = zero_node
            self.zero_end = self.zero_end.next

    def add_at_one_list(self, one_node):
        # if there is no element in list
        if (self.one_head == None):
            self.one_head = one_node
            self.one_end = one_node
        else:
            # reach to end node of zero list
            self.one_end.next = one_node
            self.one_end = self.one_end.next

    def add_at_two_list(self, two_node):
        # if there is no element in list
        if (self.two_head == None):
            self.two_head = two_node
            self.two_end = two_node
        else:
            # reach to end node of zero list
            self.two_end.next = two_node
            self.two_end = self.two_end.next

    def segregate_nodes(self):
        current_node = self.head

        while(current_node):
            if(current_node.data == 0):
                self.add_at_zero_list(current_node)
            elif(current_node.data == 1):
                self.add_at_one_list(current_node)
            else:
                self.add_at_two_list(current_node)
            current_node =  current_node.next
        
        self.zero_end.next = self.one_head
        self.one_end.next = self.two_head
        self.two_end.next = None
        self.head = self.zero_head

if __name__ == '__main__':
    # construct the linked list
    linked_list = LinkedList()
    linked_list.add_at_end(1)
    linked_list.add_at_end(0)
    linked_list.add_at_end(1)
    linked_list.add_at_end(2)
    linked_list.add_at_end(0)
    linked_list.add_at_end(1)
    linked_list.add_at_end(2)
    linked_list.add_at_end(0)
    linked_list.add_at_end(1)
    linked_list.add_at_end(2)
    linked_list.add_at_end(0)
    # print the elements in list
    linked_list.print_elements()
    linked_list.segregate_nodes()
    print()
    linked_list.print_elements()


    # 17->15->8->12->10->5->4->1->7->6->NULL