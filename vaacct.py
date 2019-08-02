#!/usr/bin/env python
########## Vaacct User account creation##########
#########                      ##################
#########
#########Author: Sayi krishna  ##################
########Version: 1.0           ###################
########Date : 10-06-2019 ###########

import sys
import os
import platform
import datetime
try:
    import subprocess
except Exception as e:
    logging.info("subprocess module is not imported")
try:
    import logging
except Exception as e:
    logging.info("logging module is not imported")


Redhat = 2.6
OEL = 2.6
SuSE11 = "11"
SuSE10 = "10"
SuSE9 = "9"
RE = "Redhat"
USER='vaacct'
USERID='67375'
GRPID='100'
DESC='ISRM USER'
root = 'root'
PHASH='-p$6$d2mAv3qJ$n9rIbXZGKnCDaKLo.Dl8AygZib.68qzWPcstkSFBWxCYGaFQkpmOLx393itdI7LDKkpkatYAjQnSeNwlgP6KX1'
SLES10HASH='$1$R5v4ywF9$JtlYubaTLgBgroQlqjOM50'
SLES9HASH='$1$.FxzWzzz$LJfuTg6Am1AE4jd9V3smp/'

def OS_chk():
       if os.path.exists("/etc/TR-release-MOE"):
           if Redhat  >= float(platform.release()[0:3]):
                    return Redhat
       elif os.path.exists("/etc/TR-release"):
            if Redhat  >= float(platform.release()[0:3]):
                    return OEL
       elif os.path.exists("/etc/redhat-release"):
           with open("/etc/redhat-release") as file:
                data = file.readlines()
                if 7.0  <= data[0][36:37]:
                    print ("Old version REDHAT is running. This script won't work in this OS")
                    sys.exit(1)
       elif os.path.exists("/etc/SuSE-release"):
           with open("/etc/SuSE-release") as file:
                data = file.readlines()
                if SuSE11  == data[0][29:31]:
                    print ("SUSE 11 is running. This script won't work in this OS")
                    sys.exit(1)
       elif os.path.exists("/etc/SuSE-release"):
           with open("/etc/SuSE-release") as file:
                data = file.readlines()
                if SuSE10  == data[0][29:31]:
                    print ("SUSE 10 is running. This script won't work in this OS")
       elif os.path.exists("/etc/SuSE-release"):
           with open("/etc/SuSE-release") as file:
                data = file.readlines()
                if SuSE9  == data[0][29:30]:
                   print ("SUSE is running. This script won't work in this OS")
                   sys.exit(1)

       else:
           print ("This Scipt works only on OLE and REDHAT Linux OS")
           sys.exit(1)

OS = OS_chk()

def User_Validate():
         with open('/etc/passwd') as f:
             for lines in f:
                  line = lines.split(':')
                  if USER  == line[0]:
                      print ("VAACCT user validation is OK")
                      try:
                          subprocess.call(["userdel","-r",USER])
                          logging.info(" User delete command is executed")
                          subprocess.call(["rm","-rf","/etc/sudoers.d/10_vaacct"])
                          logging.info(" sudo file is remove from /etc/sudero.d/10_vaacct")
                          print("VAACCT user Cleanup is completed")
                          logging.info("EXIT CODE 0")
                          return USER
                      except:
                          logging.info("Unable to remove VAACCT user")
                          logging.info("EXIT CODE 1")




#user = User_Validate()
#print user
def grp_Validate():
       with open('/etc/group') as f:
            for lines in f:
                  line = lines.split(':')
                  if '100' ==  line[2]:
                      #print line[2]
                      return True


group = grp_Validate()


sudoers = """# vaact Sudoers - QCMD
Cmnd_Alias      QCMD=/bin/su
vaacct          ALL=QCMD
"""

def Sudo_access():
     with open('/etc/sudoers.d/10_vaacct','w') as sudo:
          sudo.write(sudoers)
          sudo.close()

def Add_User():
     if Redhat >= OS:
        if True:
          try:
              subprocess.call(["useradd","-m","-d/home/vaacct",PHASH,"-g 100","-u 67375","-c 'ISRM USER'",USER])
              logging.info(" User add command is executed ")
              Sudo_access()
              logging.info(" Sudo access configured for vaacct User")
              print ("VAACCT user account is created and grated SUDO access")
              logging.info("EXIT CODE 0")
          except:
              logging.info("Useradd command is not executed ")
              print("Unable to created VAACCT account. See /var/tmp/Add_Vaacct_User* logs for more information")
              logging.info("EXIT CODE 1")

     elif OEL >= OS:
        if True:
          try:
              subprocess.call(["useradd","-m","-d/home/vaacct",PHASH,"-g 100","-u 67375","-c 'ISRM USER'",USER])
              logging.info(" User add command is executed ")
              Sudo_access()
              logging.info(" Sudo access configured for vaacct User")
              print ("VAACCT user account is created and grated SUDO access")
              logging.info("EXIT CODE 0")
          except:
              logging.info(" User add command is not executed ")
              print("Unable to created VAACCT account. See /var/tmp/Add_Vaacct_User* logs for more information")
              logging.info("EXIT CODE 1")


def Add_group():
       if group:
           print("'Users' Group exist")
       else:
           try:
              subprocess.call(["groupadd","-g 100","users"])
              logging.info("Group add command is  executed ")
              print("GID 100 not found hence added now")
              logging.info("EXIT CODE 0")
           except:
              logging.info("Group add command is not  executed ")
              print("Unable to create Group 'users'.See /var/tmp/Add_Vaacct_User* logs for more information")
              logging.info("EXIT CODE 1")
'''
def Cleanup():
    logging.info(" User Cleanup function is executed")
    if Redhat >= OS:
         if user == USER:
           try:
              subprocess.call(["userdel","-r",USER])
              logging.info(" User delete command is executed")
              subprocess.call(["rm","-rf","/etc/sudoers.d/10_vaacct"])
              logging.info(" sudo file is remove from /etc/sudero.d/10_vaacct")
              print("VAACCT user Cleanup is completed")
              logging.info("EXIT CODE 0")
           except:
              logging.info("Unable to remove VAACCT user")
              logging.info("EXIT CODE 1")
'''

remote_job = '''
import os
import sys
import datetime
import logging
import subprocess

now = datetime.datetime.now()
remove_script_name = os.path.basename(sys.argv[0])
logdir = "/var/tmp"
logfile =  logdir+"/"+remove_script_name+"_"+now.strftime("%Y%m%d%H%M%S")
logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
logging.info("%s Main program Start", remove_script_name)

USER = "vaacct"

def remove_user():
     with open('/etc/passwd') as f:
          for lines in f:
               line = lines.split(':')
               if USER  == line[0]:
                  subprocess.call(["userdel","-r",USER])
                  logging.info(" User delete command is executed")
                  subprocess.call(["rm","-rf","/etc/sudoers.d/10_vaacct"])
                  logging.info(" sudo file is remove from /etc/sudero.d/10_vaacct")
remove_user()
'''

def remove_user():
    with open('/var/tmp/remote_user.py','w') as file:
         file.write(remote_job)
         file.close()

def At_job():
     print ("Creating User remove Job")
     remove_user()
     subprocess.call(["at","-f","/var/tmp/remote_user.py","now","+","7days"])
     print("AT successufully schduled for 7 days")

def Final_Validate():
         with open('/etc/passwd') as f:
             for lines in f:
                  line = lines.split(':')
                  if 'vaacct'  == line[0]:
                      print ("VAACCT user Final validation is OK")


####Main Programs#####


now = datetime.datetime.now()
#base_script_name = os.path.basename(sys.argv[0])
base_script_name = "Add_vaacct_user"
logdir = "/var/tmp"
logfile =  logdir+"/"+ base_script_name +"_"+now.strftime("%Y%m%d%H%M%S")
logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
logging.info(" Main program Start")
try:
       Add_group()
       User_Validate()
       Add_User()
       logging.info(" %s  add funcion called",USER )
       At_job()
       Final_Validate()

except:
       logging.info("Unable to created VAACCT account. See /var/tmp/Add_Vaacct_User* logs for more information")
       sys.exit(1)
