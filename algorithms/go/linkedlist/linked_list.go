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
}

type LinkedList struct {
	head *Node
	tail *Node
	size int
}

func newNode(val interface{}) *Node {
	return &Node{val, nil}
}

func (n *Node) getData() interface{} {
	return n.data
}

func (n *Node) setData(val interface{}) {
	n.data = val
}

func newLinkedList() *LinkedList {
	return &LinkedList{nil, nil, 0}
}

func (ll *LinkedList) getSize() int {
	return ll.size
}

func (ll *LinkedList) printList() {
	if ll.head == nil {
		fmt.Println("Empty List")
		return
	}

	fmt.Printf("List of %d\n", ll.size)
	curr := ll.head
	for {
		fmt.Println(curr.getData())
		curr = curr.next_node
		if curr == nil {
			break
		}
	}
}

func (ll *LinkedList) insert(n *Node) {
	if ll.head == nil {
		ll.head = n
	} else {
		ll.tail.next_node = n
	}

	ll.tail = n
	ll.size += 1
}

func (ll *LinkedList) traverse() []interface{} {
	var y []interface{}
	n := ll.head
	for {
		y = append(y, n.getData())
		n = n.next_node
		if n == nil {
			break
		}
	}

	return y
}

func (ll *LinkedList) reverseTraverse() []interface{} {
	var y []interface{}
	var curr, prev *Node
	if ll.tail != nil {
		curr = ll.tail
		for curr != ll.head {
			prev = ll.head
			for prev.next_node != curr {
				prev = prev.next_node
			}
			y = append(y, curr.data)
			curr = prev
		}
		y = append(y, curr.data)
		return y
	} else {
		y = append(y, ll.head.data)
		return y
	}
}

func (ll *LinkedList) contains(v interface{}) bool {
	curr := ll.head
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

func (ll *LinkedList) remove(n *Node) bool {
	var curr *Node
	if ll.head == nil {
		// Empty list
		return false
	}
	curr = ll.head
	if curr.data == n.data {
		if ll.head == ll.tail {
			// there's only the head in the list, remove it
			ll.head = nil
			ll.tail = nil
		} else {
			// node is the head, change head then to the next node in list
			ll.head = ll.head.next_node
		}
		ll.size -= 1
		return true
	}
	for curr.next_node != nil && curr.next_node.data != n.data {
		// iterate on the list
		curr = curr.next_node
	}

	if curr.next_node != nil {
		if curr.next_node == ll.tail {
			// node is the tail
			ll.tail = curr
		}
		// node is between head and tail, so skip it to remove
		curr.next_node = curr.next_node.next_node
		ll.size -= 1
		return true
	}
	// if all the tests fail, node is not in the list
	return false
}


func main() {
	ll := newLinkedList()
	fmt.Println(ll.size)
	n1 := newNode(44)
	n2 := newNode("ave")
	n3 := newNode(8.8)
	ll.insert(n1)
	ll.insert(n2)
	ll.insert(n3)
	fmt.Println("Original list")
	ll.printList()
	ll.remove(n3)
	fmt.Println("List removed")
	ll.printList()
}
