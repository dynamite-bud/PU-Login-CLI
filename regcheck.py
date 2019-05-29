import re


myFile=open("failresp.txt","r")

resp=myFile.read()
loginStr=" External Welcome Page"
if loginStr in resp:
    print("Login Successful")
else:
    pat1=re.compile("<div id=\"errorbox\" style=\"\">([\s\w]+)<\/div>")
    strin=pat1.findall(resp)
    pat2=re.compile("\w+\s\w+")
    ans=pat2.findall(strin[0])
    if(str(ans[0])=="\n\t\t" or ans[0]==None):
        print("NULL response from server.\nPlease try again.")
    else:
        print(str(ans[0]))

