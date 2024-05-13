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

    def reverse_linked_list(self):
        current_node = self.head
        prev_node = None

        while(current_node != None):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
    
        self.head = prev_node


    def reverse(self, head):
    
        # If head is empty or has reached the list end
        if head is None or head.next is None:
            return head

        # Reverse the new_head list
        new_head = self.reverse(head.next)

        # Put first element at the end
        head.next.next = head
        head.next = None

        # Fix the header pointer
        return new_head

    def reverse_linked_list_recursion(self):
        self.head = self.reverse(self.head)

if __name__ == '__main__':
    # add elements at end
    linked_list = LinkedList()
    linked_list.add_at_end(1)
    linked_list.add_at_end(3)
    linked_list.add_at_end(5)
    linked_list.add_at_end(7)
    linked_list.add_at_end(11)
    linked_list.add_at_end(13)
    # 3-5>7->11
    linked_list.print_elements_list()

    linked_list.reverse_linked_list_recursion()
    print()
    linked_list.print_elements_list()
