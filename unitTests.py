"""
* Name : unitTests.py
* Author: Rawley Collins
* Created : 12/1/2021
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: Windows 10
* IDE: PyCharm 2021.2.1
* Copyright : This is my own original work
* based on specifications issued by our instructor
* Description : A file that contains the unit testing portion of this program
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""
import datetime
import unittest
import AssignmentClass


# a lot of my stuff is really hard to unit test and I'm frankly not at a skill level that allows me to do so
# and many of my functions outside of AssignmentClass are not able to be tested at all to my knowledge
class MyTestCase(unittest.TestCase):
    def testAssignmentClassGetName(self):
        assignment = AssignmentClass.Assignment("TheName", "TheClass", datetime.datetime(2021, 12, 5))
        self.assertEqual(assignment.getName(), "TheName")

    def testAssignmentClassGetClass(self):
        assignment = AssignmentClass.Assignment("TheName", "TheClass", datetime.datetime(2021, 12, 5))
        self.assertEqual(assignment.getClass(), "TheClass")


if __name__ == '__main__':
    unittest.main()
