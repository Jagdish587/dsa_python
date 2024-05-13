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
    
    def print_elements_list(self):
        # print all elements in linked list
        current_node = self.head
        while(current_node != None):
            print(current_node.data, end=" ")
            current_node = current_node.next        

    def add_helper(self, node):

        if(node == None):
            return 1
        carry = self.add_helper(node.next)
        node.data = node.data + carry
        if(node.data < 10):
            carry = 0
        else:
            node.data = 0
            carry = 1
        return carry


    def add_one_linked_list(self):

        carry = self.add_helper(self.head)
        if (carry == 1):
            new_node = Node(1)
            new_node.next = self.head
            self.head = new_node

if __name__ == '__main__':
    # add elements at end
    linked_list = LinkedList()
    linked_list.add_at_end(9)
    linked_list.add_at_end(9)
    linked_list.add_at_end(9)
    # 1->5>9
    linked_list.print_elements_list()
    linked_list.add_one_linked_list()
    print()
    linked_list.print_elements_list()