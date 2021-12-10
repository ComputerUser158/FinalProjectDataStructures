"""
* Name : LinkedListClass.py
* Author: Rawley Collins
* Created : 12/1/2021
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: Windows 10
* IDE: PyCharm 2021.2.1
* Copyright : This is my own original work
* based on specifications issued by our instructor
* Description : A file that contains the linked list class portion of this program
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""


class Nodes:
    def __init__(self, assignment=None):
        # will hold assignment data
        self.assignment = assignment
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, node):
        # adds to the start of the linked list
        node.next = self.head
        self.head = node

    def __iter__(self):
        # this function allows linked list to iterate
        node = self.head
        while node is not None:
            yield node
            node = node.next



