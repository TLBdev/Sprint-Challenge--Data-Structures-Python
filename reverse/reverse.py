class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        if node is None:
            return
        if node.next_node is None:
            self.head = node
            node.next_node = prev
            return
        
        pointer = node.next_node
        node.next_node = prev
        self.reverse_list(pointer, node)
        
           
        
    #     if head.next == None:
    #     return
    # first = head
    # second = head.next
    # first.next = None
    # while second != None:
    #     pointer = second.next
    #     second.next = first
    #     first = second
    #     second = pointer
test = LinkedList()
test.add_to_head(1)

test.add_to_head(2)

test.add_to_head(3)

test.add_to_head(4)

test.add_to_head(5)
test.reverse_list(test.head, None)
node = test.head
while node:
    print(node.value)
    node = node.next_node
# 5 > 4 > 3 > 2 > 1  (5, None)
# pointer = 4
# 5.next = None
# None < 5 4 > 3 > 2 > 1 (4, 5)
# pointer = 3
# 4.next = 5
# None < 5 < 4  3 > 2 > 1 (3, 4)
# pointer = 2
# 3.next = 4
# None < 5 < 4 < 3  2 > 1 (2, 3)