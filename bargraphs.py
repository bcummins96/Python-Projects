# Benjamin Cummins
# this program creates a bar graph to visualize the comparison of 2 numerical values.

from graphics import *

def main():

    #open window
    comparewindow = GraphWin("Comparison Graph", 400, 400)

    #draw x and y axis in window
    xaxis = Line(Point(70,330), Point(330,330))
    yaxis = Line(Point(70,330), Point(70,70))
    xaxis.draw(comparewindow)
    yaxis.draw(comparewindow)

    #display x axis values (text objects)
    msg25 = Text(Point(120,350), "25")
    msg25.draw(comparewindow)
    msg50 = Text(Point(200,350), "50")
    msg50.draw(comparewindow)
    msg75 = Text(Point(280,350), "75")
    msg75.draw(comparewindow)

    #display Option A and B messages above entry boxes
    msgA = Text(Point(350,150), "Option A")
    msgA.draw(comparewindow)
    msgB = Text(Point(350,200), "Option B")
    msgB.draw(comparewindow)

    #set up entry boxes for data
    inputA = Entry(Point(350,170), 3)
    inputA.setFill("light grey")
    inputA.draw(comparewindow)
    inputB = Entry(Point(350,220), 3)
    inputB.setFill("light grey")
    inputB.draw(comparewindow)

    #compare and exit button rectangles
    comp = Rectangle(Point(330,330), Point(390,360))
    comp.draw(comparewindow)
    comp.setFill("green")
    leave = Rectangle(Point(330,360), Point(390,390))
    leave.draw(comparewindow)
    leave.setFill("red")

    #compare and exit button messages
    comptxt = Text(Point(359,345), "Compare!")
    comptxt.setSize(10)
    comptxt.draw(comparewindow)
    quittxt = Text(Point(358,375), "Quit")
    quittxt.setSize(10)
    quittxt.draw(comparewindow)

    #initialize rectangles so we can undraw as part of the for loop
    rectA = Rectangle(Point(0,0), Point(0,0))
    rectA.setFill("green")
    rectB = Rectangle(Point(0,0), Point(0,0))
    rectB.setFill("blue")


    #start reactivity, run 200 times (or a while loop would be fine too)
    for i in range(200):

        #wait for mouse click, fetch values
        click = comparewindow.getMouse()
        xcoord = click.getX()
        ycoord = click.getY()

        #if in the x range of my buttons
        if xcoord > 331 and xcoord < 391:

            #if in the y range of compare button
            if ycoord > 331 and ycoord < 361:

                #first undraw old rectangles
                rectA.undraw()
                rectB.undraw()

                #receive entry box values as numbers
                optionAvalue = int(inputA.getText())
                optionBvalue = int(inputB.getText())

                #ensure the values are in range
                if optionAvalue > -1 and optionAvalue < 101:
                    if optionBvalue > -1 and optionBvalue < 101:

                        #draw rectangles, length based on entry box
                        rectA = Rectangle(Point(70,160), Point(70 + (optionAvalue*2.63),190))
                        rectA.draw(comparewindow)
                        rectA.setFill("green")
                        rectB = Rectangle(Point(70,190), Point(70 + (optionBvalue*2.63),220))
                        rectB.draw(comparewindow)
                        rectB.setFill("blue")

                else:
                    1==1

            #close window if y click in exit box range    
            if ycoord > 360 and ycoord < 391:
                comparewindow.close()
            else:
                1 == 1
 
#call main function
main()
