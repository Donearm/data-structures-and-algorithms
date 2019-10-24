package main

////////////////////////////////////////////////////////////////////////////////
// Copyright (c) 2019, Gianluca Fiore
//
//    This program is free software: you can redistribute it and/or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation, either version 3 of the License, or
//    (at your option) any later version.
//
////////////////////////////////////////////////////////////////////////////////

import (
	"fmt"
)

type Node struct {
	data      interface{}
	next_node *Node
	prev_node *Node
}

type DoublyLinkedList struct {
	head *Node
	tail *Node
	size int
}

func newNode(val interface{}) *Node {
	return &Node{val, nil, nil}
}

func (n *Node) getData() interface{} {
	return n.data
}

func (n *Node) setData(val interface{}) {
	n.data = val
}

func newDoublyLinkedList() *DoublyLinkedList {
	return &DoublyLinkedList{nil, nil, 0}
}

func (dl *DoublyLinkedList) getSize() int {
	return dl.size
}

func (dl *DoublyLinkedList) printList() {
	if dl.head == nil {
		fmt.Println("Empty List")
		return
	}

	fmt.Printf("List of %d\n", dl.size)
	curr := dl.head
	for {
		fmt.Println(curr.getData())
		curr = curr.next_node
		if curr == nil {
			break
		}
	}
}

func (dl *DoublyLinkedList) insert(n *Node) {
	if dl.head == nil {
		dl.head = n
		dl.tail = n
	} else {
		n.prev_node = dl.tail
		dl.tail.next_node = n
	}

	dl.tail = n
	dl.size += 1
}

func (dl *DoublyLinkedList) contains(v interface{}) bool {
	curr := dl.head
	for curr != nil {
		if curr.getData() == v {
			fmt.Println("Value is present")
			return true
		}
		curr = curr.next_node
	}
	fmt.Println("Value is absent")
	return false
}

func (dl *DoublyLinkedList) remove(n *Node) bool {
	if dl.head == nil {
		// List empty, return false
		return false
	}

	if n.data == dl.head.data {
		if dl.head == dl.tail {
			dl.head = nil
			dl.tail = nil
			dl.size -= 1
		} else {
			dl.head = dl.head.next_node
			dl.head.prev_node = nil
			dl.size -= 1
		}
		return true
	}

	curr := dl.head.next_node
	for curr != nil && n.data != curr.data {
		curr = curr.next_node
	}

	if curr == dl.tail {
		dl.tail = dl.tail.prev_node
		dl.tail.next_node = nil
		dl.size -= 1
		return true
	} else if curr != nil {
		curr.prev_node.next_node = curr.next_node
		curr.next_node.prev_node = curr.prev_node
		dl.size -= 1
		return true
	} else {
		return false
	}
}

func (dl *DoublyLinkedList) reverseTraversal() []interface{} {
	var y []interface{}
	curr := dl.tail
	for curr != nil {
		y = append(y, curr.data)
		curr = curr.prev_node
	}
	return y
}

func main() {
	dl := newDoublyLinkedList()
	fmt.Println(dl.size)
	n1 := newNode(43)
	n2 := newNode(55)
	n3 := newNode("65")

	dl.insert(n1)
	dl.insert(n2)
	dl.insert(n3)
	dl.printList()
}
