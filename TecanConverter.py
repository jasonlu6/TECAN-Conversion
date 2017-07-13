# File: TecanConverter.py
# Author: Jason Lu (jasonlu6@bu.edu)
# Collaborations:
# Rohim Banerji (rohinb96@bu.edu) (Class of 2019 Fellow Undergraduate CE student)
# Professor Douglas Densmore (dougd@bu.edu)
# Marliene Pavan (mapavan@bu.edu) (Supervisor / Senior Researcher at BU)
# Luis Ortiz (lortiz15@bu.edu) (Graduate supervisor of TECAN / ECHO conversion)
# Densmore CIDARLAB UROP Project #4 (WETLAB division)
# Date: 6/28/2# File: TecanConverter.py
# Author: Jason Lu (jasonlu6@bu.edu)
# Collaborations:
# Rohim Banerji (rohinb96@bu.edu) (Class of 2019 Fellow Undergraduate CE student)
# Professor Douglas Densmore (dougd@bu.edu)
# Marliene Pavan (mapavan@bu.edu) (Supervisor / Senior Researcher at BU)
# Luis Ortiz (lortiz15@bu.edu) (Graduate supervisor of TECAN / ECHO conversion)
# Densmore CIDARLAB UROP Project #4 (WETLAB division)
# Date: 6/28/2017

# imported packages: pyevo.py (with attribution to the original author)

# This program is a simulation of a TECAN robot using TECAN instructions, and
# through a middleware class Convert.py, will give out the instructions
# of the simulation in ECHO format, which can then be used
# as a source text file for Excel CSV format

# attribution: MIT CSail Documentation of the PyEvo module:
# http://people.csail.mit.edu/georgiou/pyevo/doc/

# modification: now the program allows up to 100 TECAN commands
# due to increase of capacity and memoization of tube tip numbers
# in the Python list data structure

# importing the python evo module
# import pyevo
# importing string library
import string
# import math library
import math
# from pyevoRobot import pyevo

# class to store the amount of destination and source liquids
class liquidClass():
    # assume 500 uL for now for sourceLiquid
    sourceLiquid = 500
    # assume 0 uL for now for destLiquid
    destLiquid = 0
    # boolean to determine if the liquids are already used up

# imported packages: pyevo.py (with attribution to the original author)

# This program is a simulation of a TECAN robot using TECAN instructions, and
# through a middleware class Convert.py, will give out the instructions
# of the simulation in ECHO format, which can then be used
# as a source text file for Excel CSV format

# attribution: MIT CSail Documentation of the PyEvo module:
# http://people.csail.mit.edu/georgiou/pyevo/doc/

# modification: now the program allows up to 100 TECAN commands
# due to increase of capacity and memoization of tube tip numbers
# in the Python list data structure

# importing the python evo module
# import pyevo
# importing string library
import string
# import math library
import math
# from pyevoRobot import pyevo

# class to store the amount of destination and source liquids
class liquidClass():
    # assume 500 uL for now for sourceLiquid
    sourceLiquid = 500
    # assume 0 uL for now for destLiquid
    destLiquid = 0
    # boolean to determine if the liquids are already used up
    isUsedUp = False
    # tipNumber of the liquid class
    tipNumber = range(1,96,1)

# class to store plate attributes
class plate():

    # lab plate located at some location of robot workplace
    # constructor for plate
    def __init__(self,grid,site):
        self.grid = grid
        self.site = site
    # initialize to 0 for now
    grid = 0
    site = 0
    plateType = "P96WellEppendorf"
    # is there a well available?
    getFreeWell = False

# class to determine the location of a robot on the worktable
class location():
    # location constructor
    def __init__(self,grid,site):
        self.grid = grid
        self.site = site
    # initialze to 0 for now
    grid = 0
    site = 0

# method: aspirate
def aspirate(tipNumber, well, amount):
    if amount > 0:
        print("TECAN robot with tip " + str(tipNumber) + " will aspirate " + str(amount)
        + " uL at well " + str(well))
    elif amount < liquidClass.sourceLiquid:
        diff = liquidClass.sourceLiquid - amount
        print("TECAN robot with tip " + str(tipNumber) + " will aspirate " + str(diff)
        + " uL at well " + str(well))
    else:
        print("Not enough to aspirate for TECAN robot.")

# method: dispense
def dispense(tipNumber, well, amount):
    if amount > 0:
        print("TECAN robot with tip " + str(tipNumber) + " will dispense " + str(amount)
              + " uL at well " + str(well))
    elif amount > liquidClass.destLiquid:
        add = liquidClass.destLiquid + amount
        print("TECAN robot with tip " + str(tipNumber) + " will dispense " + str(add)
              + " uL at well " + str(well))
    else:
        print("Not enough to dispense for TECAN robot.")

# method: wash TECAN robot

# helper methods:
# pickUpTip()
# setBackTip()
def pickUpTip(tipNumber, tip):
    if tip != 0:
        print("Pick up tip " + str(tip) + " at DiTi number " + str(tipNumber))
    else:
        print("Do not pick up tip " + str(tip))
    # return the tipNumber
    return tipNumber

def setBackTip(tipNumber, tip):
    # figure out the math behind tip and tip number
    # diff = float(tipNumber - tip + 1)
    if tip != 0:
        print("Set back tip " + str(tip) + " at DiTi number " + str(tipNumber))
    else:
        print("Do not pick up tip " + str(tip))
    return tipNumber

def wash(tipNumbers, well):
    # each value of well is a float
    wellVal = 96.0
    # tipNumber is a range of tip numbers
    for i in range(well):
        # debugging statements
        # print("well is : " + str(well))
        # print("tipNumbers[i] is " + str(tipNumbers))
        if tipNumbers < well:
            # pick up the tip
            pickUpTip(liquidClass.tipNumber,i)
        elif tipNumbers == well:
            # set back the tip
            setBackTip(liquidClass.tipNumber,i)
        else:
            # round up to the next tip available
            print("Onto the next tip: " + math.ceil(wellVal + float(tipNumbers+1)))
    print("TECAN robot done washing")

# functions to be built:
# enzyme dictionary function

# reagent function
# well: as a range of numbers
def reagent(source,dest,tipNumber,well,amount,start,end):
    tipNumber = range(1,96,1)
    print("Dispensing from reagent plate " + str(source) + " from 96 well" + " to tips " +
          str(tipNumber[start:end]) + " with a volume of " + str(amount) + " uL.")
    return amount

# main function to test this all out

# script should match the results from TECAN to ECHO conversion
# attempt first 20 commands for now

# As a initial stage, we are assuming that
# dispensing is only on 1 plate, on a 96-well Eppendorf

# we will build a Robot() class later for OOP purposes
# maybe even use an interface, similar to that of Java
def main():
    print("Starting the TECAN robot: ")

    print("Well used for the experiment:")
    print(plate.plateType)

    print("Is the well free for reuse?")
    print(plate.getFreeWell)

    # skip first 3 commands, reagent class not built yet
    print("Command 1: ")
    reagent(1,1,1,96,6,1,33)
    print("Command 2: ")
    reagent(1,2,2,96,6,34,66)
    print("Command 3: ")
    reagent(1,3,3,96,6,67,96)
    print(("Command 4:"))
    aspirate(1,96,2)
    print("Command 5: ")
    dispense(1,96,2)
    print("Command 6: ")

    # wash
    print("TECAN Robot First Wash")
    wash(1,96)


    print("Command 7: ")
    aspirate(1,1,2)
    print("Command 8: ")
    dispense(1,1,2)

    print("Command 9: ")

    # wash
    print("TECAN Robot Second Wash")
    wash(1,2)


    print("Command 10: ")
    aspirate(96,1,2)
    print("Command 11: ")
    dispense(96,1,2)
    print("Command 12: ")

    # full clean wash of all of the wells

    print("FIRST CLEAN WASH FROM ROBOT: ")
    print()
    print("TECAN Robot Third Wash")
    wash(96,96)


    print("Command 13: ")
    aspirate(1,12,2)

    print("Command 14: ")
    dispense(1,1,2)

    print("Command 15: ")

    print("TECAN Robot Fourth Wash")
    wash(1,1)


    print("Command 16: ")
    aspirate(96,16,2)

    print("Command 17: ")
    dispense(1,96,2)

    print("Command 18: ")

    print("TECAN Robot Fifth Wash: ")
    wash(1,96)

    print("Command 19: ")
    print("Reservior command, robot does another task")

    print("Command 20: ")
    dispense(1,1,4)

    # final clean wash of the experiment
    print("Command 21: ")
    print()
    print("FINAL WASH :-)")
    wash(1,96)

    print("TECAN Robot Shutting Down...")
    print("TECAN Robot JoVE Experiment Done!")

    print("PART II of TECAN Robot: ")

    # extension to 100th command (according to the procedure / discussion
    # set out by Luis yesterday)

    print("Command 22: ")
    aspirate(1,20,2)

    print("Command 23: ")
    dispense(1,3,2)

    print("Command 24: ")
    wash(1,20)

    print("Command 25: ")
    aspirate(1,1,2)

    print("Command 26: ")
    dispense(1,3,2)

    print("Command 27: ")
    wash(1,1)

    print("Command 28: ")
    aspirate(1,9,2)

    print("Command 29: ")
    dispense(1,3,2)

    print("Command 30: ")
    wash(9,3)

    print("Command 31: ")
    aspirate(1,14,2)

    print("Command 32: ")
    aspirate(1,3,2)

    print("Command 33:")
    wash(14,3)

    print("Command 34: ")
    aspirate(1,16,2)

    print("Command 35: ")
    dispense(1,3,2)

    print("Command 36: ")
    wash(16,3)

    print("Command 37: ")
    print("Reservior command, robot does another task")

    print("Command 38: ")
    dispense(1,3,4)

    print("Command 39: ")
    wash(1,3)

    print("Command 40: ")
    aspirate(1,20,2)

    print("Command 41: ")
    dispense(1,4,2)

    print("Command 42: ")
    wash(20,4)

    print("Command 43: ")
    aspirate(1,1,2)

    print("Command 44: ")
    dispense(1,4,2)

    print("Command 45: ")
    wash(1,4)

    print("Command 46: ")
    aspirate(1,9,2)

    print("Command 47: ")
    dispense(1,4,2)

    print("Command 48: ")
    wash(9,4)

    print("Command 49: ")
    aspirate(1,15,2)

    print("Command 50: ")
    dispense(1,4,2)

    print("Command 51: ")
    wash(15,4)

    print("Command 52: ")
    aspirate(1,16,2)

    print("Command 53: ")
    dispense(1,4,2)

    print("Command 54: ")
    wash(16,4)

    print("Command 55: ")
    print("Reservior command, robot does another task")

    print("Command 56: ")
    dispense(1,4,4)

    print("Command 57: ")
    wash(1,4)

    print("Command 58: ")
    aspirate(1,20,2)

    print("Command 59: ")
    dispense(1,5,2)

    print("Command 60: ")
    wash(20,5)

    print("Command 61: ")
    aspirate(1,1,2)

    print("Command 62: ")
    dispense(1,5,2)

    print("Command 63: ")
    wash(1,5)

    print("Command 64: ")
    aspirate(1,10,2)

    print("Command 65: ")
    dispense(1,5,2)

    print("Command 66: ")
    wash(10,5)

    print("Command 67: ")
    aspirate(1,12,2)

    print("Command 68: ")
    dispense(1,5,2)

    print("Command 69: ")
    wash(12,5)

    print("Command 70: ")
    aspirate(1,16,2)

    print("Command 71: ")
    dispense(1,5,2)

    print("Command 72: ")
    wash(16,5)

    print("Command 73: ")
    print("Reservior command, robot does another task")

    print("Command 74: ")
    dispense(1,5,4)

    print("Command 75: ")
    # since no aspirate command was found
    wash(5,0)

    print("Command 76: ")
    aspirate(1,20,2)

    print("Command 77: ")
    dispense(1,6,2)

    print("Command 78: ")
    wash(20,6)

    print("Command 79: ")
    asprate(1,1,2)

    print("Command 80: ")
    dispense(1,6,2)

main()




