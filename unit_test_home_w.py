# -*- coding: utf-8 -*-
import unittest
import homework


"""
Task 2

Writing tests for context manager

Take your implementation of the context manager class from Task 1 and write tests for it. 
Try to cover as many use cases as you can, positive ones when a file exists and everything works 
as designed. And also, write tests when your class raises errors or you have errors in the runtime context suite.

"""


class ContextTestCase(unittest.TestCase):
    def setUp(self):
        self.filename = 'test_file.txt'

    def test_file_opened_and_closed(self):
        with homework.ContextM(self.filename, 'w') as file:
            self.assertTrue(file.closed is False)
        self.assertTrue(file.closed is True)

    def test_file_content_written(self):
        with homework.ContextM(self.filename, 'w') as file:
            file.write('test')
        with open(self.filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, 'test')

    def test_exception_logged(self):
        with self.assertRaises(Exception):
            with homework.ContextM(self.filename, 'w') as file1:
                raise Exception('test exception')
        with open('log.txt', 'r') as file2:
            content = file2.read()
            self.assertEqual(content, 'test exception\n')


if __name__ == '__main__':
    unittest.main()
