# File: EchoConverter.py
# Author: Jason Lu (jasonlu6@bu.edu)
# Collaborations:
# Rohin Banerji (rohinb96@bu.edu) (Class of 2019 Fellow Undergraduate CE student)
# Professor Douglas Densmore (dougd@bu.edu)
# Marliene Pavan (mapavan@bu.edu) (Supervisor / Senior Researcher at BU)
# Luis Ortiz (lortiz15@bu.edu) (Graduate supervisor of TECAN / ECHO conversion)
# Densmore CIDARLAB UROP Project #4 (WETLAB division)
# Date: 7/12/2017

# This program will take the input of a CSV / ECHO file (with five main
# parameters of command, source well, destination well, plate name, and transfer
# volume) and translate the data into English pseudocode for TECAN conversion

# conversion directly to TECAN is more difficult since the TECAN aspirate,
# dispense, and wash parameters have significantly more parameters
# than the ECHO counterparts

# importing the CSV module
import csv

# importing the string module
import string

# import system os
import sys

# class to store each dispensed TECAN solution
class instruction():
    # assume command to be a string
    command = " "
    # source well should be a coordinate tuple (A1 by default)
    sourceWell = [("A","1")]
    # destination well should also be a coordinate tuple
    destWell = [("","")]
    # plate name should be string (example: "reagent_plate")
    plateName = " "
    # transfer volume shluld be a float
    transferVolume = 0.0

# class to store additional parameters
class parameters():
    # row of the pipetting
    pipetteRow = 0
    # column of the pipetting
    pipetteCol = 0

# method for trying to parse the CSV file
# source (Python Documentation)
# https://docs.python.org/3/library/csv.html
def parseCSV():

    # read the CSV file (example: conversion.csv or JoVe article)
    with open('conversion.csv', newline='') as csvfile:
        # reader object to parse the file
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        # for loop to process the parsed lines
        for row in csvreader:
            print(', '.join(row))
    # print the file out
    print(csvfile)

# aspirate command
# well: int, source: string, transferVol = float
def aspirate(well,source,transferVol,plate):
    # same logic as TecanConverter.py
    if transferVol > 0.0 and transferVol < 100.0:
        # transferVol = instruction().transferVolume
        print("Transfer volume is: ", transferVol)
    elif transferVol == 0.0:
        print("TECAN robot unable to process.")
    else:
        print("Not enough to aspirate for TECAN robot")
    # print statement
    print("TECAN robot with well number " + str(well) + " and " + plate + " will aspirate amount of "
          + str(transferVol)+ " uL of solution at source well " + source)

# dispense command
# need to catch error since dispense takes away
# from the original solution
def dispense(well,dest,transferVol,plate):
    # same logic as TecanConverter.py
    # cap at 100 uL for now
    if transferVol > 0.0 and transferVol < 100.0:
        # transferVol = instruction().transferVolume
        print("Transfer volume is: ", transferVol)
    elif transferVol == 0.0:
        print("TECAN robot unable to process.")
    elif transferVol < 0.0:
        try:
            print("TECAN broke down!")
            print("Fix the TECAN robot before continuing...")
            sys.exit()
        # in case the volume goes below 0
        except ValueError:
            print("Transfer volume is not realistic!")
            # stop the TECAN robot from continuing run
    print("TECAN robot with well number " + str(well) + " and " + plate + " will dispense amount of "
              + str(transferVol) + " uL of solution at source well " + dest)

# wash command, pretty simple for this program
def wash(wellStart,wellEnd):
    print("TECAN washing wells from " + str(wellStart) + " : " + str(wellEnd))

# additional class (just in case)
def NotApplicable():
    if instruction().command == "dispense":
        print("No source well needed")
    elif instruction().command == "aspirate":
        print("No destination well needed")
    elif instruction().command == "wash":
        print("TECAN robot washing, no destination / source well needed")
    else:
        try:
            print("TECAN robot unable to proceed")
        except NameError:
            print("Unspecified TECAN command")
            raise

# main function to test it out
# for simplicity, only conversion.csv will be parsed
# if no CSV file available, then the commands will be put in manually
def main():

    print("Starting the TECAN robot: ")

    # parsing command
    parseCSV()

    # command 1
    print("Command 1: ")
    dispense(1,"A1",25.0,"ReagentPlate")

    # command 2
    print("Command 2: ")
    # dispense(1,"A1",25.0,"ReagentPlate")
    # try negative command (to catch the exception and stop TECAN robot)
    # dispense(2,"A1",-25.0,"ReagentPlate")
    # try 0.0 uL volume
    dispense(1,"A1",0.0,"ReagentPlate")

    # command 3
    print("Command 3: ")
    dispense(3,"A1",25.0,"ReagentPlate")

    # command 4
    print("Command 4: ")
    aspirate(1,"A1",25.0,"SetupPlate1")

    # command 5
    print("Command 5: ")
    # testing arithmetics 
    # dispense(1,"A1",-1*25.0,"SetupPlate1")
    dispense(1,"A1",25.0,"SetupPlate1")

    # print("BREAKDOWN 1")

    # command 6
    print("Command 6: ")
    print("TECAN first wash")
    wash(1,1)

    # command 7
    print("Command 7 : ")
    aspirate(1,"D3",25.0,"SetupPlate1")

    # command 8
    print("Command 8: ")
    dispense(1,"A1",25.0,"SetupPlate1")

    # command 9
    print("Command 9: ")
    print("TECAN second wash")

    # command 10
    print("Command 10: ")
    aspirate(1,"A2",25.0,"SetupPlate1")

    # command 11
    print("Command 11: ")
    dispense(1,"A1",25.0,"SetupPlate1")

    # command 12
    print("Command 12: ")
    print("TECAN third wash")
    wash(1,1)

    # command 13
    print("Command 13: ")
    aspirate(1,"D2",25.0,"SetupPlate1")

    # command 14
    print("Command 14: ")
    dispense(1,"A1",25.0,"SetupPlate1")

    # command 15
    print("Command 15: ")
    print("TECAN Final WASH!")
    wash(1,1)

    print("TECAN robot shutting down...")
main()






