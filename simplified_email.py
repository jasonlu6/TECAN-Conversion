# File: simplified_email.py
# Author: Jason Lu (jasonlu6@bu.edu)
# Collaborations:
# Rohin Banerji (rohinb96@bu.edu) (Class of 2019 Fellow Undergraduate CE student)
# Professor Douglas Densmore (dougd@bu.edu)
# Marliene Pavan (mapavan@bu.edu) (Supervisor / Senior Researcher at BU)
# Luis Ortiz (lortiz15@bu.edu) (Graduate supervisor of TECAN / ECHO conversion)
# Densmore CIDARLAB UROP Project #4 (WETLAB division)
# Date: 7/13/2017 - 8/11/2017 

# Description: second of the "error-checking" deliverables, which
# will use Python's SMTP / Email library modules to give the
# user a rudimentary version of an email system to give user
# information about errors (using a 0-12 message code, where 0 is no error
# occuring, and TECAN can continue running the script)

# simplified version (only send a message from TECAN robot, no subject specified) 

# source:

'''Manual Freedom EVOware 2.3 Research Use Only copy.pdf (Ch 18.1)'''

''' 7/13/2017: make sure that the TECAN robot simulator can catch
the exceptions in a regular manner (purposely try some error-raising commands
in the aspirate and dispense commands)'''

''' 7/25/2017: connect to the email.py and tecanconnect.py (or another programming language form)
in order to allow the TECAN robot to directly show / email to the user(s) via a text message / email
exactly to the user(s) what is the error, and how to diagnose it, and potential solutions'''

# API: Google Gmail (gmail)
# Used with express permission with BU CIDAR LAB (from Mary Pavan and Professor Douglas Densmore) 

# Guide: https://en.wikibooks.org/wiki/Python_Programming/Email

# Works, but faces a less secure app situations
# Figure out how to have a safer access to gmail 

import smtplib
#import math
#import os
#import sys
#import email

# Source: my own CS 108 project (the sendMail() function from final_project.py)
def sendMail(sender, recipient, msg):

    """Connect up to the SMTP server and send the message
        to from sender (the TECAN error server) to the recipient (user)"""

    # mailer object
    mailer = smtplib.STMP()

    # connect to the outgoing mail server (use BU for now)
    mailer.connect("acs-stp.bu.edu",25)

    # recipient
    rec = smtp.helo("USERNAME")
    print("Connected to SMTP server.")

    # message to send to the user
    rec = smtp.sendmail(sender,recipient,msg)
    print("Email was sent to %s" % recipient)

    msg = '''\nHello user! \nThe TECAN Robot is now running the script.
    \nThe following error(s) were detected:'''

    print("Message: %s" % msg)

    # goodbye to the user
    smtp.quit()
    print("Disconnected from the SMTP server.")

# must allow less secure apps in order to work

# create the server object
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# choose a more secure email later
server.login("jasonlu6@bu.edu","myson.AB.267")

# message
msg = '''\nHello user! \nThe TECAN Robot is now running the script.
\nThe following error(s) were detected:'''

# sending the mail
# attempt to send to Mary first 
server.sendmail("tecanserver@gmail.com","mapavan@bu.edu",msg)
server.quit() 

def main():
    # first try and send the message for Mary 
    sendMail("jasonlu6@bu.edu","mapavan@bu.edu","TECAN robot error")
main()

