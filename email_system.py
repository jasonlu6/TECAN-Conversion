# File: email_system.py
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

import smtplib
import math
import os
import sys
import email
# if necessary
# import cgi 

# import MIMETEXT and multiparts
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# iport email message
from email.message import EmailMessage 

# server class
class server():

    # create the server object
    # figure out the BU code (later)

    # unsecure access supported 
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # stuff to set up proper connection for sending mail
    server.ehlo()
    server.starttls()
    server.ehlo()

    # logging into the server
    # change the password later to something more secure 
    server.login("jasonlu6@bu.edu","password")

    # sending mail function
    def sendmail(msg,server):
        server = smtplib.SMTP('smtp.gmail.com.', 587)

        msg = '''
        \nHello user! 

        The TECAN Robot is now running the script.

        The following error(s) were detected:
        '''

        # use the STEM pathways mail for now
        server.sendmail('connect@stempathways.org')

    # make sure the server quits / exits after use
    server.quit()

# email class
class email():
    # same server object
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # basic message headers
    from_address = "jasonlu6@bu.edu"
    to_address = "connect@stempathways.org"
    # multi-part message 
    msg = MIMEMultipart()
    # CGI form format 
    msg['From'] = from_address
    msg['To'] = to_address
    # additional params
    msg['Cc'] = " "
    msg['Bcc'] = " "
    msg['Subject'] = "TECAN Error Message"

    # attach the body of email to the MIME message:
    body = '''
        \nHello user! 

        The TECAN Robot is now running the script.

        The following error(s) were detected:
        '''
    
    msg.attach(MIMEText(body, 'plain'))

    # get the text message
    text = msg.as_string()

    # send the mail
    server.sendmail(from_address, to_address, text) 




