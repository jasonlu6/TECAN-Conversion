# File: tecanmessenger.py
# Author: Jason Lu (jasonlu6@bu.edu)
# Collaborations:
# Rohin Banerji (rohinb96@bu.edu) (Class of 2019 Fellow Undergraduate CE student)
# Professor Douglas Densmore (dougd@bu.edu)
# Marliene Pavan (mapavan@bu.edu) (Supervisor / Senior Researcher at BU)
# Luis Ortiz (lortiz15@bu.edu) (Graduate supervisor of TECAN / ECHO conversion)
# Densmore CIDARLAB UROP Project #4 (WETLAB division)
# Date: 7/13/2017

# Description: first of the many "error-checking" deliverables for
# the TECAN to ECHO conversion. Will catch the most generic systematic,
# lexical, and name / type errors in the aspirate, dispense, wash, and reagent
# commands

# source:
'''Manual Freedom EVOware 2.3 Research Use Only copy.pdf (Ch 18.1)'''

''' 7/13/2017: make sure that the TECAN robot simulator can catch
the exceptions in a regular manner (purposely try some error-raising commands
in the aspirate and dispense commands)'''

'''Not an extensive list of errors / handling, best consult the manual'''

# import the pythonEVO module
# import pyevo

# importing string library
import string

# importing the math library (to test floating error)
import math

# additional import
# from pyevoRobot import pyevo

# class to keep all of the errors
class TecanErrors(Exception):

    '''self-initializing method to determine the TECAN robot's
    startng reservior volume, tip number, source, destination wells, and
    well number'''
    def __init__(self,washVolume,tipNumber,source,dest,well):
        self.washVolume = washVolume
        self.tipNumber = tipNumber
        self.source = source
        self.dest = dest
        self.well = well

        # initialize the parameters (assume 1000 mL for reservior wash volume)
        washVolume = 1000
        # keep the tip numbers in a list for now 
        tipNumber = []
        # init source well (as a tuple) 
        source = [(",")]
        # init destination well (also as a tuple)
        dest = [(",")]
        # initi well number (start at well 1)
        well = 1

    # initialize the error with a message
    def __init__(self,message,errors):

        # call base class constructor with a super function
        super(ReserviorError,self).__init__(message)

        # create the reservior error
        self.errors = errors
        
    # first Tecan error: volume of water (reservior) has run out
    def reserviorRunOut(washVolume):
        if washVolume != 1000:
            print("TECAN robot reservior has run out! Please refill")
        else:
            print("Continue the procedure")

# separate class to raise various TECAN robot exceptions

# how to print out the Python traceback script? 

# reservior exception class 
class ReserviorExceptions(Exception):
    pass
    # first error to raise
# raise ReserviorExceptions("TECAN robot reservior has run out! Please refill.")
print("TECAN robot reservior has run out! Please refill.")

class SourceWellException(Exception):
    pass
    # second error to raise
#raise SourceWellException("TECAN robot source well not defined.")
print("TECAN robot source well not defined.")

class DestinationWellException(Exception):
    pass
    # third error to raise
# raise DestinationWellException("TECAN robot destination well not defined.")
print("TECAN robot destination well not defined.")

    # clot error, tip error, pmp error other errors
    # described in the TECAN manual Chapter 18
    # liquid detection error
class LiquidDetectionError(Exception):
    pass
raise LiquidDetectionError('''TECAN DiTi Script Sample as no liquid or not enough
liquid in the reservior''')

class ClotError(Exception):
    pass
    # clot error 
raise ClotError("Exit signal during pipetting has occured!")

class PMPError(Exception):
    pass
    # pressure monitored pipetting error (PMP)
raise PMPError("Tip" + str(self.tipNumber) + "is effected. Please diagnose immediately.")

class PMPInstrumentError(Exception):
    pass
    # PMP instrument error
raise PMPInstrumentError("Something is wrong with a TECAN part. Please shut down the robot.")

class LiquidArrivalCheckError(Exception):
    pass
    # liquid arrival check error
raise LiquidArrivalCheckError("Incorrect volume dispensed before pipetting!")

    # raise other errors (if necessary)...

# same methods from TecanConverter.py (as a copy)
'''Methods necessary in order to test exception handling
with the first 100 TECAN commands from the JoVE article
experiment'''
# class to store the amount of destination and source liquids
class liquidClass():
    # assume 500 uL for now for sourceLiquid
    sourceLiquid = 500
    # assume 0 uL for now for destLiquid
    destLiquid = 0
    # boolean to determine if the liquids are already used up

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


# main function (using the module functions from TecanConverter.py)
def main():

    print("Testing Error handling with TECAN robot, using the same 100 commands in the prototype conversion script.")

main()
    
    


    

