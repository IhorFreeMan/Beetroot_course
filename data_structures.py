# -*- coding: utf-8 -*-
import stack

"""
Task 1

Write a program that reads in a sequence of characters and prints them in reverse order,
using your implementation of Stack.

"""


class CorrectedStack:
    def __init__(self):
        self._items = []

    def set_e(self, e):
        self._items.append(e)

    def pop(self):
        return self._items.pop()

    # def __iter__(self):
    #     return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __repr__(self):
        return f"{self._items}"


"""
Task 2

Write a program that reads in a sequence of characters, 
and determines whether it's parentheses, braces, and curly brackets are "balanced."
"""



def chek_balanced(elem: CorrectedStack) -> bool:
    s = Stack()


    def serch(element_one, element_twu):
        rez = False
        for i in elem:
            if i == element_one:
                s.push(i)

            if i == element_twu:
                try:
                    s.pop()
                except IndexError:
                    return rez

        if s.is_empty() == False:
            rez = True
            return rez

    if serch("(", ")") and serch("{", "}"):
        return True
    else:
        return False



"""
Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
Any other element must remain on the stack respecting their order. 
Consider the case in which the element is not found - raise ValueError with proper info Message

 
Extend the Queue to include a method called get_from_stack that searches and returns an element e from a queue. 
Any other element must remain in the queue respecting their order.
 Consider the case in which the element is not found - raise ValueError with proper info Message
"""


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def get_from_stack(self, e):
        if e in self._items:
            return e
        else:
            raise ValueError("Element is missing")

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    # def __iter__(self):
    #     return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def get_from_stack(self, e):
        if e in self._items:
            return e
        else:
            raise ValueError("Element is missing")

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    print(f"{20 * '_'}\nTask 1\n")
    s = CorrectedStack()
    s.set_e("1")
    s.set_e("2")
    s.set_e("3")
    print(s[::-1])

    print(f"{20 * '_'}\nTask 2\n")

    y = CorrectedStack()
    y.set_e("(")
    y.set_e("#")
    y.set_e("#")
    y.set_e(")")
    y.set_e("{")
    y.set_e("}")
    print(chek_balanced(y))

    print(f"{20 * '_'}\nTask 3\n")
    st = Stack()
    st.push("1")
    st.push("2")
    st.push("3")
    print(st)
    print("Stack", st.get_from_stack("1"))
    # print(st.get_from_stack("4"))

    queue = Queue()
    queue.enqueue("1")
    queue.enqueue("2")
    queue.enqueue("3")
    print(st)
    print("Queue", st.get_from_stack("2"))
    # print(queue.get_from_stack("4"))
