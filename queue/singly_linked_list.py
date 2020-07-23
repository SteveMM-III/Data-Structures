class Node:
    def __init__( self, value ):
        self.value = value
        self.next = None

    def get_value( self ):
        return self.value

    def get_next( self ):
        return self.next

    def set_next( self, new_next ):
        self.next = new_next


class LinkedList:
    def __init__( self ):
        self.head = None
        self.tail = None

    def add_to_head( self, value ):
        # create a new node
        new_node = Node( value )

        # if list empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # list not empty
        new_node.set_next( self.head )
        self.head = new_node

    
    def add_to_tail( self, value ):
        # create a new node
        new_node = Node( value )

        # if list empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # list not empty
        else:
            self.tail.set_next( new_node )
            self.tail = new_node
    
    def remove_head( self ):
        # if list empty
        if not self.head:
            return None
        # head has no next
        elif not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        # list with next
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value

    def remove_tail( self ):
        # if list empty
        if not self.head:
            return None
        # head has no next
        elif not self.head.get_next():
            tail = self.tail
            self.head = None
            self.tail = None
            return tail.get_value()
        # list with next
        else:
            prev = self.head
            curr = prev
            while curr.get_next():
                prev = curr
                curr = curr.get_next()
                if curr == self.tail:
                    prev.set_next( None )
                    self.tail = prev
                    return curr.get_value()
            

    def contains( self, value ):
        # if list empty
        if not self.head:
            return False
        # check for value
        else:
            test_node = self.head
            while test_node:
                if test_node.get_value() == value:
                    return True
                test_node = test_node.get_next()
            return False

    def get_max( self ):
        # if list empty
        if not self.head:
            return None
        # check values
        else:
            nxt = self.head
            mx  = 0

            while nxt:
                test = nxt.get_value()
                if test > mx:
                    mx = test
                nxt = nxt.get_next()
            return mx
