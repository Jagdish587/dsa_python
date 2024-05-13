class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.even_head = None
        self.even_end = None
        self.odd_head = None
        self.odd_end = None

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


    def add_at_even_end(self, even_node):
        # if there is no element in list
        if (self.even_head == None):
            self.even_head = even_node
            self.even_end = even_node
        else:
            # reach to end node of even list
            self.even_end.next = even_node
            self.even_end = self.even_end.next


    def add_at_odd_end(self, odd_node):
        # if there is no element in list
        if (self.odd_head == None):
            self.odd_head = odd_node
            self.odd_end = odd_node
        else:
            # reach to end node of odd list
            self.odd_end.next = odd_node
            self.odd_end = self.odd_end.next

    def segregate_even_odd_nodes(self):
        current_node = self.head

        print()
        while(current_node):
            if(current_node.data % 2):
                self.add_at_odd_end(current_node)
            else:
                self.add_at_even_end(current_node)
            current_node =  current_node.next
        
        self.odd_end.next= None
        self.even_end.next = self.odd_head
        self.head = self.even_head

if __name__ == '__main__':
    # construct the linked list
    linked_list = LinkedList()
    linked_list.add_at_end(17)
    linked_list.add_at_end(15)
    linked_list.add_at_end(8)
    linked_list.add_at_end(12)
    linked_list.add_at_end(10)
    linked_list.add_at_end(5)
    linked_list.add_at_end(4)
    linked_list.add_at_end(1)
    linked_list.add_at_end(7)
    linked_list.add_at_end(6)
    # print the elements in list
    linked_list.print_elements()
    linked_list.segregate_even_odd_nodes()
    print()
    linked_list.print_elements()


    # 17->15->8->12->10->5->4->1->7->6->NULL