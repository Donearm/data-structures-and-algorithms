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
	"testing"
	"fmt"
	"os"
)

func typeOf(v interface{}) string {
	return fmt.Sprintf("%T", v)
}

func TestNewNode(t *testing.T) {
	n := newNode(55)
	nodetype := typeOf(n)
	if (nodetype != "*main.Node") {
		t.Errorf("The node was not correctly created")
	}
}

func TestGetData(t *testing.T) {
	n := newNode(46)
	value := n.getData()
	if (value != 46) {
		t.Error("Value of Node doesn't match")
	}
}

func TestSetData(t *testing.T) {
	n := newNode(12)
	n.setData(111)
	if (n.data != 111) {
		t.Error("Value in Node wasn't set")
	}
}

func TestNewLinkedList(t *testing.T) {
	ll := newLinkedList()
	if (typeOf(ll) != "*main.LinkedList") {
		t.Error("The Linked List wasn't successfully created")
	}
}

func TestGetSize(t *testing.T) {
	ll := newLinkedList()
	n1 := newNode(12)
	n2 := newNode(13)
	ll.insert(n1)
	ll.insert(n2)
	if (ll.size != 2) {
		t.Error("The size of the Linked List isn't correct")
	}
}

func TestInsert(t *testing.T) {
	ll := newLinkedList()
	n1 := newNode(333)
	ll.insert(n1)
	if (ll.size != 1) {
		t.Error("The Linked List has not the correct size")
	}
	if (ll.head != n1) {
		t.Error("The node insertion was not successful")
	}
}

func TestContains(t *testing.T) {
	ll := newLinkedList()
	n1 := newNode(45)
	n2 := newNode(56)
	nodeNotInList := newNode(444)
	ll.insert(n1)
	ll.insert(n2)
	if (ll.contains(nodeNotInList.data) != false) {
		t.Error("Node was erroneusly present in Linked List")
	}
	if (ll.contains(45) != true) {
		t.Error("Node was erroneously not found in Linked List")
	}
}

func TestRemove(t *testing.T) {
	ll := newLinkedList()
	n1 := newNode("abc")
	n2 := newNode(7.8)
	n3 := newNode(44)
	ll.insert(n1)
	ll.insert(n2)
	ll.insert(n3)
	ll.remove(n2)
	if (ll.size != 2) {
		t.Error("Size of Linked List wasn't update after the removal")
	}
	if (ll.head != n1) {
		t.Error("The head of the Linked List isn't correct after the removal")
	}
}

func TestMain(m *testing.M) {
	os.Exit(m.Run())
}

