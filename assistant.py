'''
The list of functions that don't do any math directly, but implement print out the steps
to passing values to the function. The idea is to allow for users who don't know much about python,
and how to use functions, can still use the program given they understand the engineering
behind these values.
'''

import calculator as calc
from PIL import Image
HSS_desc = calc.build_HSS_descriptors()
mats_table = calc.build_mat_table()


def truss_finder_directions():
    print("\n\nThis function determines the suitable HSS structural beams if given a few values.")
    print("\nThe minimum cross-sectional area, moment of inertia, and radius of gyration required. If there are no restrictrions on any of these variables, please enter 0 for said values.")
    print("\nThe function can also take a minimum factor of safety. To disregard factors of safety, enter 1).")
    print("\nWhen ready, hit enter and the program will begin.")
    dummy = input("")
    global HSS_desc

    A = float(input("Minimum cross-sectional Area (mm^2): "))
    I = float(input("Minimum moment of inertia (mm^4 x 10^6):"))
    r = float(input("Minimum radius of gyration (mm):"))
    FOS = float(input("Desired factor of safety: (if none desired, enter 1): "))
    all_cand = calc.find_HSS_all(A, I, r, FOS, HSS_desc)
    best = calc.find_HSS_lightest(A, I, r, FOS, HSS_desc)

    print("\n\nHere is a list of all candidates that I found suitable:")

    if len(all_cand) ==0:
        print("No such HSS beams found.")
        return
    for beam in all_cand:
        print("\n", beam[0], ": FOS of " , beam[1], " and a weight of ", beam[2], sep="")
    print("\n\nThe lightest of those cross-sections is ", best[0], ", weighing ", best[2], "kg/m.", sep="")


def i_finder_directions():
    print("\n\nThis function can compute the moment of inertia of common cross-sectional shapes of different sizes.")
    print("\nThe function can find the I for cross-sections in any of the following shapes:.")
    print("\n an \"I\" beam, a \"T\" beam, a \"pi\" beam, or a square cross-sectioned beam.")
    print("\n depending on the shape you'd like to choose, the program will ask for different dimensions")
    print("\nNote that if all dimensions are entered in units of x, the resulting value should have units of x^4")
    print("\nWhen ready, hit enter and the program will begin.")
    dummy = input("")

    type = input("Please enter a cross-section shape: s (square), I, T or pi: \n")
    print("\n\nI =", calc.beam_moment(type))

def net_force_directions():
    print("\n\nThis function can find the resultant net force of multiple forces on a 2-D object.")
    print("\nEach individual force must be specified by a magnitude and angle with a constant reference arm")
    print("\nEnter all magnitudes in N, angles in degrees")
    print("\nWhen ready, hit enter and the program will begin.")
    dummy = input("")

    count = int(input("Enter the number of forces to be analyzed: "))
    vector = calc.net_force_finder(count)
    print("\n\nResultant net force: ", vector[0], "N, ", vector[0], " degrees from the angle reference arm", sep = "")

def suspension_directions():
    print("\n\nThis function can find the highest tensile strength in the cables of a suspension bridge.")
    print("\nApart from basic bridge dimensions and the drape of the cables, an estimate of the load is required.")
    print("\nFor consistency with units, enter all values using m for dimensions, kN for loads.")
    print("\nWhen ready, hit enter and the program will begin.")
    dummy = input("")

    span = float(input("Enter the span of the bridge [m]: "))
    width = float(input("Enter the width of the bridge [m]: "))
    drape = float(input("Enter the drape of the cables of the bridge [m]: "))
    UDL = float(input("Enter the loading on the bridge [kN/m]: "))
    load = UDL * width

    tension = calc.suspension_tension(span, load, drape)
    print("\n\nHighest tension in the bridge cables will be ", load, "kN.", sep="")

def material_directions():
    print("\n\nThis function will determine which materials are available")
    print("\nApart from basic bridge dimensions and the drape of the cables, an estimate of the load is required.")
    print("\nFor consistency with units, enter all values using m for dimensions, kN for loads.")
    print("\nWhen ready, hit enter and the program will begin.")
    dummy = input("")

    E = float(input("Enter the required Young's Modulus: "))
    t_y = float(input("Enter the required Yield Strength under tension: "))
    t_u = float(input("Enter the required Failure Strength under tension: "))
    c = float(input("Enter the required Failure Strength under compression: "))
    cand = calc.find_mats(E, t_y, t_u, c, mats_table)
    lightest = calc.lightest_mat(cand)
    if len(cand) == 0:
        print("No such material found in materials data.")
        return
    print("\nThe following materials were considered to be strong enough:")
    for item in cand:
        print(item[0])
    print("\nOf those materials, the lightest is:", lightest[0])

def warren_truss_directions():
    print("\n\nThis function can compute the stresses in a truss and recommend apppropriate HSS members")
    print("\nApart from basic bridge dimensions, an estimate of the load is required.")
    print("\nFor consistency with units, enter all values using m for dimensions, kN for loads.")
    print("\nWhen ready, hit enter and the program will begin.")
    dummy = input("")

    im = Image.open("warren.png")
    im.show()

    print("The popup diagram shows what each of the different values being asked for represent.")

    UDL = float(input("Enter the load in terms of kN per m of length: "))
    span = float(input("Enter the span of the bridge: "))
    height = float(input("Enter the height of the truss: "))
    theta = float(input("Enter the angle theta as labelled inthe digram: "))

    sections = calc.warren_trusses(UDL, span, height, theta)
    print("\n\nThe truss could be built safely using these HSS sections:")
    print("Top Chord:", sections[1][0])
    print("Web:", sections[0][0])
    print("Bottom Chord:", sections[2][0])



# def popup():
#     im = Image.open("types.png")
#     im.show()







