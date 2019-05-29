#!/usr/bin/python


import os,sys
import json
import getpass
import re


filepath="/home/rudra/Documents/Portal Login_files/data.json"

def fileExists(path):
    return os.path.isfile(path)

def fileIsEmpty(path):
    return os.stat(path).st_size==0

if(fileExists(filepath)==False):
    os.mknod(filepath)

print("PU LOGIN CLI\n")


data={
        "user": "",
        "password": ""
        }
loginstr1="Login=Log%20In&cmd=authenticate&password="
loginstr2="&user="

if(fileIsEmpty(filepath)):
    print("Hello, No Users Present.\nPlease enter a default username and password.\n")
    user=input("Enter Username:\t")
    password=getpass.getpass(prompt="Enter Password:\t")
    try:
        data["user"]=user
        data["password"]=password
        f=open(filepath,"w")
        f.write(json.dumps(data))
        f.close()
    except IOError:
        print("Error creating file")





if(fileIsEmpty(filepath)!=True):
    try:
        f=open(filepath,"r")
        dataArg=f.read()
        dataArg=json.loads(dataArg)
        f.close()
    except IOError:
        print("Error loading file")
    
def printResponse(response):
    loginStr=" External Welcome Page"
    if loginStr in response:
        print("Login Successful")
    else:
        pat1=re.compile("<div id=\"errorbox\" style=\"\">([\s\w]+)<\/div>")
        strin=pat1.findall(response)
        pat2=re.compile("\w+\s\w+")
        ans=pat2.findall(strin[0])
        if(str(ans[0])=="\n\t\t" or ans[0]==None):
            print("NULL response from server.\nPlease try again.")
        else:
            print(str(ans[0]))



def loginToNetwork():
    print("Hello user, logging in with ID\t"+dataArg.get("user"))
    loginstr=loginstr1+dataArg.get("password")+loginstr2+dataArg.get("user")
    myCmd="curl -# -k --data \""+loginstr+"\" https://securelogin.pu.ac.in/cgi-bin/login"
    res=os.popen(myCmd,'r')
    response=res.read()
    printResponse(response)

loginToNetwork()

    





