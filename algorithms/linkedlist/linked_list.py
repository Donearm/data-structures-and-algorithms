#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (c) 2019, Gianluca Fiore
#
###############################################################################

__author__ = "Gianluca Fiore"

# Big Oh on Linked Lists:
# Insertion = O(1) if the node to be inserted is the head or tail, otherwise it's O(n)
# Deletion = O(n)
# Searching = O(n)

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    # Return the current Node's value
    def getData(self):
        return self.data

    # Set a new value for Node
    def setData(self, val):
        self.data = val

class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    # Print all values of nodes in the list
    def printList(self):
        if self.head == None:
            print("Empty List")
            return

        print("List of %i nodes" % self.size)
        curr = self.head
        while curr:
            print(curr.getData())
            curr = curr.next_node

    # Get the current size of the list
    def getSize(self):
        return self.size

    # Insert a new Node in the list
    def insert(self, node):
        if self.head == None:
            self.head = node
        else:
            self.tail.next_node = node

        self.tail = node
        self.size += 1

    # Check if a value is present in the list or not
    def contains(self, value):
        n = self.head
        while n:
            if n.getData() == value:
                print("Value is present")
                return True
            n = n.next_node

        print("Value is absent")
        return False

def main():
    # Test functionalities
    l = LinkedList()
    new_node = Node(13)
    second_node = Node("abc")
    third_node = Node(8.4)

    l.insert(new_node)
    l.insert(second_node)
    l.insert(third_node)
    l.printList()
    l.contains("abc")

if __name__ == '__main__':
    main()
