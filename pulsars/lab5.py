
# Benjamin Cummins
# This program combines data from two separate data files and organizes it into a horizontal bar chart to visualize the data.

from graphics import *

#define count function
def count(it):

    #1-5 and MAKERS
    # M counts
    M1 = it.count("M1")
    M2 = it.count("M2")
    M3 = it.count("M3")
    M4 = it.count("M4")
    M5 = it.count("M5")

    # A counts
    A1 = it.count("A1")
    A2 = it.count("A2")
    A3 = it.count("A3")
    A4 = it.count("A4")
    A5 = it.count("A5")

    # K counts
    K1 = it.count("K1")
    K2 = it.count("K2")
    K3 = it.count("K3")
    K4 = it.count("K4")
    K5 = it.count("K5")

    # E counts
    E1 = it.count("E1")
    E2 = it.count("E2")
    E3 = it.count("E3")
    E4 = it.count("E4")
    E5 = it.count("E5")

    # R counts
    R1 = it.count("R1")
    R2 = it.count("R2")
    R3 = it.count("R3")
    R4 = it.count("R4")
    R5 = it.count("R5")

    # S counts
    S1 = it.count("S1")
    S2 = it.count("S2")
    S3 = it.count("S3")
    S4 = it.count("S4")
    S5 = it.count("S5")

    #create list with each value
    countlist = [M1,M2,M3,M4,M5,A1,A2,A3,A4,A5,K1,K2,K3,K4,K5,E1,E2,E3,E4,E5,R1,R2,R3,R4,R5,S1,S2,S3,S4,S5]

    #return this list
    return countlist






#define graph function
def graph(x):

    #send list to count function
    graphdata = count(x)

    #create graph window
    BOOYA = GraphWin("BOOYA", 400, 420)
    title = Text(Point(200,20), "BOOYA Pulsar Data")
    title.setSize(10)
    title.setStyle("bold")
    title.draw(BOOYA)

    #create text objects and rectangles THE HARD WAY: no loops :)
    
    #M
    M1text = Text(Point(10,60), "M1")
    M1text.setSize(8)
    M1text.draw(BOOYA)
    M1bar = Rectangle(Point(20,55), Point((20 + graphdata[0]*11),65))
    M1bar.setFill("red")
    M1bar.draw(BOOYA)
    M1count = Text(Point(graphdata[0]*11 + 10,60), graphdata[0])
    M1count.setSize(8)
    M1count.draw(BOOYA)
    
    M2text = Text(Point(10,70), "M2")
    M2text.setSize(8)
    M2text.draw(BOOYA)
    M2bar = Rectangle(Point(20,65), Point((graphdata[1]*11),75))
    M2bar.setFill("yellow")
    M2bar.draw(BOOYA)
    M2count = Text(Point(graphdata[1]*11 + 10,70), graphdata[1])
    M2count.setSize(8)
    M2count.draw(BOOYA)
    
    M3text = Text(Point(10,80), "M3")
    M3text.setSize(8)
    M3text.draw(BOOYA)
    M3bar = Rectangle(Point(20,75), Point((graphdata[2]*11),85))
    M3bar.setFill("green")
    M3bar.draw(BOOYA)
    M3count = Text(Point(graphdata[2]*11 + 10,80), graphdata[2])
    M3count.setSize(8)
    M3count.draw(BOOYA)
    
    M4text = Text(Point(10,90), "M4")
    M4text.setSize(8)
    M4text.draw(BOOYA)
    M4bar = Rectangle(Point(20,85), Point((graphdata[3]*11),95))
    M4bar.setFill("blue")
    M4bar.draw(BOOYA)
    M4count = Text(Point(graphdata[3]*11 + 10,90), graphdata[3])
    M4count.setSize(8)
    M4count.draw(BOOYA)
    
    M5text = Text(Point(10,100), "M5")
    M5text.setSize(8)
    M5text.draw(BOOYA)
    M5bar = Rectangle(Point(20,95), Point((graphdata[4]*11),105))
    M5bar.setFill("pink")
    M5bar.draw(BOOYA)
    M5count = Text(Point(graphdata[4]*11 + 10,100), graphdata[4])
    M5count.setSize(8)
    M5count.draw(BOOYA)


    #A
    A1text = Text(Point(10,110), "A1")
    A1text.setSize(8)
    A1text.draw(BOOYA)
    A1bar = Rectangle(Point(20,105), Point((graphdata[5]*11),115))
    A1bar.setFill("red")
    A1bar.draw(BOOYA)
    M5count = Text(Point(graphdata[5]*11 + 10,110), graphdata[5])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    A2text = Text(Point(10,120), "A2")
    A2text.setSize(8)
    A2text.draw(BOOYA)
    A2bar = Rectangle(Point(20,115), Point((graphdata[6]*11),125))
    A2bar.setFill("yellow")
    A2bar.draw(BOOYA)
    M5count = Text(Point(graphdata[6]*11 + 10,120), graphdata[6])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    A3text = Text(Point(10,130), "A3")
    A3text.setSize(8)
    A3text.draw(BOOYA)
    A3bar = Rectangle(Point(20,125), Point((graphdata[7]*11),135))
    A3bar.setFill("green")
    A3bar.draw(BOOYA)
    M5count = Text(Point(graphdata[7]*11 + 10,130), graphdata[7])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    A4text = Text(Point(10,140), "A4")
    A4text.setSize(8)
    A4text.draw(BOOYA)
    A4bar = Rectangle(Point(20,135), Point((graphdata[8]*11),145))
    A4bar.setFill("blue")
    A4bar.draw(BOOYA)
    M5count = Text(Point(graphdata[8]*11 + 10,140), graphdata[8])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    A5text = Text(Point(10,150), "A5")
    A5text.setSize(8)
    A5text.draw(BOOYA)
    A5bar = Rectangle(Point(20,145), Point((20 + graphdata[9]*11),155))
    A5bar.setFill("pink")
    A5bar.draw(BOOYA)
    M5count = Text(Point(graphdata[9]*11 + 10,150), graphdata[9])
    M5count.setSize(8)
    M5count.draw(BOOYA)
    
    #K
    K1text = Text(Point(10,160), "K1")
    K1text.setSize(8)
    K1text.draw(BOOYA)
    K1bar = Rectangle(Point(20,155), Point((graphdata[10]*11),165))
    K1bar.setFill("red")
    K1bar.draw(BOOYA)
    M5count = Text(Point(graphdata[10]*11 + 10,160), graphdata[10])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    K2text = Text(Point(10,170), "K2")
    K2text.setSize(8)
    K2text.draw(BOOYA)
    K2bar = Rectangle(Point(20,165), Point((graphdata[11]*11),175))
    K2bar.setFill("yellow")
    K2bar.draw(BOOYA)
    M5count = Text(Point(graphdata[11]*11 + 10,170), graphdata[11])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    K3text = Text(Point(10,180), "K3")
    K3text.setSize(8)
    K3text.draw(BOOYA)
    K3bar = Rectangle(Point(20,175), Point((graphdata[12]*11),185))
    K3bar.setFill("green")
    K3bar.draw(BOOYA)
    M5count = Text(Point(graphdata[12]*11 + 10,180), graphdata[12])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    K4text = Text(Point(10,190), "K4")
    K4text.setSize(8)
    K4text.draw(BOOYA)
    K4bar = Rectangle(Point(20,185), Point((graphdata[13]*11),195))
    K4bar.setFill("blue")
    K4bar.draw(BOOYA)
    M5count = Text(Point(graphdata[13]*11 + 10,190), graphdata[13])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    K5text = Text(Point(10,200), "K5")
    K5text.setSize(8)
    K5text.draw(BOOYA)
    K5bar = Rectangle(Point(20,195), Point((graphdata[14]*11),205))
    K5bar.setFill("pink")
    K5bar.draw(BOOYA)
    M5count = Text(Point(graphdata[14]*11 + 10,200), graphdata[14])
    M5count.setSize(8)
    M5count.draw(BOOYA)
    
    #E
    E1text = Text(Point(10,210), "E1")
    E1text.setSize(8)
    E1text.draw(BOOYA)
    E1bar = Rectangle(Point(20,205), Point((graphdata[15]*11),215))
    E1bar.setFill("red")
    E1bar.draw(BOOYA)
    M5count = Text(Point(graphdata[15]*11 + 10,210), graphdata[15])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    E2text = Text(Point(10,220), "E2")
    E2text.setSize(8)
    E2text.draw(BOOYA)
    E2bar = Rectangle(Point(20,215), Point((graphdata[16]*11),225))
    E2bar.setFill("yellow")
    E2bar.draw(BOOYA)
    M5count = Text(Point(graphdata[16]*11 + 10,220), graphdata[16])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    E3text = Text(Point(10,230), "E3")
    E3text.setSize(8)
    E3text.draw(BOOYA)
    E3bar = Rectangle(Point(20,225), Point((graphdata[17]*11),235))
    E3bar.setFill("green")
    E3bar.draw(BOOYA)
    M5count = Text(Point(graphdata[17]*11 + 10,230), graphdata[17])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    E4text = Text(Point(10,240), "E4")
    E4text.setSize(8)
    E4text.draw(BOOYA)
    E4bar = Rectangle(Point(20,235), Point((graphdata[18]*11),245))
    E4bar.setFill("blue")
    E4bar.draw(BOOYA)
    M5count = Text(Point(graphdata[18]*11 + 10,240), graphdata[18])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    E5text = Text(Point(10,250), "E5")
    E5text.setSize(8)
    E5text.draw(BOOYA)
    E5bar = Rectangle(Point(20,245), Point((graphdata[19]*11),255))
    E5bar.setFill("pink")
    E5bar.draw(BOOYA)
    M5count = Text(Point(graphdata[19]*11 + 10,250), graphdata[19])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    #R
    R1text = Text(Point(10,260), "R1")
    R1text.setSize(8)
    R1text.draw(BOOYA)
    R1bar = Rectangle(Point(20,255), Point((graphdata[20]*11),265))
    R1bar.setFill("red")
    R1bar.draw(BOOYA)
    M5count = Text(Point(graphdata[20]*11 + 10,260), graphdata[20])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    R2text = Text(Point(10,270), "R2")
    R2text.setSize(8)
    R2text.draw(BOOYA)
    R2bar = Rectangle(Point(20,265), Point((graphdata[21]*11),275))
    R2bar.setFill("yellow")
    R2bar.draw(BOOYA)
    M5count = Text(Point(graphdata[21]*11 + 10,270), graphdata[21])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    R3text = Text(Point(10,280), "R3")
    R3text.setSize(8)
    R3text.draw(BOOYA)
    R3bar = Rectangle(Point(20,275), Point((graphdata[22]*11),285))
    R3bar.setFill("green")
    R3bar.draw(BOOYA)
    M5count = Text(Point(graphdata[22]*11 + 10,280), graphdata[22])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    R4text = Text(Point(10,290), "R4")
    R4text.setSize(8)
    R4text.draw(BOOYA)
    R4bar = Rectangle(Point(20,285), Point((graphdata[23]*11),295))
    R4bar.setFill("blue")
    R4bar.draw(BOOYA)
    M5count = Text(Point(graphdata[23]*11 + 10,290), graphdata[23])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    R5text = Text(Point(10,300), "R5")
    R5text.setSize(8)
    R5text.draw(BOOYA)
    R5bar = Rectangle(Point(20,295), Point((graphdata[24]*11),305))
    R5bar.setFill("pink")
    R5bar.draw(BOOYA)
    M5count = Text(Point(graphdata[24]*11 + 10,300), graphdata[24])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    #S
    S1text = Text(Point(10,310), "S1")
    S1text.setSize(8)
    S1text.draw(BOOYA)
    S1bar = Rectangle(Point(20,305), Point((graphdata[25]*11),315))
    S1bar.setFill("red")
    S1bar.draw(BOOYA)
    M5count = Text(Point(graphdata[25]*11 + 10,310), graphdata[25])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    S2text = Text(Point(10,320), "S2")
    S2text.setSize(8)
    S2text.draw(BOOYA)
    S2bar = Rectangle(Point(20,315), Point((graphdata[26]*11),325))
    S2bar.setFill("yellow")
    S2bar.draw(BOOYA)
    M5count = Text(Point(graphdata[26]*11 + 10,320), graphdata[26])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    S3text = Text(Point(10,330), "S3")
    S3text.setSize(8)
    S3text.draw(BOOYA)
    S3bar = Rectangle(Point(20,325), Point((graphdata[27]*11),335))
    S3bar.setFill("green")
    S3bar.draw(BOOYA)
    M5count = Text(Point(graphdata[27]*11 + 10,330), graphdata[27])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    S4text = Text(Point(10,340), "S4")
    S4text.setSize(8)
    S4text.draw(BOOYA)
    S4bar = Rectangle(Point(20,335), Point((graphdata[28]*11),345))
    S4bar.setFill("blue")
    S4bar.draw(BOOYA)
    M5count = Text(Point(graphdata[28]*11 + 10,340), graphdata[28])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    S5text = Text(Point(10,350), "S5")
    S5text.setSize(8)
    S5text.draw(BOOYA)
    S5bar = Rectangle(Point(20,345), Point((graphdata[29]*11),355))
    S5bar.setFill("pink")
    S5bar.draw(BOOYA)
    M5count = Text(Point(graphdata[29]*11 + 10,350), graphdata[29])
    M5count.setSize(8)
    M5count.draw(BOOYA)

    #close window when clicked
    BOOYA.getMouse()
    BOOYA.close()



    
#define read function
def read(x,y,size):

    #initialize list
    newlist = []
    
    print()
    #for loop to create list
    for i in range(size + 2):
        xvalues = x.readline(i)
        yvalues = y.readline(i)
        combine = xvalues.strip() + yvalues.strip()
        newlist.append(combine)

    #cleanup
    newlist.remove("")
    newlist.remove("")

    #close lists and return value
    x.close
    y.close
    return newlist

#define main
def main():

    #print functionality
    print("This program processes data from the Pulsar Laboratory")
    print("="*60)
    print("It reads the data from 2 files containing the pulsar name and")
    print(" signal strength, then combines them and displays the results.")
    print("")

    #prompt for user input
    xdata = input("Pulsar name file: ")
    ydata = input("Signal strength file: ")

    #count length of list
    with open(xdata) as f:
        number = len(f.readlines())

    #print steps
    print("")
    print("Analyzing data from " + xdata + " and " + ydata + " files...")
    print("\t" + "Reading from " + xdata + "...")
    print("\t" + "Reading from " + ydata + "...")
    print("\t" + "Combining values...")
    
    #send to read function
    returnedlist = read((open(xdata)),(open(ydata)),number)

    #print data
    print("The combined data includes " + str(number) + " values.")
    print("="*60)

    #for loop to print values
    for i in range(len(returnedlist)):
        print(returnedlist[i], end="  ")

    #send files to graph function
    graph(returnedlist)

#call main function    
main()

    

