import sys 
import argparse
import subprocess
import os
from datetime import datetime
import random
username="sanchayana2007"
token= os.environ.get("GIT_TOKEN")


#Random int to create the value 
j= random.randint(0,1)
################ RAndom file creator for chein in ##################
if j:
    if os.path.isfile("./tete"):
        output = subprocess.check_output("rm tete",shell = True, stderr=subprocess.STDOUT)
    else:
        output = subprocess.check_output("touch tete",shell = True, stderr=subprocess.STDOUT)
else:
    if os.path.isfile("./tete"):
        output = subprocess.check_output("rm tete",shell = True, stderr=subprocess.STDOUT)
################ RAndom file creator for chein in ##################


comment = "checking changes for " +  os.environ.get("USERNAME") + " "+ datetime.now().strftime("%b %d, %Y")  
print(comment)


if os.path.isdir("./.git"):

    print("The Folder is Already Intilaised with Git no need to init it ")

    
    CMD = " git status "
    print("###################  GIT STATUS ######################") 
    print("# In ./git/objects compare the staged files the cache#")   
    print("###################  #################################") 
    
    try: 
        output = subprocess.check_output(CMD,shell = True, stderr=subprocess.STDOUT)
    except subprocess.SubprocessError as e:
        print("Got and error",e)
    k= [ print(j) for i,j in enumerate(output.decode('utf-8').split('\n')) if i < 2 ]
  

    CMD = " git add --all "
    print("###################  GIT ADD in Staging Area ###################") 
    print("# In ./git/index is the Staged changes are kept as binary     #")   
    print("###################  ###########################################") 
    
    try: 
        output = subprocess.check_output(CMD,shell = True, stderr=subprocess.STDOUT)
    except subprocess.SubprocessError as e:
        print("Got and error",e)

    print(output.decode('utf-8'))
    

    CMD = " git commit -m " +  "\"" + comment + "\""
    print("###################  GIT COMMIT  in LOcal Repo  ###################") 
    print("#                       Local RFepository ./git/                  #")   
    print("###################  ##############################################") 
    
    try: 
        output = subprocess.check_output(CMD,shell = True, stderr=subprocess.STDOUT)
    except subprocess.SubprocessError as e:
        print("Got and error",e)
    print(output.decode('utf-8'))
    CMD = " git remote show origin  " 
    
    print("############  GIT show Branch Names Remote and Local  #########") 
    print("# It Shows the Name of the Barnch                             #")   
    print("##################  ###########################################") 
    try: 
        output = subprocess.check_output(CMD,shell = True, stderr=subprocess.STDOUT)
    except subprocess.SubprocessError as e:
        print("Got and error",e)
    print(output.decode('utf-8'))

    

    CMD = "cat  .git/refs/heads/master" 
    print("###################  GIT HEAD  pointer ###################") 
    print("# It Shows the Head id where the checkin will be done    #")   
    print("#############  ###########################################") 
    try: 
        output = subprocess.check_output(CMD,shell = True, stderr=subprocess.STDOUT)
    except subprocess.SubprocessError as e:
        print("Got and error",e)
    print(output.decode('utf-8'))
    

    if username and token:
        CMD = "git push  http://" + username + ":"+ token + "@github.com/sanchayana2007/HackerRanksTypesolutions.git"


        try :
            output = subprocess.check_output(CMD,shell = True, stderr=subprocess.STDOUT)
        except subprocess.SubprocessError as e:
            print("Got and error",e)
        print(output)
    
    else:
        print("Check the Useanme or Tone in Enviroment is not set")
    
else:
    print("Git Folder is not present.. Run from the main folder Exiting")