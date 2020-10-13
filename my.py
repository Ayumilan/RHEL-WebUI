#! /usr/bin/python3

print("content-type: text/html")
print()

import subprocess
import cgi

form=cgi.FieldStorage()
cmd=form.getvalue("x")


if(("man" not in cmd) and ("ip" in cmd) or ("ip address" in cmd) or ("ifconfig" in cmd)):
    a=subprocess.getoutput('ifconfig')
elif(("man" not in cmd) and ("date" in cmd)):
    a=subprocess.getoutput('date')
elif(("man" not in cmd) and ("ls" in cmd) or ("list" in cmd)):
    a=subprocess.getoutput('ls')
elif(("man" not in cmd) and ("pwd" in cmd) or ("folder" in cmd) or ("directory" in cmd)) :
    a=subprocess.getoutput('pwd')
elif(("manual" in cmd) or ("man" in cmd) and ("date" in cmd)) :
    a=subprocess.getoutput('man date')
elif(("manual" in cmd) or ("man" in cmd) and ("cal" in cmd)) :
    a=subprocess.getoutput('man cal')
elif(("manual" in cmd) or ("man" in cmd)and ("ls" in cmd)) :
    a=subprocess.getoutput('man ls')
elif(("manual" in cmd) or ("man" in cmd)and ("pwd" in cmd)) :
    a=subprocess.getoutput('man pwd')
elif(("man" not in cmd) and ("cal" in cmd) or ("calender" in cmd)):
    a=subprocess.getoutput('cal')
else:
    print("Don't understand")
print(a)
