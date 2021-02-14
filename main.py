''' all code written by Daniel Han, for the Open competitiion category of YUHacks Feb 2021.'''
'''
the "main" file has the user-interface functions, and allows for the user to use all functions without having to enter the functions and parameters into the terminal.
two main functions in this file are initialize(); which starts the program, and continue(), which guides the user back after having reached the end of one inquiry
'''


import calculator as calc
import assistant as assist
import PIL

def show_tasks():
    print(open("introduction.txt", "r").read()[320:])
    print("====================================================")

def initialize():
    intro = open("introduction.txt", "r")
    print(intro.read())
    global HSS_desc
    global mats_table

    task = int(input("Please enter the number of your desired task: "))
    print("====================================================")
    if task == 0:
        print("All fuctions are available for you to use. to revisit the options available, use command show_tasks()")
        return

    elif task == 1:
        assist.truss_finder_directions()
    elif task == 2:
        assist.i_finder_directions()
    elif task == 3:
        assist.warren_truss_directions()
    elif task == 4:
        assist.suspension_directions()
    elif task == 5:
        assist.net_force_directions()
    elif task == 6:
        assist.material_directions()

    print("\n\nUse command calculate() to perform a new calculation")



def calculate():
    print("====================================================")
    show_tasks()
    global HSS_desc
    task = int(input("Please enter the number of your desired task: "))
    print("====================================================")

    if task == 0:
        print("All fuctions are available for you to use. to revisit the options available, use command show_tasks()")
        return

    elif task == 1:
        assist.truss_finder_directions()
    elif task == 2:
        assist.i_finder_directions()
    elif task == 4:
        assist.suspension_directions()
    elif task == 5:
        assist.net_force_directions()

    print("\n\nUse command calculate() to perform a new calculation")



