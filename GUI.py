"""
* Name : GUI.py
* Author: Rawley Collins
* Created : 12/4/2021
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: Windows 10
* IDE: PyCharm 2021.2.1
* Copyright : This is my own original work
* based on specifications issued by our instructor
* Description : A file that contains the gui portion of this program
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""


import tkinter
from tkinter import *
import LinkedListClass
import AssignmentClass
import datetime


# type of sort to be done
def dateSort(x):
    return x.assignment.getDueDate()


def classSort(x):
    return x.assignment.getClass()


# will sort and overwrite assignments to file
def writeSortedToFile(filename, linkedList, sortType):
    log = open(filename, 'w')
    sorting = []
    for x in linkedList:
        sorting.append(x)

    # decides on the sort to do
    if sortType == "date":
        sorting.sort(reverse=False, key=dateSort)
    elif sortType == "class":
        sorting.sort(reverse=False, key=classSort)
    else:
        pass

    for x in sorting:
        log.write(x.assignment.getName() + ", " + x.assignment.getClass() + ", " + str(x.assignment.getDueDate()) + "\n")


def showAssignments(filename):
    with open(filename, 'r') as f:
        assignmentText.insert(END, f.read())


def createAssignment(assignmentList):
    # assignment name, class name, year, month, and day inputs
    assignmentName = e1.get()
    className = e2.get()
    try:
        year = int(e3.get())
        month = int(e4.get())
        day = int(e5.get())

        # creates an assignment and adds it to a list to be passed
        newAssignment = AssignmentClass.Assignment(assignmentName, className, datetime.datetime(year, month, day))
    except:
        # if the user enters a bad value a default error assignment will be added instead
        newAssignment = AssignmentClass.Assignment("User Input Error", "N/A", datetime.datetime(1, 1, 1))
    assignmentList.append(newAssignment)
    return assignmentList


# will be run after an assignment list is created
def createLinkedList(assignList, sortType):
    # creates and adds nodes from the list of assignments
    myLinkedList = LinkedListClass.LinkedList()
    counter = 0
    while counter < len(assignList):
        node = LinkedListClass.Nodes(assignList[counter])
        myLinkedList.add_first(node)
        counter = counter + 1

    writeAndShow(myLinkedList, sortType)


def writeAndShow(linkedList, sortType):
    # paths will vary, will likely need changed
    writeSortedToFile("C:/Users/Owner/PycharmProjects/FinalProjectDataStructures/AssignmentFile", linkedList, sortType)
    showAssignments("C:/Users/Owner/PycharmProjects/FinalProjectDataStructures/AssignmentFile")


if __name__ == '__main__':
    window = Tk()

    # assignment name input field
    e1 = tkinter.Entry(window)
    e1.insert(10, "Assignment Name")
    e1.pack(padx=5, pady=10, side=TOP, anchor=W)

    # assignment class input field
    e2 = tkinter.Entry(window)
    e2.insert(10, "Class")
    e2.pack(padx=5, pady=10, side=TOP, anchor=W)

    # assignment year input field
    e3 = tkinter.Entry(window)
    e3.insert(10, "year")
    e3.pack(padx=5, pady=10, side=TOP, anchor=W)

    # assignment month input field
    e4 = tkinter.Entry(window)
    e4.insert(10, "month")
    e4.pack(padx=5, pady=10, side=TOP, anchor=W)

    # assignment day input field
    e5 = tkinter.Entry(window)
    e5.insert(10, "day")
    e5.pack(padx=5, pady=10, side=TOP, anchor=W)

    # storage list
    passList = []
    # buttons
    ListButton = Button(text="Add Assignment to Group", command=lambda: createAssignment(passList))
    ListButton.pack(padx=5, pady=10, side=TOP, anchor=W)

    # sort and display buttons
    pushButton = Button(text="Show Assignments Sorted by Date", command=lambda: createLinkedList(passList, "date"))
    pushButton.pack(padx=5, pady=3, side=TOP, anchor=W)
    pushButton = Button(text="Show Assignments Sorted by Class", command=lambda: createLinkedList(passList, "class"))
    pushButton.pack(padx=5, pady=3, side=TOP, anchor=W)

    # display fields
    firstLabel = Label(text="Assignments: ")
    firstLabel.pack(padx=5, pady=15, side=TOP, anchor=W)
    firstLabel.config(bg='#3FB6CB')
    assignmentText = Text(height=5, width=60)
    assignmentText.pack(padx=5, pady=15, side=TOP, anchor=W)
    assignmentText.lower(firstLabel)

    # the path for this will likely need changed
    assignmentsButton = Button(text="Show Assignments Currently Stored in File", command=lambda: showAssignments(
        "C:/Users/Owner/PycharmProjects/FinalProjectDataStructures/AssignmentFile"))
    assignmentsButton.pack(padx=5, pady=15, side=TOP, anchor=NW)
    firstLabel.pack(padx=5, pady=15, side=TOP, anchor=W)

    # window details
    window.title("Homework Tracker")
    window.geometry("850x720")
    window['background'] = '#3FB6CB'

    # button to easily clear the text box
    clearButton = Button(text="Clear Text Box", command=lambda: assignmentText.delete(1.0, END))
    clearButton.pack(padx=5, pady=15, side=TOP, anchor=W)

    window.mainloop()
