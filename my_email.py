#!/usr/bin/env python
# coding: utf-8

# In[1]:
# These are some functions to complete the twitter extraction.
# This file will be imported as a module in the main notebook.


def check_battery():
    """Checks the battery. It returns battery percentage as an integer."""
    # import the module
    import psutil
    
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    return battery.percent


def warning():
    """Send an email from my gmail account to myself warning on low battery.
    
    Add this function to the twitter long term retrieval function.
    It takes no arguments.
    """
    # import the necessary modules
    import os
    import smtplib
    from email.message import EmailMessage
    # set up some variables
    mail = 'jlopezfernandez112@gmail.com'
    py_gmail_password = os.environ.get('PyGmail')
    # message info
    msg = EmailMessage()
    msg['Subject'] = 'Battery Warning!!!'
    msg['From'] = mail
    msg['To'] = mail
    msg.set_content('You are running out of battery.\nBattery is at 20% or lower.\n\nGo charge it!')
    # send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(mail, py_gmail_password)
        smtp.send_message(msg)
        
    
def last_lap_reminder():
    """Send an email from my gmail account to myself reminding this is the last lap.
    
    45 mins aprox. to finish the extraction. 
    """
    # import the necessary modules
    import os
    import smtplib
    from email.message import EmailMessage
    # set up some variables
    mail = 'jlopezfernandez112@gmail.com'
    py_gmail_password = os.environ.get('PyGmail')
    # message info
    msg = EmailMessage()
    msg['Subject'] = 'Last lap remainder'
    msg['From'] = mail
    msg['To'] = mail
    msg.set_content('In 45 mins aprox. the extraction will be over.')
    # send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(mail, py_gmail_password)
        smtp.send_message(msg)
        
        
def error_email():
    """Send an email from my gmail account to myself informing an error has occurred.
    
    Probably because we exceeded the limit requests. It definitely should not. 
    """
    # import the necessary modules
    import os
    import smtplib
    from email.message import EmailMessage
    # set up some variables
    mail = 'jlopezfernandez112@gmail.com'
    py_gmail_password = os.environ.get('PyGmail')
    # message info
    msg = EmailMessage()
    msg['Subject'] = 'ERROR. Script has stopped.'
    msg['From'] = mail
    msg['To'] = mail
    msg.set_content('It probably has exceeded the limit requests.')
    # send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(mail, py_gmail_password)
        smtp.send_message(msg)
