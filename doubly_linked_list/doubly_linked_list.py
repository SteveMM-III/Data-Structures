"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""

class ListNode:
    def __init__(self, value, prev=None, nxt=None):
        self.prev  = prev
        self.value = value
        self.next  = nxt

    def delete( self ):
        # if the node being deleted has a previous node
        # set the previous node's next = to the node being delted's next
        if self.prev:
            self.prev.next = self.next
        # if the node being deleted has a next node
        # set the next node's prev = to the node being deleted's prev
        if self.next:
            self.next.prev = self.prev
        # del---v
        # 2 <-> 1 <-> 3
        # |<___>|<___>|
        # |<_________>|

            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
         # create a new node
        new_node = ListNode( value )

        # if list empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # list not empty
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return None
        else:
            val = self.head.value
            self.delete( self.head )
            return val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create a new node
        new_node = ListNode( value )

        # if list empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        # list not empty
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.tail:
            return None
        else:
            val = self.tail.value
            self.delete( self.tail )
            return val

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        val = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            self.delete( node )
        self.add_to_head( val )
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        val = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            self.delete( node )
        self.add_to_tail( val )

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node is self.tail:
            if self.tail.prev:
                temp = self.tail.prev
                self.tail.delete()
                self.tail = temp
            else:
                self.tail.delete()
                self.head = None
                self.tail = None
        elif node is self.head:
            if self.head.next:
                temp = self.head.next
                self.head.delete()
                self.head = temp
            else:
                self.head.delete()
                self.head = None
                self.tail = None
        else:
            node.delete()

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # if list empty
        if not self.head:
            return None
        # check values
        else:
            nxt = self.head
            mx  = nxt.value

            while nxt:
                test = nxt.value
                if test > mx:
                    mx = test
                nxt = nxt.next
            return mx
