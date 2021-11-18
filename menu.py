import os
import sys
import subprocess
import webbrowser
import shutil
import curses
import time
from colorama import Fore


def download_all_files1():
    os.system("cls")
    print(60 * "-")
    print("Starting to download all files and placing them in the right folder")
    print(60 * "-")
    input("Press any key to start the download proccess:" + " ")
    os.system("cls")
    print(50 * "-")
    print("Downloading...")
    print(50 * "-")
    os.system("curl.exe -o CCPART1V3.1R5.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART1V3.1R5.pdf") # Downloading first file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CCPART1V3.1R5_marked_changes.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART1V3.1R5_marked_changes.pdf") # Downloading 2nd file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CCPART2V3.1R5.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART2V3.1R5.pdf") # Downloading 3rd file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CCPART2V3.1R5_marked_changes.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART2V3.1R5_marked_changes.pdf") # Downloading 4th file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CCPART3V3.1R5.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART3V3.1R5.pdf") # Downloading 5th file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CCPART3V3.1R5_marked_changes.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART3V3.1R5_marked_changes.pdf") # Downloading 6th file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CEMV3.1R5.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CEMV3.1R5.pdf") # Downloading 7th file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CEMV3.1R5_marked_changes.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CEMV3.1R5_marked_changes.pdf") # Downloading 8th file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf") # Downloading 9th file
    print(50 * "-")
    print("Download complete")
    print(50 * "-")
    input("Press any key to move the downloads to the respective folder:" + " ")
    os.system("cls")
    moving_files_one()
    exit()


def moving_files_one():
    src_file_1 = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART1V3.1R5.pdf'
    des_file_1 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_1, des_file_1) # First file moved
    src_file_2 = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART1V3.1R5_marked_changes.pdf'
    des_file_2 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_2, des_file_2) # 2nd file moved
    src_file_3 = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART2V3.1R5.pdf'
    des_file_3 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_3, des_file_3) # 3rd file moved
    src_file_4 = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART2V3.1R5_marked_changes.pdf'
    des_file_4 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_4, des_file_4) # 4th file moved
    src_file_5 = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART3V3.1R5.pdf'
    des_file_5 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_5, des_file_5) # 5th file moved
    src_file_6 = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART3V3.1R5_marked_changes.pdf'
    des_file_6 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_6, des_file_6) # 6th file moved
    src_file_7 = 'C:/Users/Adolfo/Desktop/tools/CC/CEMV3.1R5.pdf'
    des_file_7 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_7, des_file_7) # 7th file moved
    src_file_8 = 'C:/Users/Adolfo/Desktop/tools/CC/CEMV3.1R5_marked_changes.pdf'
    des_file_8 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_8, des_file_8) # 8th file moved
    src_file_9 = 'C:/Users/Adolfo/Desktop/tools/CC/CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf'
    des_file_9 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_9, des_file_9) # 9th file moved
    print(50 * "-")
    print("All the PDFs have been moved!")
    print(50 * "-")
    input("Press any key to go back to the main menu:" + " ")
    os.system("cls")
    show_menu_one()

def moving_files_two():
    src_file_one = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART1V3.1R5.pdf'
    des_file_one = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_one, des_file_one) # First file moved
    src_file_two = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART1V3.1R5_marked_changes.pdf'
    des_file_two = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_two, des_file_two) # 2nd file moved
    src_file_three = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART2V3.1R5.pdf'
    des_file_three = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_three, des_file_three) # 3rd file moved
    src_file_four = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART2V3.1R5_marked_changes.pdf'
    des_file_four = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_four, des_file_four) # 4th file moved
    src_file_five = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART3V3.1R5.pdf'
    des_file_five = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_five, des_file_five) # 5th file moved
    src_file_six = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART3V3.1R5_marked_changes.pdf'
    des_file_six = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_six, des_file_six) # 6th file moved
    src_file_seven = 'C:/Users/Adolfo/Desktop/tools/CC/CEMV3.1R5.pdf'
    des_file_seven = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_seven, des_file_seven) # 7th file moved
    src_file_eight = 'C:/Users/Adolfo/Desktop/tools/CC/CEMV3.1R5_marked_changes.pdf'
    des_file_eight = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_eight, des_file_eight) # 8th file moved
    src_file_nine = 'C:/Users/Adolfo/Desktop/tools/CC/CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf'
    des_file_nine = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_nine, des_file_nine) # 9th file moved
    src_file_ten = 'C:/Users/Adolfo/Desktop/tools/CC/cc3R5.XML.zip' 
    des_file_ten = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_ten, des_file_ten) # 10th file moved (.ZIP)
    src_file_eleven = 'C:/Users/Adolfo/Desktop/tools/CC/CC3R3.dtd'
    des_file_eleven = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
    shutil.move(src_file_eleven, des_file_eleven) # 11th file moved (DTD) 
    print(50 * "-")
    print("All the PDFs & Other files have been moved!")
    print(50 * "-")
    input("Press any key to go back to the main menu:" + " ")
    os.system("cls")
    show_menu_one()

def download_all_files():
    os.system("cls")
    print(60 * "-")
    print("Starting to download all files and placing them in the right folder")
    print(60 * "-")
    input("Press any key to start the download proccess:" + " ")
    os.system("cls")
    print(50 * "-")
    print("Downloading...")
    print(50 * "-")
    os.system("curl.exe -o CCPART1V3.1R5.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART1V3.1R5.pdf") # Downloading first file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CCPART1V3.1R5_marked_changes.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART1V3.1R5_marked_changes.pdf") # Downloading 2nd file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CCPART2V3.1R5.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART2V3.1R5.pdf") # Downloading 3rd file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CCPART2V3.1R5_marked_changes.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART2V3.1R5_marked_changes.pdf") # Downloading 4th file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CCPART3V3.1R5.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART3V3.1R5.pdf") # Downloading 5th file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CCPART3V3.1R5_marked_changes.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART3V3.1R5_marked_changes.pdf") # Downloading 6th file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CEMV3.1R5.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CEMV3.1R5.pdf") # Downloading 7th file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CEMV3.1R5_marked_changes.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CEMV3.1R5_marked_changes.pdf") # Downloading 8th file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf") # Downloading 9th file
    print(50 * "-")
    print(50 * "-")
    print("Downloading DTDs & XML")
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o cc3R5.XML.zip --url https://www.commoncriteriaportal.org/files/ccfiles/cc3R5.XML.zip") # Downloading .ZIP file
    print(50 * "-")
    print(50 * "-")
    os.system("curl.exe -o CC3R3.dtd --url https://www.commoncriteriaportal.org/files/ccfiles/CC3R3.dtd") # Downloading DTDs
    print(50 * "-")
    print(50 * "-")
    print("Download complete")
    print(50 * "-")
    input("Press any key to move the downloads to the respective folder:" + " ")
    os.system("cls")
    moving_files_two()
    exit()

def show_menu_one(): # Menu one
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
    elif target == "2":
        webbrowser.open("https://www.commoncriteriaportal.org/ccra/index.cfm")
    elif target == "11":
        print("Shutting down program.")
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
            show_menu_one()
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
    menu_3 = input("Enter the section you want to access:" + " ")
    if menu_3 == "1":
        os.system("cls")
        show_menu_three()
        choose_sub_three()
    elif menu_3 == "6":
        os.system("cls")
        show_menu_one()

def show_menu_three():
    print("CC v3.1 Release 5 consists of three parts. Make sure to download and use these files.")
    print("this is a list of the PDFs available to download:")
    print(50 * "-")
    print("-> CCPART1V3.1R5.pdf(1)")
    print("-> CCPART1V3.1R5_marked_changes.pdf(2)")
    print("-> CCPART2V3.1R5.pdf(3)")
    print("-> CCPART2V3.1R5_marked_changes.pdf(4)")
    print("-> CCPART3V3.1R5.pdf(5)")
    print("-> CCPART3V3.1R5_marked_changes.pdf(6)")
    print("-> CEMV3.1R5.pdf(7)")
    print("-> CEMV3.1R5_marked_changes.pdf(8)")
    print("-> CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf(9)")
    print(50 * "-")
    print("XML")
    print(50 * "-")
    print("-> CC3R3.dtd(10)")
    print("-> cc3R4.XML.zip(11)")
    print(50 * "-")
    print("Download all PDFs(12)")
    print(50 * "-")
    print("Downloads all files (PDFs & XML files)(13)")
    print(50 * "-")
    print("Go back(14)")
    print(50 * "-")

def choose_sub_three():
    selection = (input("Select what would you like to view/download:" + " "))
    if selection == "1": # CCPART1V3.1R5.pdf(1)
        os.system("cls")
        print(50 * "-")
        print("What would you like to do?")
        print(50 * "-")
        print("-> Download(1)")
        print("-> View online(2)")
        print(50 * "-")
        selection_one = (input("Please select your option:" + " "))
        if selection_one == "1":
            print(50 * "-")
            print("Your download will start shortly...")
            print(50 * "-")
            print("Before downloading, do you want to check it has been previously downloaded?")
            download_activation = input("Y(1)/N(2):" + " ")
            if download_activation == "1":
                print("Running check, wait a moment...")
                print(50 * "-")
                path_exists = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CCPART1V3.1R5.pdf")
                if os.path.exists(path_exists) == "CCPART1V3.1R5.pdf":
                    print("Yes, file already downloaded, theres no need to download, check your folder.")
                else:
                    print("File doesnt exist, starting download now")
                print(50 * "-")
                print(input("Press enter to start download:" + " "))
                os.system("cls")
                print("Preparing download...")
                print(50 * "-")
                os.system("curl.exe -o CCPART1V3.1R5.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART1V3.1R5.pdf")
                print(50 * "-")
                print("Download complete")
                src1 = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART1V3.1R5.pdf'
                des1 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
                shutil.move(src1, des1)
                print("Done")
                print(50 * "-")
                input("Press any key to go back to the main menu:" + " ")
                print(50 * "-")
                os.system("cls")
                show_menu_one()
        elif selection_one == "2":
            os.system("cls")
            print(50 * "-")
            input("Press any key to open PDF in browswer:" + " ")
            print(50 * "-")
            webbrowser.open("https://www.commoncriteriaportal.org/files/ccfiles/CCPART1V3.1R5.pdf")
            show_menu_one()
            os.system("cls")
            exit()
    elif selection == "2": # CCPART1V3.1R5_marked_changes.pdf(2)
        os.system("cls")
        print(50 * "-")
        print("What would you like to do?")
        print(50 * "-")
        print("-> Download(1)")
        print("-> View online(2)")
        print(50 * "-")
        selection_one = (input("Please select your option:" + " "))
        if selection_one == "1":
            print(50 * "-")
            print("Your download will start shortly...")
            print(50 * "-")
            print("Before downloading, do you want to check it has been previously downloaded?")
            download_activation = input("Y(1)/N(2):" + " ")
            if download_activation == "1":
                print("Running check, wait a moment...")
                print(50 * "-")
                path_exists = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CCPART1V3.1R5_marked_changes.pdf")
                if os.path.exists(path_exists) == "CCPART1V3.1R5_marked_changes.pdf":
                    print("Yes, file already downloaded, theres no need to download, check your folder.")
                else:
                    print("File doesnt exist, starting download now")
                print(50 * "-")
                print(input("Press enter to start download:" + " "))
                os.system("cls")
                print("Preparing download...")
                print(50 * "-")
                os.system("curl.exe -o CCPART1V3.1R5_marked_changes.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART1V3.1R5_marked_changes.pdf")
                print(50 * "-")
                print("Download complete")
                src2 = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART1V3.1R5_marked_changes.pdf'
                dest2 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
                shutil.move(src2, dest2)
                print("Done")
                print(50 * "-")
                input("Press any key to go back to the main menu:" + " ")
                print(50 * "-")
                os.system("cls")
                show_menu_one()
        elif selection_one == "2":
            os.system("cls")
            print(50 * "-")
            input("Press any key to open PDF in browswer:" + " ")
            print(50 * "-")
            webbrowser.open("https://www.commoncriteriaportal.org/files/ccfiles/CCPART1V3.1R5_marked_changes.pdf")
            show_menu_one()
            os.system("cls")
            exit()
    elif selection == "3": # CCPART2V3.1R5.pdf(3)
        os.system("cls")
        print(50 * "-")
        print("What would you like to do?")
        print(50 * "-")
        print("-> Download(1)")
        print("-> View online(2)")
        print(50 * "-")
        selection_one = (input("Please select your option:" + " "))
        if selection_one == "1":
            print(50 * "-")
            print("Your download will start shortly...")
            print(50 * "-")
            print("Before downloading, do you want to check it has been previously downloaded?")
            download_activation = input("Y(1)/N(2):" + " ")
            if download_activation == "1":
                print("Running check, wait a moment...")
                print(50 * "-")
                path_exists = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CCPART2V3.1R5.pdf")
                if os.path.exists(path_exists) == "CCPART2V3.1R5.pdf":
                    print("Yes, file already downloaded, theres no need to download, check your folder.")
                else:
                    print("File doesnt exist, starting download now")
                print(50 * "-")
                print(input("Press enter to start download:" + " "))
                os.system("cls")
                print("Preparing download...")
                print(50 * "-")
                os.system("curl.exe -o CCPART2V3.1R5.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART2V3.1R5.pdf")
                print(50 * "-")
                print("Download complete")
                src3 = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART2V3.1R5.pdf'
                dest3 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
                shutil.move(src3, dest3)
                print("Done")
                print(50 * "-")
                input("Press any key to go back to the main menu:" + " ")
                print(50 * "-")
                os.system("cls")
                show_menu_one()
        elif selection_one == "2":
            os.system("cls")
            print(50 * "-")
            input("Press any key to open PDF in browswer:" + " ")
            print(50 * "-")
            webbrowser.open("https://www.commoncriteriaportal.org/files/ccfiles/CCPART2V3.1R5.pdf")
            show_menu_one()
            os.system("cls")
            exit()
    elif selection == "4": #CCPART2V3.1R5_marked_changes.pdf(4)
        os.system("cls")
        print(50 * "-")
        print("What would you like to do?")
        print(50 * "-")
        print("-> Download(1)")
        print("-> View online(2)")
        print(50 * "-")
        selection_one = (input("Please select your option:" + " "))
        if selection_one == "1":
            print(50 * "-")
            print("Your download will start shortly...")
            print(50 * "-")
            print("Before downloading, do you want to check it has been previously downloaded?")
            download_activation = input("Y(1)/N(2):" + " ")
            if download_activation == "1":
                print("Running check, wait a moment...")
                print(50 * "-")
                path_exists = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CCPART2V3.1R5_marked_changes.pdf")
                if os.path.exists(path_exists) == "CCPART2V3.1R5_marked_changes.pdf":
                    print("Yes, file already downloaded, theres no need to download, check your folder.")
                else:
                    print("File doesnt exist, starting download now")
                print(50 * "-")
                print(input("Press enter to start download:" + " "))
                os.system("cls")
                print("Preparing download...")
                print(50 * "-")
                os.system("curl.exe -o CCPART2V3.1R5_marked_changes.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART2V3.1R5_marked_changes.pdf")
                print(50 * "-")
                print("Download complete")
                src4 = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART2V3.1R5_marked_changes.pdf'
                dest4 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
                shutil.move(src4, dest4)
                print("Done")
                print(50 * "-")
                input("Press any key to go back to the main menu:" + " ")
                print(50 * "-")
                os.system("cls")
                show_menu_one()
        elif selection_one == "2":
            os.system("cls")
            print(50 * "-")
            input("Press any key to open PDF in browswer:" + " ")
            print(50 * "-")
            webbrowser.open("https://www.commoncriteriaportal.org/files/ccfiles/CCPART2V3.1R5_marked_changes.pdf")
            show_menu_one()
            os.system("cls")
            exit()
    elif selection == "5": # CCPART3V3.1R5.pdf(5)
        os.system("cls")
        print(50 * "-")
        print("What would you like to do?")
        print(50 * "-")
        print("-> Download(1)")
        print("-> View online(2)")
        print(50 * "-")
        selection_one = (input("Please select your option:" + " "))
        if selection_one == "1":
            print(50 * "-")
            print("Your download will start shortly...")
            print(50 * "-")
            print("Before downloading, do you want to check it has been previously downloaded?")
            download_activation = input("Y(1)/N(2):" + " ")
            if download_activation == "1":
                print("Running check, wait a moment...")
                print(50 * "-")
                path_exists = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CCPART3V3.1R5.pdf")
                if os.path.exists(path_exists) == "CCPART3V3.1R5.pdf":
                    print("Yes, file already downloaded, theres no need to download, check your folder.")
                else:
                    print("File doesnt exist, starting download now")
                print(50 * "-")
                print(input("Press enter to start download:" + " "))
                os.system("cls")
                print("Preparing download...")
                print(50 * "-")
                os.system("curl.exe -o CCPART3V3.1R5.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART3V3.1R5.pdf")
                print(50 * "-")
                print("Download complete")
                src5 = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART3V3.1R5.pdf '
                dest5 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
                shutil.move(src5, dest5)
                print("Done")
                print(50 * "-")
                input("Press any key to go back to the main menu:" + " ")
                print(50 * "-")
                os.system("cls")
                show_menu_one()
        elif selection_one == "2":
            os.system("cls")
            print(50 * "-")
            input("Press any key to open PDF in browswer:" + " ")
            print(50 * "-")
            webbrowser.open("https://www.commoncriteriaportal.org/files/ccfiles/CCPART3V3.1R5.pdf")
            show_menu_one()
            os.system("cls")
            exit()
    elif selection == "6": # CCPART3V3.1R5_marked_changes.pdf(6)
        os.system("cls")
        print(50 * "-")
        print("What would you like to do?")
        print(50 * "-")
        print("-> Download(1)")
        print("-> View online(2)")
        print(50 * "-")
        selection_one = (input("Please select your option:" + " "))
        if selection_one == "1":
            print(50 * "-")
            print("Your download will start shortly...")
            print(50 * "-")
            print("Before downloading, do you want to check it has been previously downloaded?")
            download_activation = input("Y(1)/N(2):" + " ")
            if download_activation == "1":
                print("Running check, wait a moment...")
                print(50 * "-")
                path_exists = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CCPART3V3.1R5_marked_changes.pdf")
                if os.path.exists(path_exists) == "CCPART3V3.1R5_marked_changes.pdf":
                    print("Yes, file already downloaded, theres no need to download, check your folder.")
                else:
                    print("File doesnt exist, starting download now")
                print(50 * "-")
                print(input("Press enter to start download:" + " "))
                os.system("cls")
                print("Preparing download...")
                print(50 * "-")
                os.system("curl.exe -o CCPART3V3.1R5_marked_changes.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCPART3V3.1R5_marked_changes.pdf")
                print(50 * "-")
                print("Download complete")
                src6 = 'C:/Users/Adolfo/Desktop/tools/CC/CCPART3V3.1R5_marked_changes.pdf'
                dest6 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
                shutil.move(src6, dest6)
                print("Done")
                print(50 * "-")
                input("Press any key to go back to the main menu:" + " ")
                print(50 * "-")
                os.system("cls")
                show_menu_one()
        elif selection_one == "2":
            os.system("cls")
            print(50 * "-")
            input("Press any key to open PDF in browswer:" + " ")
            print(50 * "-")
            webbrowser.open("https://www.commoncriteriaportal.org/files/ccfiles/CCPART3V3.1R5_marked_changes.pdf")
            show_menu_one()
            os.system("cls")
            exit()
    elif selection == "7": #CEMV3.1R5.pdf(7)
        os.system("cls")
        print(50 * "-")
        print("What would you like to do?")
        print(50 * "-")
        print("-> Download(1)")
        print("-> View online(2)")
        print(50 * "-")
        selection_one = (input("Please select your option:" + " "))
        if selection_one == "1":
            print(50 * "-")
            print("Your download will start shortly...")
            print(50 * "-")
            print("Before downloading, do you want to check it has been previously downloaded?")
            download_activation = input("Y(1)/N(2):" + " ")
            if download_activation == "1":
                print("Running check, wait a moment...")
                print(50 * "-")
                path_exists = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CEMV3.1R5.pdf")
                if os.path.exists(path_exists) == "CEMV3.1R5.pdf":
                    print("Yes, file already downloaded, theres no need to download, check your folder.")
                else:
                    print("File doesnt exist, starting download now")
                print(50 * "-")
                print(input("Press enter to start download:" + " "))
                os.system("cls")
                print("Preparing download...")
                print(50 * "-")
                os.system("curl.exe -o CEMV3.1R5.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CEMV3.1R5.pdf")
                print(50 * "-")
                print("Download complete")
                src7 = 'C:/Users/Adolfo/Desktop/tools/CC/CEMV3.1R5.pdf'
                dest7 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
                shutil.move(src7, dest7)
                print("Done")
                print(50 * "-")
                input("Press any key to go back to the main menu:" + " ")
                print(50 * "-")
                os.system("cls")
                show_menu_one()
        elif selection_one == "2":
            os.system("cls")
            print(50 * "-")
            input("Press any key to open PDF in browswer:" + " ")
            print(50 * "-")
            webbrowser.open("https://www.commoncriteriaportal.org/files/ccfiles/CEMV3.1R5.pdf")
            show_menu_one()
            os.system("cls")
            exit()
    elif selection == "8": # CEMV3.1R5_marked_changes.pdf(8)
        os.system("cls")
        print(50 * "-")
        print("What would you like to do?")
        print(50 * "-")
        print("-> Download(1)")
        print("-> View online(2)")
        print(50 * "-")
        selection_one = (input("Please select your option:" + " "))
        if selection_one == "1":
            print(50 * "-")
            print("Your download will start shortly...")
            print(50 * "-")
            print("Before downloading, do you want to check it has been previously downloaded?")
            download_activation = input("Y(1)/N(2):" + " ")
            if download_activation == "1":
                print("Running check, wait a moment...")
                print(50 * "-")
                path_exists = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CEMV3.1R5_marked_changes.pdf")
                if os.path.exists(path_exists) == "CEMV3.1R5_marked_changes.pdf":
                    print("Yes, file already downloaded, theres no need to download, check your folder.")
                else:
                    print("File doesnt exist, starting download now")
                print(50 * "-")
                print(input("Press enter to start download:" + " "))
                os.system("cls")
                print("Preparing download...")
                print(50 * "-")
                os.system("curl.exe -o CEMV3.1R5_marked_changes.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CEMV3.1R5_marked_changes.pdf")
                print(50 * "-")
                print("Download complete")
                src8 = 'C:/Users/Adolfo/Desktop/tools/CC/CEMV3.1R5_marked_changes.pdf'
                dest8 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
                shutil.move(src8, dest8)
                print("Done")
                print(50 * "-")
                input("Press any key to go back to the main menu:" + " ")
                print(50 * "-")
                os.system("cls")
                show_menu_one()
        elif selection_one == "2":
            os.system("cls")
            print(50 * "-")
            input("Press any key to open PDF in browswer:" + " ")
            print(50 * "-")
            webbrowser.open("https://www.commoncriteriaportal.org/files/ccfiles/CEMV3.1R5_marked_changes.pdf")
            show_menu_one()
            os.system("cls")
            exit()
    elif selection == "9": # CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf(9)
        os.system("cls")
        print(50 * "-")
        print("What would you like to do?")
        print(50 * "-")
        print("-> Download(1)")
        print("-> View online(2)")
        print(50 * "-")
        selection_one = (input("Please select your option:" + " "))
        if selection_one == "1":
            print(50 * "-")
            print("Your download will start shortly...")
            print(50 * "-")
            print("Before downloading, do you want to check it has been previously downloaded?")
            download_activation = input("Y(1)/N(2):" + " ")
            if download_activation == "1":
                print("Running check, wait a moment...")
                print(50 * "-")
                path_exists = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf")
                if os.path.exists(path_exists) == "CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf":
                    print("Yes, file already downloaded, theres no need to download, check your folder.")
                else:
                    print("File doesnt exist, starting download now")
                print(50 * "-")
                print(input("Press enter to start download:" + " "))
                os.system("cls")
                print("Preparing download...")
                print(50 * "-")
                os.system("curl.exe -o CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf --url https://www.commoncriteriaportal.org/files/ccfiles/CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf")
                print(50 * "-")
                print("Download complete")
                src9 = 'C:/Users/Adolfo/Desktop/tools/CC/CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf'
                dest9 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
                shutil.move(src9, dest9)
                print("Done")
                print(50 * "-")
                input("Press any key to go back to the main menu:" + " ")
                print(50 * "-")
                os.system("cls")
                show_menu_one()
        elif selection_one == "2":
            os.system("cls")
            print(50 * "-")
            input("Press any key to open PDF in browswer:" + " ")
            print(50 * "-")
            webbrowser.open("https://www.commoncriteriaportal.org/files/ccfiles/CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf")
            show_menu_one()
            os.system("cls")
            exit()
    elif selection == "10": # CC3R3.dtd(10)
        os.system("cls")
        print(50 * "-")
        print("What would you like to do?")
        print(50 * "-")
        print("-> Download(1)")
        print("-> View online(2)")
        print(50 * "-")
        selection_one = (input("Please select your option:" + " "))
        if selection_one == "1":
            print(50 * "-")
            print("Your download will start shortly...")
            print(50 * "-")
            print("Before downloading, do you want to check it has been previously downloaded?")
            download_activation = input("Y(1)/N(2):" + " ")
            if download_activation == "1":
                print("Running check, wait a moment...")
                print(50 * "-")
                path_exists = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CC3R3.dtd")
                if os.path.exists(path_exists) == "CC3R3.dtd":
                    print("Yes, file already downloaded, theres no need to download, check your folder.")
                else:
                    print("File doesnt exist, starting download now")
                print(50 * "-")
                print(input("Press enter to start download:" + " "))
                os.system("cls")
                print("Preparing download...")
                print(50 * "-")
                os.system("curl.exe -o CC3R3.dtd --url https://www.commoncriteriaportal.org/files/ccfiles/CC3R3.dtd")
                print(50 * "-")
                print("Download complete")
                src10 = 'C:/Users/Adolfo/Desktop/tools/CC/CC3R3.dtd'
                dest10 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
                shutil.move(src10, dest10)
                print("Done")
                print(50 * "-")
                input("Press any key to go back to the main menu:" + " ")
                print(50 * "-")
                os.system("cls")
                show_menu_one()
        elif selection_one == "2":
            os.system("cls")
            print(50 * "-")
            input("Press any key to open PDF in browswer:" + " ")
            print(50 * "-")
            webbrowser.open("https://www.commoncriteriaportal.org/files/ccfiles/CC3R3.dtd")
            show_menu_one()
            os.system("cls")
            exit()
    elif selection == "11": # cc3R5.XML.zip(11)
        os.system("cls")
        print(50 * "-")
        print("What would you like to do?")
        print(50 * "-")
        print("-> Download(1)")
        print("-> View online(2)")
        print(50 * "-")
        selection_one = (input("Please select your option:" + " "))
        if selection_one == "1":
            print(50 * "-")
            print("Your download will start shortly...")
            print(50 * "-")
            print("Before downloading, do you want to check it has been previously downloaded?")
            download_activation = input("Y(1)/N(2):" + " ")
            if download_activation == "1":
                print("Running check, wait a moment...")
                print(50 * "-")
                path_exists = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\cc3R5.XML.zip")
                if os.path.exists(path_exists) == "cc3R5.XML.zip":
                    print("Yes, file already downloaded, theres no need to download, check your folder.")
                else:
                    print("File doesnt exist, starting download now")
                print(50 * "-")
                print(input("Press enter to start download:" + " "))
                os.system("cls")
                print("Preparing download...")
                print(50 * "-")
                os.system("curl.exe -o cc3R5.XML.zip --url https://www.commoncriteriaportal.org/files/ccfiles/cc3R5.XML.zip")
                print(50 * "-")
                print("Download complete")
                src11 = 'C:/Users/Adolfo/Desktop/tools/CC/cc3R5.XML.zip'
                dest11 = 'C:/Users/Adolfo/Desktop/tools/CC/Downloads/Publications/CC_v3.1_Release_5'
                shutil.move(src11, dest11)
                print("Done")
                print(50 * "-")
                input("Press any key to go back to the main menu:" + " ")
                print(50 * "-")
                os.system("cls")
                show_menu_one()
        elif selection_one == "2":
            os.system("cls")
            print(50 * "-")
            input("Press any key to download .ZIP in browswer:" + " ")
            print(50 * "-")
            webbrowser.open("https://www.commoncriteriaportal.org/files/ccfiles/cc3R5.XML.zip")
            show_menu_one()
            os.system("cls")
            exit()
    elif selection == "12":
        download_all_files1()
    elif selection == "13":
        download_all_files()
    elif selection == "14":
        os.system("cls")
        show_menu_one() # Go back to the main menu

def cool_search_local():
    os.system("cls")
    print(Fore.RED + 90 * "-")
    print(Fore.WHITE + "Welcome to the local serch menu, listed below you will find the local downloaded files.")
    print(Fore.RED + 90 * "-")
    print(Fore.WHITE + "Here are the local directories")
    print(Fore.RED + 50 * "-")
    print("CC_v3.1_Release_5 (1)")
    print("other folder (2)")
    print("Other folder name (2)")
    print(Fore.RED + 50 * "-")
    folder_selection = input("Select folder too see files: " + " ")
    folder_one = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5")
    folder_contents = (os.listdir(folder_one))
    if folder_selection == "1":
        os.system("cls")
        print(Fore.RED + 50 * "-")
        print(Fore.WHITE + "\n".join(folder_contents))
        print(Fore.RED + 50 * "-")
        print(Fore.WHITE + "Go back (1)")
        print(Fore.WHITE + "Main menu (2)")
        print(Fore.WHITE + "Open PDF file (3)")
        print(Fore.RED + 50 * "-")
        choice_folder = input("Please select option:" + " ")
        if choice_folder == "1":
            os.system("cls")
            cool_search_local()
        elif choice_folder == "2":
            os.system("cls")
            show_menu_one()
        elif choice_folder == "3":
            os.system("cls")
            print(Fore.RED + 50 * "-")
            print(Fore.WHITE + "\n".join(folder_contents))
            print(Fore.RED + 50 * "-")
            print(Fore.WHITE + "Go back (1)")
            print(Fore.WHITE + "Main menu (2)")
            print(Fore.RED + 50 * "-")
            pdf_name = input("Please type the PDF file you wish to open:" + " ")
            if pdf_name == "CCPART1V3.1R5":
                subprocess.Popen([pdf1_path], shell=True) # Opening 1st PDF
                print("Opened PDF!")
                print("Anything else?")
                input("Press any key to go back:" + " ")
                os.system("cls")
                cool_search_local()
            elif pdf_name == "CCPART1V3.1R5_marked_changes":
                subprocess.Popen([pdf1_path], shell=True) # Opening 2nd PDF
                print("Opened PDF!")
                print("Anything else?")
                input("Press any key to go back:" + " ")
                os.system("cls")
                cool_search_local()
            elif pdf_name == "CCPART2V3.1R5":
                subprocess.Popen([pdf1_path], shell=True) # Opening 3rd PDF
                print("Opened PDF!")
                print("Anything else?")
                input("Press any key to go back:" + " ")
                os.system("cls")
                cool_search_local()
            elif pdf_name == "CCPART2V3.1R5_marked_changes":
                subprocess.Popen([pdf1_path], shell=True) # Opening 4th PDF
                print("Opened PDF!")
                print("Anything else?")
                input("Press any key to go back:" + " ")
                os.system("cls")
                cool_search_local()
            elif pdf_name == "CCPART3V3.1R5":
                subprocess.Popen([pdf1_path], shell=True) # Opening 5th PDF
                print("Opened PDF!")
                print("Anything else?")
                input("Press any key to go back:" + " ")
                os.system("cls")
                cool_search_local()
            elif pdf_name == "CCPART3V3.1R5_marked_changes":
                subprocess.Popen([pdf1_path], shell=True) # Opening 6th PDF
                print("Opened PDF!")
                print("Anything else?")
                input("Press any key to go back:" + " ")
                os.system("cls")
                cool_search_local()
            elif pdf_name == "CEMV3.1R5":
                subprocess.Popen([pdf1_path], shell=True) # Opening thth PDF
                print("Opened PDF!")
                print("Anything else?")
                input("Press any key to go back:" + " ")
                os.system("cls")
                cool_search_local()
            elif pdf_name == "CEMV3.1R5_marked_changes":
                subprocess.Popen([pdf1_path], shell=True) # Opening 8th PDF
                print("Opened PDF!")
                print("Anything else?")
                input("Press any key to go back:" + " ")
                os.system("cls")
                cool_search_local()
            elif pdf_name == "CCDB-2017-05-17-CCaddenda-Exact_Conformance":
                subprocess.Popen([pdf1_path], shell=True) # Opening 9th PDF
                print("Opened PDF!")
                print("Anything else?")
                input("Press any key to go back:" + " ")
                os.system("cls")
                cool_search_local()
            else:
                print("PDF not found, are you sure it exits?")
                input("Press enter to go back:" + " ")
                cool_search_local()


pdf1_path = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CCPART1V3.1R5.pdf")
pdf2_path = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CCPART1V3.1R5_marked_changes.pdf")
pdf3_path = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CCPART2V3.1R5.pdf")
pdf4_path = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CCPART2V3.1R5_marked_changes.pdf")
pdf5_path = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CCPART3V3.1R5.pdf")
pdf6_path = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CCPART3V3.1R5_marked_changes.pdf")
pdf7_path = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CEMV3.1R5.pdf")
pdf8_path = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CEMV3.1R5_marked_changes.pdf")
pdf9_path = (r"C:\Users\Adolfo\Desktop\tools\CC\Downloads\Publications\CC_v3.1_Release_5\CCDB-2017-05-17-CCaddenda-Exact_Conformance.pdf")
