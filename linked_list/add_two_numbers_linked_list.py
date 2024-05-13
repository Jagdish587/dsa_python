class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.new_head = None

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

    def add_at_front_new_node(self, data):
        new_node = Node(data)

        if(self.new_head == None):
            self.new_head = new_node
        else:
            new_node.next = self.new_head
            self.new_head = new_node

    def print_elements(self, head_node):
        curent_node = head_node

        while(curent_node):
            print(curent_node.data, end=" ")
            curent_node = curent_node.next

    def reverse(self, head_node):
        current_node = head_node
        prev = None
        next_node = None

        while(current_node):
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        
        head_node = prev

        return head_node

    def add_two_linked_list(self, first_head, second_head):
        digit = 0
        carry = 0
        first_reversed = self.reverse(first_head)
        second_reversed = self.reverse(second_head)
    
        while(first_reversed and second_reversed):
            sum_value = first_reversed.data + second_reversed.data + carry
            digit = sum_value % 10
            carry = sum_value // 10

            # now create a new node
            self.add_at_front_new_node(digit)
            first_reversed = first_reversed.next            
            second_reversed = second_reversed.next

        if(carry):
            self.add_at_front_new_node(carry)
        print("\nresultant list\n")
        self.print_elements(self.new_head)


if __name__ == '__main__':
    linked_list_first = LinkedList()
    linked_list_first.add_at_end(7)
    linked_list_first.add_at_end(5)
    linked_list_first.add_at_end(9)
    linked_list_first.print_elements(linked_list_first.head)
    print()
    linked_list_second = LinkedList()
    linked_list_second.add_at_end(7)
    linked_list_second.add_at_end(2)
    linked_list_second.add_at_end(9)
    linked_list_second.print_elements(linked_list_second.head)

    linked_list_first.add_two_linked_list(linked_list_first.head, linked_list_second.head)

