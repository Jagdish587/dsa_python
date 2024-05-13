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
    

    def return_middle_node(self):
        slow_ptr = self.head
        fast_ptr = self.head

        # fast_ptr reaches NULL for even nodes 
        # fast_ptr reaches last for odd nodes
        while(fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        return slow_ptr
    
    def reverse_nodes(self, new_head):
        prev = None
        current_node = new_head

        while(current_node):
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        new_head = prev

        return new_head


    def is_palindrome(self):
        """
        Step 1 : find middle of linked list
        Step 2:  from next of middle element , reverse rest of entire linked list
        Step 3:  from next of middle node , reach to end of list and compare 
                 first node data to second node data
        """

        middle_node = self.return_middle_node()
        middle_node.next = self.reverse_nodes(middle_node.next)
        first_node = self.head
        second_node = middle_node.next

        while(second_node):
            if (first_node.data != second_node.data):
                return False
            first_node = first_node.next
            second_node = second_node.next

        # let's keep original links 
        middle_node.next = self.reverse_nodes(middle_node.next)
        return True

    def print_elements(self):
        current_node = self.head

        while(current_node):
            print(current_node.data, end=" ")
            current_node = current_node.next

if __name__ == '__main__':
    # construct the linked list
    linked_list = LinkedList()
    linked_list.add_at_end('r')
    linked_list.add_at_end('a')
    linked_list.add_at_end('c')
    linked_list.add_at_end('e')
    linked_list.add_at_end('c')
    linked_list.add_at_end('a')
    linked_list.add_at_end('r')

    # print the elements in list
    linked_list.print_elements()

    middle_element = linked_list.return_middle_element()

    print("\nmiddle element = ", middle_element)

    ret = linked_list.is_palindrome()
    print("is plaindrome = ",ret)


