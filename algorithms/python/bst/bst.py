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

    # Search if the tree contains a given value
    def contains(self, root_node, value):
        if root_node is None:
            return False

        if root_node.data is value:
            return True
        elif value < root_node.data:
            return self.contains(root_node.left, value)
        else:
            return self.contains(root_node.right, value)

    # Find parent of a node in the tree
    def find_parent(self, root_node, value):
        if value is root_node.data:
            return None

        if value < root_node.data:
            if root_node.left is None:
                return None
            elif root_node.left.data is value:
                return root_node
            else:
                return self.find_parent(root_node.left, value)
        else:
            if root_node.right is None:
                return None
            elif root_node.right.data is value:
                return root_node
            else:
                return self.find_parent(root_node.right, value)

    # Find a node in the tree
    def find_node(self, root_node, value):
        if root_node is None:
            return None

        if root_node.data is value:
            return root_node
        elif value < root_node.data:
            return self.find_node(root_node.left, value)
        else:
            return self.find_node(root_node.right, value)

    # Remove a node from the tree
    def remove(self, value):
        node_to_remove = self.find_node(self.root, value)
        if node_to_remove is None:
            return False

        parent = self.find_parent(self.root, value)
        if self.root.left is None and self.root.right is None:
            self.root = None
            return True
        elif node_to_remove.left is None and node_to_remove.right is None:
            if node_to_remove.data < parent.data:
                parent.left = None
            else:
                parent.right = None
        elif node_to_remove.left is None and node_to_remove.right is not None:
            if node_to_remove.data < parent.data:
                parent.left = node_to_remove.right
            else:
                parent.right = node_to_remove.right
        elif node_to_remove.left is not None and node_to_remove.right is None:
            if node_to_remove.data < parent.data:
                parent.left = node_to_remove.left
            else:
                parent.right = node_to_remove.left
        else:
            largest_value = node_to_remove.left
            while largest_value is not None:
                # Find largest value in subtree of node_to_remove
                largest_value = largest_value.right
            self.find_parent(largest_value.data).right = None
            node_to_remove.data = largest_value.data

        return True

    # Find smallest value in the tree
    def find_min(self, root_node):
        current = root_node
        while current.left is not None:
            current = current.left
        return current.data

    # Find largest value in the tree
    def find_max(self, root_node):
        current = root_node
        while current.right is not None:
            current = current.right
        return current.data


def main():
    bst = BinarySearchTree()
    n1 = Node(33)
    n2 = Node(31)
    n3 = Node(45)
    n4 = Node(12)
    n5 = Node(666)
    bst.insert(n1)
    bst.insert(n2)
    bst.insert(n3)
    bst.insert(n4)
    bst.insert(n5)
    maxvalue = bst.find_max(bst.root)
    minvalue = bst.find_min(bst.root)
    print(maxvalue, minvalue)


if __name__ == '__main__':
   main()
