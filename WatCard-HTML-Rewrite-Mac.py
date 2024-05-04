"""
A script that converts a "raw" HTML file into readable WatCard Machine transaction data.
by Kelly Duong

(Relies on Python3 and built-in libraries; external library/package downloads not necessary)
"""

from datetime import datetime
import os
import shutil

def renameFile(file):
    try:
        date = str(datetime.now().strftime("%m_%d_%y"))         #Formats current date as "MM_DD_YY"
        time = str(datetime.now().strftime("%H_%M_%S"))         #Formats current time as "HH_MM_SS"
        newFolder = str('/Users/msadmin/Desktop/Receipts/Date_{}'.format(date))              #New folder w/ date
        if ((os.path.exists(newFolder)) == False):
            os.makedirs(newFolder)
        newFile = os.path.join(newFolder, 'Time_{}.html'.format(time)) 
        shutil.move(file, newFile)                                #Renames original file with time and organizes into date folders
        file = newFile
        return(file)
    except Exception as e:
        print(f"Caught an exception: {type(e).__name__}")

def parseHTML(file):                                            #Extracts text from HTML file
    try:
        f = open(file, "r")
        data = f.read()
        in_tag = False
        text = ""
        for char in data:                                       #Searches for text within the tags
            if char == "<":
                in_tag = True
            elif char == ">":
                in_tag = False
            elif in_tag == False:                               #Conditionals aid in reformatting (web browsers 
                if char == "\n":                                #Read tabs, newlines, spaces, etc. as single characters)
                    text += "<br>"
                elif char == " ":
                    text += "&#160 "
                else:
                    text += char
        return(text)
    except Exception as e:
        print(f"Caught an exception: {type(e).__name__}")

def rewriteFile(file,text):                                     #Rewrites the file with reformatted text (improved legibility)
    try:
        f = open(file, "w")
        f.write(text)
        f.close()
    except Exception as e:
        print(f"Caught an exception: {type(e).__name__}")

while True:                                                     #Actively seeks for receipt file - renames and sorts as soon as it is uploaded to the computer
    try:
        file = '/Users/msadmin/Downloads/bluetooth_content_share.html'
        if os.path.exists(file):
            newfile = renameFile(file)
            text = parseHTML(newfile)
            print(text)
            rewriteFile(newfile, text)
    except Exception as e:
        print(f"Caught an exception: {type(e).__name__}")
        


