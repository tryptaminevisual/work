# this is a tool to automatize the proccess of Searching & Downloading documents from the common criteria portal
# Also helps organizing folders when needed and placing documents were it needs to be
# Check the website "https://www.commoncriteriaportal.org" for more information 

import os
import subprocess
from datetime import date
import sys
import webbrowser
from menu import show_menu_three
from menu import choose_sub_three
from menu import show_menu_one
from menu import download_all_files1
from menu import moving_files_one
from menu import moving_files_two
from menu import download_all_files
from menu import cool_search_local
import shutil


today = date.today()
host = "https://www.commoncriteriaportal.org/"
#check_ping = os.system('cmd /c "ping commoncriteriaportal.org"') // good website = 0
#check_ping2 = os.system('cmd /c "ping blababl.org"') // fake website = 1

print(50 * "-")
print("Welcome to the CC Tool..." + " " + str(today)) 
print(50 * "-")
print("Checking if the host is up and running") # We are going to ping the host to see if the site is available
print("The host is" + ":" + " " + host)
print(50 * "-")
input("press any key to check if the host is up....")
print("Checking ping...")
check_ping = os.system('cmd /c "ping commoncriteriaportal.org"')
result = check_ping
print(str(result))
a = result
if a == 0:
    print("\nHost is up!")
else:
    print("\nHost doesn't seem to be up, check manually!")
input("Press any key to continue to the menu...")
os.system("cls")

print(50 * "-")
print ("Menu")
print(50 * "-")
print("1: Open Web in browser")
print("2: About the CC")
print("3: Publications")
print("4: technical Communities")
print("5: Certified Products")
print("6: Collaborative Apps")
print("7: Protection Profiles")
print("8: ICCC")
print("9: News")
print("10 Search")
print("11: Exit")
print(50 * "-")

target = input("Enter number to access the menu:" + " ")
if target == "1":
    webbrowser.open("https://www.commoncriteriaportal.org/")
    show_menu_one()
    exit()
    
elif target == "2":
    webbrowser.open("https://www.commoncriteriaportal.org/ccra/index.cfm")
    show_menu_one()
    exit()
elif target == "3":
    os.system("cls")
    print(50 * "-")
    print("Publications")
    print(50 * "-")
    print("Sections")
    print("(1)-> New CC v3.1. Release 5")
    print("(2)CC v3.1. Release 4")
    print("(3)CC v3.1 Release 3")
    print("(4)CCRA Supporting Documents")
    print("(5)Supporting Documents related to Smart Cards and similar devices")
    print(50 * "-")
    print("(6)Go back")
    print(50 * "-")
    menu_3 = input("Enter the number you want to access:" + " ")
    if menu_3 == "1":
        os.system("cls")
        show_menu_three()
        choose_sub_three()
    elif menu_3 == "6":
        os.system("cls")
        show_menu_one()
    elif menu_3 == "11":
        exit()
elif target == "10": # Search locally
    os.system("cls")
    print(50 * "-")
    print("Search options")
    print(50 * "-")
    print("Search localy (1)")
    print("Search on CSV file (2)")
    print(50 * "-")
    print("Go back to main menu (3)")
    print(50 * "-")
    search_option = input("Select type of search you fancy:" + " ")
    if search_option == "1":
        cool_search_local()
    elif target == "2":
        print("Here we will show the CSV search bar options")
    else:
        os.system("cls")
        show_menu_one()
else:
    print("Bye")