import os
import time

red='\033[31m'
green='\033[32m'
blue='\033[36m'
pink='\033[35m'
rang='\033[34m'

os.system("clear")
print ( green + "pleas wait to install tools ...")
time.sleep(1)
os.system("clear")
print ( green + "pleas wait to install tools ..")
time.sleep(1)
os.system("clear")
print ( green + "pleas wait to install tools ...")
time.sleep(1)
os.system("clear")
print ( green + "pleas wait to install tools ..")
time.sleep(1)
os.system("clear")
print ( green + "pleas wait to install tools ...")
time.sleep(1)
os.system("clear")
print (f"{blue}")

os.system("pkg install git -y ")
os.system("apt update")
os.system("apt upgrade")
os.system("pkg install requests -y ")

print (f"{rang}")
