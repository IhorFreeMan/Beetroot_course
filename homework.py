# -*- coding: utf-8 -*-


"""
Task 1

File Context Manager class

Create your own class, which can behave like a built-in function `open`.
Also, you need to extend its functionality with counter and logging.
Pay special attention to the implementation of `__exit__` method,
which has to cover all the requirements to context managers mentioned here:

"""


class ContextM:
    _Count = 0

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        ContextM._Count += 1
        print(f"Opened file {self.filename}")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        ContextM._Count -= 1
        self.file.close()
        print(f"Closed file {self.filename}")
        if exc_type is not None:
            file1 = open("log.txt", "a")
            file1.write(f"{exc_val}" + "\n")
            file1.close()
        return False


"""
Task 2

Writing tests for context manager

Take your implementation of the context manager class from Task 1 and write tests for it. 
Try to cover as many use cases as you can, positive ones when a file exists and everything works 
as designed. And also, write tests when your class raises errors or you have errors in the runtime context suite.

"""

if __name__ == "__main__":
    with ContextM(r"sam_file.txt", "w") as file:
        # print(ContextM._Count)
        # print(1/0)
        file.write('test')
    # print(ContextM._Count)
