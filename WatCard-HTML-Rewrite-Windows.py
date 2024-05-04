"""
A script that converts a "raw" HTML file into readable WatCard Machine transaction data.
by Kelly Duong

(Ensure that Python3 is installed and its PATH is configured; this script only uses its built-in libraries - external library/package downloads not necessary)
"""

from datetime import datetime
import os

def renameFile(file):
    try: 
        date = datetime.now().strftime("%m_%d_%y")              #Formats current date as "MM_DD_YY"
        time = datetime.now().strftime("%H_%M_%S")              #Formats current time as "HH_MM_SS"
        newFolder = 'C:/HTML/Date_{}'.format(date)              #New folder w/ date
        if ((os.path.exists(newFolder)) == False):
            os.mkdir(newFolder)
        newFile = newFolder + '/Time_{}.html'.format(time) 
        os.rename(file, newFile)                                #Renames original file with time and organizes into date folders
        file = newFile
        return(file)
    except Exception as e:
        print(f"Caught an exception: {type(e).__name}")

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
        print(f"Caught an exception: {type(e).__name}")

def rewriteFile(file,text):                                     #Rewrites the file with reformatted text (improved legibility)
    try:
        f = open(file, "w")
        f.write(text)
        f.close()
    except Exception as e:
        print(f"Caught an exception: {type(e).__name}")

while True:                                                     #Actively seeks for receipt file - renames and sorts as soon as it is uploaded to the computer
    try:
        file = 'C:/HTML/bluetooth_content_share.html'
        if os.path.exists(file):
            file = renameFile(file)
            text = parseHTML(file)
            print(text)
            rewriteFile(file, text)
    except Exception as e:
        print(f"Caught an exception: {type(e).__name}")