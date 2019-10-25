#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (c) 2019, Gianluca Fiore
#
###############################################################################

__author__ = "Gianluca Fiore"


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    # Iterate over the tree to count the size of it
    def count_size(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.count_size(root.left) + self.count_size(root.right)

    # Call count_size to get the total size of the tree
    def get_size(self):
        return self.count_size(self.root)

    # Insert a new node
    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            # Call insert_node() to find the correct place in tree for the new value
            self.insert_node(self.root, node)

    def insert_node(self, current_node, new_node):
        if new_node.data < current_node.data:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self.insert_node(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self.insert_node(current_node.right, new_node)


def main():
    bst = BinarySearchTree()
    n1 = Node(33)
    n2 = Node(31)
    n3 = Node(45)
    bst.insert(n1)
    bst.insert(n2)
    bst.insert(n3)
    print(bst.root.data)
    print(bst.root.left.data)
    print(bst.root.right.data)

if __name__ == '__main__':
   main()
