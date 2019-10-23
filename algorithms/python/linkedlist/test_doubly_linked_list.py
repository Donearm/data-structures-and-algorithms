#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (c) 2019, Gianluca Fiore
#
###############################################################################

__author__ = "Gianluca Fiore"


import unittest
import doubly_linked_list


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = doubly_linked_list.DoublyLinkedList()
        self.node1 = doubly_linked_list.Node(41)
        self.node2 = doubly_linked_list.Node(55.6)
        self.node3 = doubly_linked_list.Node("rar")

    def test_new_node(self):
        self.assertIsInstance(self.node1, doubly_linked_list.Node)

    def test_new_list(self):
        self.assertIsInstance(self.list, doubly_linked_list.DoublyLinkedList)

    def test_insert(self):
        self.list.insert(self.node1)
        self.assertIsInstance(self.list.size, int)
        self.assertEqual(self.list.size, 1)
        self.assertEqual(self.list.head.data, 41)

    def test_remove(self):
        head = self.list.insert(doubly_linked_list.Node(1))
        for i in range(2, 5):
            self.list.insert(doubly_linked_list.Node(i))

        self.assertEqual(self.list.size, 4)
        self.node_to_remove = self.list.head.next_node
        self.list.remove(self.node_to_remove)
        self.assertEqual(self.list.size, 3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDoublyLinkedList)
    unittest.TextTestRunner(verbosity=2).run(suite)
