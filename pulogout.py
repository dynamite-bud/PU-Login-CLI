#!/usr/bin/python


import os,sys
import getpass
import re    


def printResponse(response):
    logoutStr="Logout Successful"
    if logoutStr in response:
        print("Logout Successful")
    else:
        print("Error,User Not Logged In")



def logoutOfNetwork():
    myCmd="curl -k -# https://securelogin.pu.ac.in/cgi-bin/login?cmd=logout"
    res=os.popen(myCmd,'r')
    response=res.read()
    printResponse(response)

logoutOfNetwork()

    





