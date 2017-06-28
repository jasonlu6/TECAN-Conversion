# File: Convert.py
# Author: Jason Lu (jasonlu6@bu.edu)
# Collaborations:
# Rohim Banerji (rohinb96@bu.edu) (Class of 2019 Fellow Undergraduate CE student)
# Professor Douglas Densmore (dougd@bu.edu)
# Marliene Pavan (mapavan@bu.edu) (Supervisor / Senior Researcher at BU)
# Luis Ortiz (lortiz15@bu.edu) (Graduate supervisor of TECAN / ECHO conversion)
# Densmore CIDARLAB UROP Project #4 (WETLAB division)
# Date: 6/28/2017

# imported packages: pyevo.py (with attribution to the original author)

# This program is a middleware function that will attempt to convert the
# command scripts from TecanConverter.py into a CSV file that can
# then be used for the ECHO script

# Revision: just require making a template of the 96
# Wells-Eppendorf Pipetting plate

# attribution: MIT CSail Documentation of the PyEvo module:
# http://people.csail.mit.edu/georgiou/pyevo/doc/

# importing the python evo module
# import pyevo
# importing string library
import string
# import math library
import math
# from pyevoRobot import pyevo

# importing the TECAN converter class
from numpy import iterable

import TecanConverter

import itertools

class Convert():
    def conversion(self,script,echo):
        self.script = script
        self.echo = echo

# class to store TECAN values
class TecanVals():
    values = range(1,96)
    # dictionary to store the tipNumbers for TECAN values
    dict = {}


# error check / handling exceptions
def parseString(str):
    try:
        return int(str)
    # throw the error!
    except ValueError:
        return str

class EchoVals():
    # Format of a 96-Well Eppendorf plate
    # Values range from 1A to 12H
    # chain.from_iterable() to link them together
    # start with a smaller set first
    # use Python zip() function

    alphabet = ["A","B","C","D","E","F","G","H"]
    values = ["1","2","3","4","5","6","7","8","9","10","11","12"]
    mapGrid = map(''.join,itertools.chain(itertools.product(alphabet,values),itertools.product(values,alphabet)))
    print("Grid of the ECHO: ")

    # generate an array of arrays to store the 96-Well Eppendorf
    # 8 * 12 grid
    plate = [["00"]*12 for i in range(8)]
    # for p in plate:
        # print(plate[p])

    # try to fill in some values
    # naive approach for now (figure out list comprehension later)

    # first row (A)
    for a in range(len(values)-1):
        # plate[1] = [('1','A')]
        plate[0] = [(values[a+1],alphabet[0])]
        print(plate[0],end="\n")

    # second row (B)
    for b in range(len(values)-1):
        plate[1] = [(values[b+1],alphabet[1])]
        print(plate[1],end="\n")

    # third row (C)
    for c in range(len(values)-1):
        plate[2] = [(values[c+1],alphabet[2])]
        print(plate[2],end="\n")

    # fourth row (D)
    for d in range(len(values)-1):
        plate[3] = [(values[d+1],alphabet[3])]
        print(plate[3],end="\n")

    # fifth row (E)
    for e in range(len(values)-1):
        plate[4] = [(values[e+1],alphabet[4])]
        print(plate[4],end="\n")

    # sixth row (F)
    for f in range(len(values)-1):
        plate[5] = [(values[f+1],alphabet[5])]
        print(plate[5],end="\n")

    # seventh row (G)
    for g in range(len(values)-1):
        plate[6] = [(values[g+1],alphabet[6])]
        print(plate[6],end="\n")

    # eighth row (H)
    for h in range(len(values)-1):
        plate[7] = [(values[h+1],alphabet[7])]
        print(plate[7],end="\n")


    # potential convert to a list approach?
    # test
    # print("\t".join(mapGrid), end=" ")



def main():
    print("96 Well-Eppendorf ECHO plate: ")
    print(" ")

    # keep the formatting relatively clean
    # print out the plate for now
    print(EchoVals.plate[1])
    print(EchoVals.plate[2])
    main()