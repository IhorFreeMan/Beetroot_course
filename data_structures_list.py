# -*- coding: utf-8 -*-
"""
Task 1

Extend UnorderedList

Implement append, index, pop, insert methods for UnorderedList.
Also implement a slice method, which will take two parameters `start` and `stop`,
and return a copy of the list starting at the position and going up to but not including the stop position.

"""
from node import Node


class UnorderedList:

    def __init__(self):
        self._head = None


    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self, new_data):
        new_node = Node(new_data)
        if self._head is None:
            self._head = new_node
            return
        current = self._head
        while current._next:
            current = current._next
        current._next = new_node

    def index(self, element):
        ind = 0
        current = self._head
        while current is not None:
            if element == current.get_data():
                return ind
            ind += 1
            current = current.get_next()
        else:
            raise ValueError("the value is not in the list")

    def pop(self, index):
        ind = 0
        current = self._head
        while current is not None:
            if ind == index:
                self.remove(current.get_data())
                return ind
            ind += 1
            current = current.get_next()
        else:
            raise IndexError("index is missing")

    def insert(self, index, element):
        ind = 0
        current = self._head
        while current is not None:
            if index == ind:
                current.set_data(element)
            ind += 1
            current = current.get_next()

    def slice(self, start, stop):
        ind = 0
        current = self._head
        cop = []
        while current is not None:
            if ind >= start and ind < stop:
                cop.append(current.get_data())
            ind += 1
            current = current.get_next()

        for i in cop:
            print(i)

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


"""
Task 2
Implement a stack using a singly linked list.
"""


class Stack:

    def __init__(self):
        self._head = None

    def add(self, new_data):
        new_node = Node(new_data)
        if self._head is None:
            self._head = new_node
            return
        current = self._head
        while current._next:
            current = current._next
        current._next = new_node

    def take(self):
        if self._head is None:
            return None
        if self._head._next is None:
            self.head = None
            return None
        previous = self._head
        current = self._head._next
        while current._next:
            previous = current
            current = current._next
        previous._next = None
        return current

    def __repr__(self):
        representation = "<Stack: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


"""
Task 3

Implement a queue using a singly linked list.
"""


class Queue:
    def __init__(self):
        self._head = None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def take(self):
        if self._head is None:
            return None
        if self._head._next is None:
            self.head = None
            return None
        previous = self._head
        current = self._head._next
        while current._next:
            previous = current
            current = current._next
        previous._next = None
        return current

    def __repr__(self):
        representation = "<Queue: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()




if __name__ == "__main__":
    print(f"{20 * '_'}\nTask 1\n")
    my_list = UnorderedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)
    my_list.append(1)
    my_list.append(2)
    # print(my_list.index(1))
    my_list.pop(7)
    my_list.insert(index=0, element=7)
    my_list.slice(0, 3)
    print(my_list)

    print(f"{20 * '_'}\nTask 2\n")
    my_stack = Stack()
    my_stack.add(1)
    my_stack.add(2)
    my_stack.add(3)
    my_stack.take()

    print(my_stack)
    print(f"{20 * '_'}\nTask 3\n")
    my_queue = Queue()
    my_queue.add(1)
    my_queue.add(2)
    my_queue.add(3)
    my_queue.take()
    print(my_queue)
