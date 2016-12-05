#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """
        Initialize this linked list; append the given items, if any
        Best case: Om(1) list is initialized empty
        Worst case: O(n) list is initialized with items
        """
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """
        Return a string representation of this linked list
        Best case: Om(1) same as as_list
        Worst case: O(n) same as as_list
        """
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """
        Return a list of all items in this linked list
        Best case: Om(1) list is empty or only 1 element
        Worst case: O(n) list is not empty
        """
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def map(self, quality):
        """
        Perform an action on all elements in the linked list
        Best case: Om(1) list is empty or only 1 element
        Worst case: O(n) list is not empty
        """
        current = self.head
        while current is not None:
            quality(current.data)
            current = current.next

    def is_empty(self):
        """
        Return True if this linked list is empty, or False
        Best case: Om(1) list is empty
        Worst case: O(1) list is not empty
        """
        return self.head is None

    def length(self):
        """
        Return the length of this linked list by traversing its nodes
        Best case: Om(1) list is empty or only 1 element
        Worst case: O(n) list is not empty
        """
        # TODO: count number of items
        node_count = 0
        # edge case - check if empty
        if self.head is not None:
            current_node = self.head
            # if the current node isn't empty, add one and go to next
            while current_node is not None:
                node_count += 1
                current_node = current_node.next
            # else:
        return node_count

    def append(self, item):
        """
        Insert the given item at the tail of this linked list
        Best case: Om(1) list is empty
        Worst case: O(1) list has to append
        """
        # TODO: append given item
        new_node = Node(item)

        # check if there is a head, if not add it
        if self.head is None:
            self.head = new_node
        # check if there is a tail, if not add it
        if self.tail is None:
            self.tail = new_node
        # if there is a tail, add it to the end
        else:
            # set current tail's next to the new node
            self.tail.next = new_node
            # then override current tail to be the new node
            self.tail = new_node

    def prepend(self, item):
        """
        Insert the given item at the head of this linked list
        Best case: Om(1) list is empty
        Worst case: O(1) list has to prepend
        """
        # TODO: prepend given item
        new_node = Node(item)

        # check if there is a tail, if not add it
        if self.tail is None:
            self.tail = new_node
        # check if there is a head, if not add it
        if self.head is None:
            self.head = new_node
        else:
            # make new node's next pointer the current head
            new_node.next = self.head
            # then override current head to be the new node
            self.head = new_node

    def delete(self, item):
        """
        Delete the given item from this linked list, or raise ValueError
        Best case: Om(1) item is at the head of list
        Worst case: O(n) item not present or at end
        """
        # TODO: find given item and delete if found

        # edge case - check if empty
        if self.head is not None:
            current_node = self.head
            # edge case - check front of line: one time check to "delete" first item
            if current_node.data is item:
                # edge case - if also only item in array
                if current_node.next is None:
                    self.head = None
                    self.tail = None
                else:
                    new_head = current_node.next
                    # remove reference to the next node so this node can be garbage collected when "deleted"
                    current_node.next = None
                    # set current_node's next to no longer be the "deleted" node and be the node after
                    self.head = new_head

            while current_node is not None and current_node.next is not None:
                # check if the next node's data matches
                if current_node.next.data is item:
                    # edge case - for end of line: save the node if the node after next isn't empty
                    if current_node.next.next is not None:
                        new_next_node = current_node.next.next
                        # remove reference to the next node so this node can be garbage collected when "deleted"
                        current_node.next.next = None
                        # set current_node's next to no longer be the "deleted" node and be the node after
                        current_node.next = new_next_node
                    # there is no node after next, so just "delete" the reference to it now
                    else:
                        current_node.next = None
                        # set current node to tail
                        self.tail = current_node
                # item not found in next node and the node after doesn't exist, so return error becuase it's end of list
                elif current_node.next.next is None:
                    raise ValueError('Linked List does not contain %i.' % (item))

                current_node = current_node.next
        # empty, so return error
        else:
            raise ValueError('Linked List is empty.')

    def deleteByKey(self, key):
        """
        Delete the given item by key from this linked list, or raise ValueError
        Specific to hashtable implementation for best speed
        Best case: Om(1) item is at the head of list
        Worst case: O(n) item not present or at end
        """
        # TODO: find given item and delete if found

        # edge case - check if empty
        if self.head is not None:
            current_node = self.head
            # edge case - check front of line: one time check to "delete" first item
            if current_node.data[0] is key:
                # edge case - if also only key in array
                if current_node.next is None:
                    self.head = None
                    self.tail = None
                else:
                    new_head = current_node.next
                    # remove reference to the next node so this node can be garbage collected when "deleted"
                    current_node.next = None
                    # set current_node's next to no longer be the "deleted" node and be the node after
                    self.head = new_head

            while current_node is not None and current_node.next is not None:
                # check if the next node's data matches
                if current_node.next.data[0] is key:
                    # edge case - for end of line: save the node if the node after next isn't empty
                    if current_node.next.next is not None:
                        new_next_node = current_node.next.next
                        # remove reference to the next node so this node can be garbage collected when "deleted"
                        current_node.next.next = None
                        # set current_node's next to no longer be the "deleted" node and be the node after
                        current_node.next = new_next_node
                    # there is no node after next, so just "delete" the reference to it now
                    else:
                        current_node.next = None
                        # set current node to tail
                        self.tail = current_node
                # key not found in next node and the node after doesn't exist, so return error becuase it's end of list
                elif current_node.next.next is None:
                    raise KeyError('Linked List does not contain %i.' % (key))

                current_node = current_node.next
        # empty, so return error
        else:
            raise KeyError('Linked List is empty.')

    def find(self, quality):
        """
        Return an item from this linked list satisfying the given quality
        Best case: Om(1) item is at the head of list
        Worst case: O(n) item not present or at end
        """
        # TODO: find item where quality(item) is True
        # edge case - check if empty
        if self.head is not None:
            current_node = self.head
            # if the current node isn't empty, add one and go to next
            while current_node is not None:
                # if true, return the data
                if quality(current_node.data) is True:
                    print(current_node.data)
                    return current_node.data
                current_node = current_node.next
        else:
            return None


def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())

    ll.delete('A')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()
