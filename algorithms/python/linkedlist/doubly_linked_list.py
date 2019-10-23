#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (c) 2019, Gianluca Fiore
#
###############################################################################

__author__ = "Gianluca Fiore"


class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    # Return the current Node's value
    def getData(self):
        return self.data

    # Set a new value for Node
    def setData(self, val):
        self.data = val


class DoublyLinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    # Get the current size of the list
    def getSize(self):
        return self.size

    # Insert a new Node in the list
    def insert(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            node.prev_node = self.tail
            self.tail.next_node = node
            self.tail = node
            self.size += 1

    # Remove a node from the list
    def remove(self, node):
        if self.head is None:
            # List empty, return false
            return False

        if node.data == self.head.data:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.size -= 1
            else:
                self.head = self.head.next_node
                self.head.prev_node = None
                self.size -= 1
            return True

        curr = self.head.next_node
        while curr is not None and node.data is not curr.data:
            curr = curr.next_node

        if curr == self.tail:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            self.size -= 1
            return True
        elif curr is not None:
            curr.prev_node.next_node = curr.next_node
            curr.next_node.prev_node = curr.prev_node
            self.size -= 1
            return True
        else:
            return False

    # Print all values of nodes in the list
    def printList(self):
        if self.head is None:
            print("Empty List")
            return

        print("List of %i nodes" % self.size)
        curr = self.head
        while curr:
            print(curr.getData())
            curr = curr.next_node

    # Reverse traversal of the list
    def reverseTraversal(self):
        curr = self.tail
        while curr is not None:
            yield curr.data
            curr = curr.prev_node


def main():
    ll = DoublyLinkedList()
    n1 = Node(12)
    n2 = Node(33)
    n3 = Node("ggg")
    ll.insert(n1)
    ll.insert(n2)
    ll.insert(n3)
    ll.printList()


if __name__ == '__main__':
    main()
