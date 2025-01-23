
# Benjamin Cummins
# This program reads through a large text file containing work shifts to display the total numbers in a graphical interface.
# Searchable locations are CHI, ATL, CIN, IND, DC.

#import graphics
from graphics import *
import time

#define readData function, accept string
def readData(String):

    #open file only during reading, read lines, close once done
    with open(String) as x:
        elem = x.readlines()

    #initialize list
    List = []
    
    #split elements into sublists
    for i in elem:
        a = i.strip('\n')
        b = a.split(',')
        #add to list
        List.append(b)

    #convert last element of each substring to an int
    for i in range(len(List)):
        (List[i][3]) = int(List[i][3])

    #return list
    return List


#define count function
def count(List):

    #initialize all counting variables and dictionary
    firstIND = 0
    secondIND = 0
    thirdIND = 0

    firstCIN = 0
    secondCIN = 0
    thirdCIN = 0

    firstCHI = 0
    secondCHI = 0
    thirdCHI = 0

    firstATL = 0
    secondATL = 0
    thirdATL = 0

    firstDC = 0
    secondDC = 0
    thirdDC = 0
    
    Dictionary = {}

    #read through list
    for i in range(len(List)):

        #read the hour of each substring
        timestr = List[i][0]
        #save this as an int
        time = int(timestr[0:2])

        #if the hour is between 0 and 8, first shift.
        #add to the first shift list for the specified location
        if time < 8:
            if List[i][2] == "IND":
                firstIND += int(List[i][3])
            if List[i][2] == "CIN":
                firstCIN += int(List[i][3])
            if List[i][2] == "CHI":
                firstCHI += int(List[i][3])
            if List[i][2] == "ATL":
                firstATL += int(List[i][3])
            if List[i][2] == "DC":
                firstDC += int(List[i][3])

        #if the hour is between 8 and 16, second shift.
        #add to the second shift list for the specified location
        if time >= 8 and time < 16:
            if List[i][2] == "IND":
                secondIND += int(List[i][3])
            if List[i][2] == "CIN":
                secondCIN += int(List[i][3])
            if List[i][2] == "CHI":
                secondCHI += int(List[i][3])
            if List[i][2] == "ATL":
                secondATL += int(List[i][3])
            if List[i][2] == "DC":
                secondDC += int(List[i][3])

        #if the hour is between 16 and 24, third shift.
        #add to the third shift list for the specified location
        if time >= 16:
            if List[i][2] == "IND":
                thirdIND += int(List[i][3])
            if List[i][2] == "CIN":
                thirdCIN += int(List[i][3])
            if List[i][2] == "CHI":
                thirdCHI += int(List[i][3])
            if List[i][2] == "ATL":
                thirdATL += int(List[i][3])
            if List[i][2] == "DC":
                thirdDC += int(List[i][3])

    #add values to dictionary corresponding to location key
    Dictionary["IND"] = [firstIND,secondIND,thirdIND]
    Dictionary["CIN"] = [firstCIN,secondCIN,thirdCIN]
    Dictionary["CHI"] = [firstCHI,secondCHI,thirdCHI]
    Dictionary["ATL"] = [firstATL,secondATL,thirdATL]
    Dictionary["DC"] = [firstDC,secondDC,thirdDC]

    #return dictionary
    return Dictionary

#define lookup function, 2 arguments
def lookup(Dictionary,String):

    #return list of zeroes if invalid location key entered
    if String not in Dictionary.keys():
        newlist = [0,0,0,0]
        return newlist
    #if valid, pass name to dictionary and return list of added values
    else:
        Dictionary[String]
        u = Dictionary[String]
        newList = [Dictionary[String],(u[0] + u[1] + u[2])]
        return newList

#define display function, Dictionary as an argument
def display(Dictionary):

    #create graphics window
    menu = GraphWin("Display", 500, 450)

    #create header
    fine = Text(Point(250,25), "FINE DETAILS, INC")
    fine.setSize(18)
    fine.setStyle("bold")
    fine.draw(menu)

    #location label
    location = Text(Point(130,75), "Location: ")
    location.setSize(16)
    location.draw(menu)

    #create entry box
    entry = Entry(Point(250,75), 10)
    entry.setFill("white")
    entry.setSize(16)
    entry.draw(menu)

    #find box background
    find = Rectangle(Point(300,120), Point(400,160))
    find.setFill("green")
    find.draw(menu)

    #exit box background
    exitit = Rectangle(Point(100,120), Point(200,160))
    exitit.setFill("red")
    exitit.draw(menu)

    #find button text
    findtxt = Text(Point(350,140), "FIND")
    findtxt.setSize(14)
    findtxt.setStyle("bold")
    findtxt.draw(menu)

    #exit button text
    exittxt = Text(Point(150,140), "EXIT")
    exittxt.setSize(14)
    exittxt.setStyle("bold")
    exittxt.draw(menu)

    #1st shift text
    fsttxt = Text(Point(150,210), "1ST SHIFT: ")
    fsttxt.setSize(14)
    fsttxt.draw(menu)

    #2nd shift text
    sndtxt = Text(Point(150,260), "2ND SHIFT: ")
    sndtxt.setSize(14)
    sndtxt.draw(menu)

    #3rd shift text
    trdtxt = Text(Point(150,310), "3RD SHIFT: ")
    trdtxt.setSize(14)
    trdtxt.draw(menu)

    #total text
    tottxt = Text(Point(132,360), "TOTAL: ")
    tottxt.setSize(14)
    tottxt.draw(menu)

    #create 1st shift result box
    fstent = Entry(Point(350,210), 7)
    fstent.setFill("white")
    fstent.setSize(16)
    fstent.draw(menu)

    #create 2nd shift result box
    sndent = Entry(Point(350,260), 7)
    sndent.setFill("white")
    sndent.setSize(16)
    sndent.draw(menu)

    #create 3rd shift result box
    trdent = Entry(Point(350,310), 7)
    trdent.setFill("white")
    trdent.setSize(16)
    trdent.draw(menu)

    #create total result box
    totan = Entry(Point(350,360), 7)
    totan.setFill("white")
    totan.setSize(16)
    totan.draw(menu)

    #initialize endcount
    endcount = 0

    #while loop until quit is clicked
    while endcount == 0:

        #check mouse location
        clickpoint = menu.checkMouse()
        if clickpoint != None: 
            clickx = clickpoint.getX()
            clicky = clickpoint.getY()

            #if click is in the exit box, close.
            if (clickx > 100 and clickx < 200):
                if (clicky > 120 and clicky < 160):
                    endcount = 1
    
            #if click is in the find box,
            if (clickx > 300 and clickx < 400):
                if (clicky > 120 and clicky < 160):
                    
                    #check location entry
                    String = entry.getText()
                    if String != "":
                        
                        #send to lookup function
                        List = lookup(Dictionary,String)

                        #if location entered is valid,
                        if List != [0,0,0,0]:

                            #store returned values
                            fstresult = List[0][0]
                            sndresult = List[0][1]
                            trdresult = List[0][2]
                            totalresult = List[1]
                            
                        #if invalid location entered, clear answer boxes
                        else: 
                            fstresult = ""
                            sndresult = ""
                            trdresult = ""
                            totalresult = ""
                        
                        #send answers to boxes in graphics window
                        fstent.setText(fstresult)
                        sndent.setText(sndresult)
                        trdent.setText(trdresult)
                        totan.setText(totalresult)
                        
            time.sleep(.01)
    #close graphics window when quit is clicked
    menu.close()

#define main function
def main():
    #call data function, assign list
    List = readData('mfgOutput.txt')
    #send list to process function
    Dictionary = count(List)
    #send dictionary to menu function
    display(Dictionary)

main()
    

