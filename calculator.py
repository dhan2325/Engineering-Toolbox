'''
this is the file containing all computational functions. Functions go beyond just
performing calculations, can also make recommendations based on entered requirements
and tables of structural properties/material properties.
'''

import math

###
def build_HSS_descriptors():
    text = open("HSS.txt", "r", encoding="latin1").read()
    temp1 = text.split("\n")
    temp2 = []
    desc = {}

    for beam in temp1:
        temp2.append(beam.split("\t"))
    for beam in temp2:
        desc[beam[0]] = [float(beam[1]), float(beam[2]), float(beam[3]), float(beam[4])]
    return desc

def find_HSS_all(A, I, r, min_FOS, desc):
    #file format goes title, mass(kg/m), Area (mm^2), I (10^6 mm^4), r (10^3 mm^3)
    cand = []
    for HSS in desc.keys():
        if A == 0:
            FOS_A = 10000
        else:
            FOS_A = desc[HSS][1] / A
        if r == 0:
            FOS_r = 10000
        else:
            FOS_r = desc[HSS][1] / r
        if I == 0:
            FOS_I = 10000
        else:
            FOS_I = desc[HSS][1] / I

        if (FOS_A >min_FOS and FOS_I > min_FOS and FOS_r > min_FOS):
            cand.append([HSS, min(FOS_A, FOS_I, FOS_r), desc[HSS][0]])
            #HSS dimensions, lowest factor of safety, weight (kg/m)
    return cand


def find_HSS_lightest(A, I, R, min_FOS, desc):
    cand = find_HSS_all(A, I, R, min_FOS, desc)
    best = []
    min_weight = 120 #greater than max weight

    for HSS in cand:
        if HSS[2] < min_weight:
            best = HSS
            min_weight = HSS[2]

    return best

# def get_HSS():
#     to_get = input("Enter the dimensions of the croess-section as 000x00x00")

###
def truss_max_stress():
    pass

###
def net_force_finder(count):
    f_x = 1
    f_y = 1
    force = 0
    angle = 0

    for i in range (count):
        print("Force number", i + 1)
        force = float(input("Force Magnitude [N]: "))
        angle = float(input("Angle with angle reference arm [deg]: "))
        f_x += math.cos(math.radians(angle)) *force
        f_y += math.sin(math.radians(angle)) *force
    mag = round((f_x**2 + f_y**2) ** 0.5, 3)
    dir = round(math.degrees(math.atan(f_y/f_x)), 4)
    return(mag, dir)


###
def beam_moment(type):
    # type must be T, I or Pi
    if type == "T": # parameters wil include top flange width + height, bottom section width+height
        tw = float(input("Please enter the top flange width: "))
        th = float(input("\nPlease enter the top flange height: "))
        ww = float(input("\nPlease enter the web width: "))
        wh = float(input("\nPlease enter the web height: "))

        y_bar = (wh*ww*0.5*wh + tw*th*0.5*th) / (wh*ww + tw*th)
        I = (ww*wh)*(wh-y_bar)**2 + (1/12)*(ww*wh**3) + (tw*th)*(0.5*th+wh-y_bar) + (1/12)*(tw*th**3)
        return I

    elif type == "I":
        fw = float(input("Please enter the flange width: "))
        fh = float(input("\nPlease enter the flange height: "))
        ww = float(input("\nPlease enter the web width: "))
        wh = float(input("\nPlease enter the web height: "))
        I = (1/12)*(wh+2*fh)**3 * fw - (1/12)*(fw-ww) * wh**3
        return I
    elif type == "pi":
        fw = float(input("Please enter the flange width: "))
        fh = float(input("\nPlease enter the flange height: "))
        ww = float(input("\nPlease enter the web width: "))
        wh = float(input("\nPlease enter the web height: "))
        y_bar = (fw*fh*(0.5*fh + wh) + ww*wh**2)/ (2*ww*wh + fw*fh)
        I = (1/12)*fw*fh**3 + fw*fh*(0.5*fh + wh - y_bar)**2 + (1/6)*(wh**3 * ww) + 2*(wh*ww)*(y_bar - 0.5*wh)**2
        return I
    elif type == "s":
        w = float(input("Please enter the width of one side of the cross-section: "))
        t = float(input("\nPlease enter the thickness of the walls of the cross-section: "))
        I= (1/12)*(w**4 - (w-2*t)**4)
        return I

    print("The cross-beam type entered was invalid. ")
    return


###
def suspension_tension(span, weight, drape):
    t_max = ((span*weight**2 / (8*drape))**2 + (weight*span / 2)**2)**0.5
    return t_max

###
def build_mat_table():
    text = open("materials.txt", "r").read()
    temp1 = text.split("\n")
    temp2 = []
    desc = {}

    for mat in temp1:
        temp2.append(mat.split("\t"))
    for mat in temp2:
        desc[mat[0]] = [float(mat[1]), float(mat[2]), float(mat[3]), float(mat[4]), float(mat[5])]
        # material: density, E, ten_y, ten_u, comp
    return desc

def find_mats(E, t_y, t_u, c, table): # all values are minima
    cand = []
    for mat in table.keys():
        if table[mat][1] >=E and table[mat][2] >= t_y and table[mat][3] >= t_u and table[mat][4] >=c:
            cand.append([mat, table[mat][1], table[mat][2], table[mat][3], table[mat][4], table[mat][0]])
            #name, E, t_y, t_u, c, den
    return cand

def lightest_mat(cand):
    #cand is a list of candidates (as given by find_mats)
    best = []
    min_weight = 78 # heaviest material is 77

    if len(cand) == 0:
        return

    for mat in cand:
        if mat[5] < min_weight:
            best = mat
            min_weight = mat[5]
    return best

###
def howe_trusses():
    pass

def pratt_trusses():
    pass

def warren_trusses(UDL, span, height, theta):
    #must solve: web length, chord segment length, number of segments, base segment length
    #find stresses in beams at midspan, use to determine lowest A, I, r
    #recommend HSS structure like a boss
    global HSS_desc
    base = (2*height) / math.tan(math.radians(theta)) #chord segment length
    web_len = height / math.sin(math.radians(theta)) # length of web member

    num_units = int(round(span / base))
    supp = (base*UDL)*((num_units-1)/2)
    pi = math.pi

    if num_units%2 == 0: #even number of segments
        web_force = supp / (math.sin(math.radians(theta)))
        top_chord = (supp*span) / (2*height)
        bot_chord = web_force*math.cos(math.radians(theta)) + top_chord
    else:
        web_force = supp / (math.sin(math.radians(theta)))
        bot_chord = supp*span / (2*height)
        top_chord = bot_chord * math.cos(math.radians(theta)) + bot_chord

    #units are metres, kN

    #check compression only for web, top chord
    web_HSS = find_HSS_lightest(2000*(web_force/700), 3000*web_force*web_len/(200000 * pi**2), web_len*5, 1, HSS_desc)
    top_HSS = find_HSS_lightest(2000*top_chord/700, 3000*top_chord*base/(200000 * pi**2), base*5, 1, HSS_desc)
    bot_HSS = find_HSS_lightest(2000*bot_chord/700, 0, base*5, 1, HSS_desc)
    return [web_HSS, top_HSS, bot_HSS]















