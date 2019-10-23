#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (c) 2019, Gianluca Fiore
#
###############################################################################

__author__ = "Gianluca Fiore"

import unittest
import linked_list


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = linked_list.LinkedList()
        self.node1 = linked_list.Node(33)
        self.node2 = linked_list.Node(8.9)
        self.node3 = linked_list.Node("abc")

    def test_new_node(self):
        self.assertIsInstance(self.node1, linked_list.Node)

    def test_new_list(self):
        self.assertIsInstance(self.list, linked_list.LinkedList)

    def test_insert(self):
        self.list.insert(self.node1)
        self.assertIsInstance(self.list.size, int)
        self.assertEqual(self.list.size, 1)
        self.assertEqual(self.list.head.data, 33)

    def test_value_not_contained(self):
        self.value_to_find = 44
        self.list.insert(self.node1)
        self.list.insert(self.node2)
        self.list.insert(self.node3)
        self.assertFalse(self.list.contains(self.value_to_find))

    def test_value_contained(self):
        self.value_to_find = 33
        self.list.insert(self.node1)
        self.list.insert(self.node2)
        self.list.insert(self.node3)
        self.assertTrue(self.list.contains(self.value_to_find))

    def test_remove(self):
        # start with head and then insert a few random nodes
        head = self.list.insert(linked_list.Node(1))
        for i in range(2, 5):
            self.list.insert(linked_list.Node(i))

        self.assertEqual(self.list.size, 4)
        self.node_to_remove = self.list.head.next_node
        self.list.remove(self.node_to_remove)
        self.assertEqual(self.list.size, 3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLinkedList)
    unittest.TextTestRunner(verbosity=2).run(suite)
