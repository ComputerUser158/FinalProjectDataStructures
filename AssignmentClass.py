"""
* Name : AssignmentClass.py
* Author: Rawley Collins
* Created : 12/1/2021
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: Windows 10
* IDE: PyCharm 2021.2.1
* Copyright : This is my own original work
* based on specifications issued by our instructor
* Description : A file that contains the assignment class portion of this program
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""


# class to hold the assignments
class Assignment:
    def __init__(self, assignmentName, assignmentClass, assignmentDueDate):
        self.assignmentName = assignmentName
        self.assignmentClass = assignmentClass
        self.assignmentDueDate = assignmentDueDate

    def getName(self):
        return self.assignmentName

    def getClass(self):
        return self.assignmentClass

    def getDueDate(self):
        return self.assignmentDueDate
