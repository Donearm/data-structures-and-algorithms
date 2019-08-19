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

class LinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class DoublyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
