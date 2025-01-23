# Ben Cummins
# Jonathan Ellingson
# CS 177
# project3.py
# this program is a game where the player attempts to locate
# a gold circle through clicking in the interactive window
# as few times as possible to check for the location.
# incorrect guesses will change color to indicate the distance
# from the correct circle, and the game is over after 5 rounds.

#custom feature 1: the green speeder
#extra circle added, green. when found, moves quickly around
#the screen and will not disappear until clicked. The
#green speeder must be caught before the game can continue.
#trying to catch it does not add to your score, as it moves
#MUCH faster than the golden pete.

#custom feature 2: hint button
#a blue  button added to the game window
#labeled "hint", when clicked chooses a grey
#circle at random to reveal. this adds 5
#to the click score. this can be used
#as many times as the player wants.

#custom feature 3: round counter
#added a counter to keep track of clicks
#for each round, in addition to cumulative
#in the game. Round clicks are displayed at the
#end of each round. if the round ends with
#less than 10 clicks, a reward message and flashing screen
#is displayed and 5 is subtracted from the total score.

#import graphics, random and time
from graphics import *
import time
import random


# define control panel function
def controlpanel():

    # create graphics window 250 x 200
    Gamecontrol = GraphWin("Game Control", 250, 200)
    
    # set background to grey
    Gamecontrol.setBackground("light grey")

    #title background
    titleblack = Rectangle(Point(0,0), Point(250,30))
    titleblack.setFill("black")
    titleblack.draw(Gamecontrol)

    #create title
    title = Text(Point(125,15), "BOILER GOLD HUNT!")
    title.setSize(12)
    title.setStyle("bold")
    title.setTextColor("gold")
    title.draw(Gamecontrol)

    #player name
    plname = Text(Point(125,50), "PLAYER NAME")
    plname.setSize(11)
    plname.setStyle("bold")
    plname.draw(Gamecontrol)

    #enter player name
    playername = Entry(Point(125,75), 10)
    playername.setFill("white")
    playername.draw(Gamecontrol)

    #new game background
    newgame = Rectangle(Point(5,120), Point(110,195))
    newgame.setFill("gold")
    newgame.draw(Gamecontrol)

    #exit background
    exitbox = Rectangle(Point(175,120), Point(245,195))
    exitbox.setFill("black")
    exitbox.draw(Gamecontrol)

    #create new game text
    newmsg = Text(Point(57,158), "NEW GAME")
    newmsg.setSize(12)
    newmsg.setStyle("bold")
    newmsg.draw(Gamecontrol)

    #create exit game text
    exitmsg = Text(Point(210,158), "EXIT")
    exitmsg.setSize(12)
    exitmsg.setStyle("bold")
    exitmsg.setTextColor("white")
    exitmsg.draw(Gamecontrol)

    #return values
    return (playername, newgame, exitbox, Gamecontrol)



#define gamewindow function
def gamewindow():

    # create graphics window 480 x 520
    GoldHunt = GraphWin("GoldHunt", 480, 520)

    #counter background
    topblack = Rectangle(Point(0,0), Point(480,40))
    topblack.setFill("black")
    topblack.draw(GoldHunt)

    #number of rounds text
    roundmsg = Text(Point(40,20), "Round: ")
    roundmsg.setSize(11)
    roundmsg.setTextColor("gold")
    roundmsg.draw(GoldHunt)

    #number of clicks text
    clicksmsg = Text(Point(403,20), "Total Score: ")
    clicksmsg.setSize(11)
    clicksmsg.setTextColor("gold")
    clicksmsg.draw(GoldHunt)

    #number of round clicks text
    clicksmsg = Text(Point(120,20), "Clicks: ")
    clicksmsg.setSize(11)
    clicksmsg.setTextColor("gold")
    clicksmsg.draw(GoldHunt)

    hint = Circle(Point(330,20), 18)
    hint.setFill("light blue")
    hint.draw(GoldHunt)

    #number of clicks text
    htxt = Text(Point(330,20), "HINT")
    htxt.setStyle("bold")
    htxt.setSize(10)
    htxt.draw(GoldHunt)

    #return labels and window
    return (roundmsg, clicksmsg, GoldHunt)



#define grid function
def grid(window,playername):

    #display player = message
    displayname = Text(Point(232,20), ("Player = " + playername))
    displayname.setSize(11)
    displayname.setTextColor("gold")
    displayname.setStyle("bold")
    displayname.draw(window)

    #initialize circle list
    blkcirclelist = []
    
    #nested for loop: i for collumns, b for rows
    for i in range (15):
        for b in range(15):
            
            #run through each location to create a circle
            blkcircle = Circle(Point(28 + (30*i),68 + (30*b)), 15)
            blkcircle.setFill("black")
            blkcircle.draw(window)
            
            #add each circle to the list
            blkcirclelist.append(blkcircle)

    #randomly choose a circle for the gold one
    goldcircle = random.choice(blkcirclelist)

    #randomly choose circle for red bummer
    redcircle = random.choice(blkcirclelist)

    #randomly choose circle for green speeder
    greencircle = random.choice(blkcirclelist)

    #if gold and red are same, change red
    while goldcircle == redcircle:
        redcircle = random.choice(blkcirclelist)

    #if green and gold or red are same, change green
    while greencircle == goldcircle or greencircle == redcircle:
        greencircle = random.choice(blkcirclelist)

    #initialize tan list
    tanlist = []

    #retreive gold circle location
    goldrad = goldcircle.getCenter()
    goldx = goldrad.getX()
    goldy = goldrad.getY()

    #retreive red circle location
    redrad = redcircle.getCenter()
    redx = redrad.getX()
    redy = redrad.getY()

    #retreive green circle location
    greenrad = greencircle.getCenter()
    greenx = greenrad.getX()
    greeny = greenrad.getY()
    
    #set tan circles in a distance around the gold one
    for i in range(225):

        #current location of circle of interest
        currentrad = (blkcirclelist[i]).getCenter()
        curx = currentrad.getX()
        cury = currentrad.getY()
        
        #fill corners
        if curx + 30 == goldx and cury + 30 == goldy:
            tanlist.append(blkcirclelist[i])
        if curx + 30 == goldx and cury - 30 == goldy:
            tanlist.append(blkcirclelist[i])
        if curx - 30 == goldx and cury - 30 == goldy:
            tanlist.append(blkcirclelist[i])
        if curx - 30 == goldx and cury + 30 == goldy:
            tanlist.append(blkcirclelist[i])

        #fill sides
        if curx + 30 == goldx and cury == goldy:
            tanlist.append(blkcirclelist[i])
        if curx - 30 == goldx and cury == goldy:
            tanlist.append(blkcirclelist[i])
        if curx == goldx and cury + 30 == goldy:
            tanlist.append(blkcirclelist[i])
        if curx == goldx and cury - 30 == goldy:
            tanlist.append(blkcirclelist[i])
            
    #initialize grey list
    greylist = []

    #fetch gold circle location (again)
    goldrad = goldcircle.getCenter()
    goldx = goldrad.getX()
    goldy = goldrad.getY()
    
    #set grey circles
    for i in range(225):

        #location of current circle
        currentrad = (blkcirclelist[i]).getCenter()
        curx = currentrad.getX()
        cury = currentrad.getY()
        
        #corner circles
        if curx + 60 == goldx and cury + 60 == goldy:
            greylist.append(blkcirclelist[i])
        if curx + 60 == goldx and cury - 60 == goldy:
            greylist.append(blkcirclelist[i])
        if curx - 60 == goldx and cury - 60 == goldy:
            greylist.append(blkcirclelist[i])
        if curx - 60 == goldx and cury + 60 == goldy:
            greylist.append(blkcirclelist[i])

        #side circles
        if curx + 60 == goldx and cury == goldy:
            greylist.append(blkcirclelist[i])
        if curx - 60 == goldx and cury == goldy:
            greylist.append(blkcirclelist[i])
        if curx == goldx and cury + 60 == goldy:
            greylist.append(blkcirclelist[i])
        if curx == goldx and cury - 60 == goldy:
            greylist.append(blkcirclelist[i])

        #fill 1
        if curx + 60 == goldx and cury + 30 == goldy:
            greylist.append(blkcirclelist[i])
        if curx + 60 == goldx and cury - 30 == goldy:
            greylist.append(blkcirclelist[i])
        if curx - 60 == goldx and cury - 30 == goldy:
            greylist.append(blkcirclelist[i])
        if curx - 60 == goldx and cury + 30 == goldy:
            greylist.append(blkcirclelist[i])
            
        #fill 2
        if curx + 30 == goldx and cury + 60 == goldy:
            greylist.append(blkcirclelist[i])
        if curx + 30 == goldx and cury - 60 == goldy:
            greylist.append(blkcirclelist[i])
        if curx - 30 == goldx and cury - 60 == goldy:
            greylist.append(blkcirclelist[i])
        if curx - 30 == goldx and cury + 60 == goldy:
            greylist.append(blkcirclelist[i])

    #initialize white list
    whitelist = []

    #if its not any of the other colors, make it white
    for i in range(225):
        if blkcirclelist[i] not in greylist:
            if blkcirclelist[i] not in tanlist:
                if blkcirclelist[i] != goldcircle:
                    if blkcirclelist[i] != redcircle:
                        if blkcirclelist[i] != greencircle:
                            whitelist.append(blkcirclelist[i])

    #now the colors are assigned, color all black.
    for i in range(225):
        (blkcirclelist[i]).setFill("black")
            
    #return the lists containing the true "secret" values
    return (goldcircle,tanlist,greylist,whitelist,redcircle,greencircle)


#define main function: runs based on
#click location in control panel.
def main(clickx,clicky):

    #initialize click locations
    newx = 0
    newy = 0


    #initialize 5 round counter
    counttofive = 1
    
    #set click counter to 0 for new game
    clickct = 0

    #initialize roundclicks
    roundclicks = 0

    #update display: clicks per round
    rdclicks = Text(Point(147,20), roundclicks)
    rdclicks.setSize(11)
    rdclicks.setTextColor("gold")

    #fetch player name from entry box
    plname = name.getText()

    #check for click in ctrl window
    clickpoint = ctrl.checkMouse()
    if clickpoint != None: 
        clickx = clickpoint.getX()
        clicky = clickpoint.getY()

    #check for player name again
    plname = name.getText()

    #if click is in the exit box, close.
    if (clickx > 175 and clicky > 120):
        ctrl.close()
        hunt.close()
        time.sleep(100000)

    #if click is in new game box AND name entered, start new game below.
    elif (clickx < 110 and clicky > 120) and plname != "":
        plname = name.getText()

    #game has now started, running below.
        
        #initialize round and count displays
        rddisplay = Text(Point(85,20), str(counttofive))
        ctdisplay = Text(Point(453,20), str(clickct))
        
        #start new round, everything in this while loop
        #below happens between rounds, 5 total.
        while counttofive < 6:

            #load circle lists, randomized for each round
            gold, tan, grey, white, red, green = grid(hunt,plname)

            #round status: running
            roundfinish = 0

            #undraw previous round count to update
            rddisplay.undraw()

            #update display: which round number it is
            rddisplay = Text(Point(70,20), str(counttofive))
            rddisplay.setSize(11)
            rddisplay.setTextColor("gold")
            rddisplay.draw(hunt)

            #loop inside a round for clicks, everything in here
            #repeats DURING a round per one mouse click.
            #while round status is running (roundfinish == 0:)
            while roundfinish == 0:
                
                #bring menu in to round to allow control board function during game
                #check for a click on control board
                clickpoint = ctrl.checkMouse()
                if clickpoint != None:
                    newx = clickpoint.getX()
                    newy = clickpoint.getY()

                #if a click is in the exit box, close.
                if (newx > 175 and newy > 120):
                    ctrl.close()
                    hunt.close()
                    time.sleep(100000)
                    

                #if click is in the new game box, close current hunt window
                #and restart main, passing along the new game box click location.
                if (newx < 110 and newy > 120) and plname != "":

                    #undraw current elements
                    ctdisplay.undraw()
                    rddisplay.undraw()
                    for i in range(len(white)):
                        white[i].undraw()
                    for i in range(len(tan)):
                        tan[i].undraw()
                    for i in range(len(grey)):
                        grey[i].undraw()
                    gold.undraw()
                    red.undraw()
                    green.undraw()
                    main(90,150)
                    
                #check for click in game window
                gameclick = hunt.checkMouse()

                #if there is a click, proceed a step in the game
                if gameclick != None:
                    huntx = gameclick.getX()
                    hunty = gameclick.getY()

                    #undraw previous round click count to update
                    rdclicks.undraw()

                    roundclicks += 1

                    #update display: clicks per round
                    rdclicks = Text(Point(149,20), roundclicks)
                    rdclicks.setSize(11)
                    rdclicks.setTextColor("gold")
                    rdclicks.draw(hunt)

                    #add one to click counter
                    clickct += 1

                    #undraw previous click count
                    ctdisplay.undraw()

                    #draw new click count
                    ctdisplay = Text(Point(453,20), str(clickct))
                    ctdisplay.setSize(11)
                    ctdisplay.setTextColor("gold")
                    ctdisplay.draw(hunt)
                    
                    #initialize current tan circle lists
                    tanx = []
                    tany = []

                    #if a circle on the tan list is clicked
                    for i in range((len(tan))):
                        tan[i]

                        #get the center
                        tancent = tan[i].getCenter()
                        tanx.append(tancent.getX())
                        tany.append(tancent.getY())

                        #if click is in range of a center of a tan circle
                        if huntx > (tanx[i] - 15) and huntx < (tanx[i] + 15):
                            if hunty > (tany[i] - 15) and hunty < (tany[i] + 15):
                                tan[i].setFill("tan")
                                
                    # initialize current grey lists
                    greyx = []
                    greyy = []

                    #if a grey circle is clicked
                    for i in range((len(grey))):
                        grey[i]

                        #get centers of the grey circles 
                        greycent = grey[i].getCenter()
                        greyx.append(greycent.getX())
                        greyy.append(greycent.getY())

                        #if click is in range of a grey circle, change its color
                        if huntx > (greyx[i] - 15) and huntx < (greyx[i] + 15):
                            if hunty > (greyy[i] - 15) and hunty < (greyy[i] + 15):
                                grey[i].setFill("grey")

                    #initialize white circle lists
                    whitex = []
                    whitey = []
                    
                    #if clicked and not in any of the lists, turn it white
                    for i in range(len(white)):
                        
                        #get centers
                        whitecent = white[i].getCenter()
                        whitex.append(whitecent.getX())
                        whitey.append(whitecent.getY())

                        #if click is in range of a white circle, turn its color
                        if huntx > (whitex[i] - 15) and huntx < (whitex[i] + 15):
                            if hunty > (whitey[i] - 15) and hunty < (whitey[i] + 15):
                                white[i].setFill("white")


                    
                    #for red circle location
                    redcent = red.getCenter()
                    redx = redcent.getX()
                    redy = redcent.getY()

                    
                    #if click in range of the red circle
                    if huntx > (redx - 15) and huntx < (redx + 15):
                        if hunty > (redy - 15) and hunty < (redy + 15):
                            red.setFill("red")
                            clickct += 5
                            #undraw previous click count
                            ctdisplay.undraw()

                            #draw new click count
                            ctdisplay = Text(Point(453,20), str(clickct))
                            ctdisplay.setSize(11)
                            ctdisplay.setTextColor("gold")
                            ctdisplay.draw(hunt)


                    #custom feature 1: the green speeder
                    #extra circle added, green. when found, moves quickly around
                    #the screen and will not disappear until clicked.
                    #green speeder must be caught before the game can continue
                    #for green circle location
                    greencent = green.getCenter()
                    greenx = greencent.getX()
                    greeny = greencent.getY()

                    #if click in range of the green speeder
                    if huntx > (greenx - 15) and huntx < (greenx + 15):
                        if hunty > (greeny - 15) and hunty < (greeny + 15):
                            green.setFill("green")
                            clickct += 1
                            #undraw previous click count
                            ctdisplay.undraw()

                            #draw new click count
                            ctdisplay = Text(Point(453,20), str(clickct))
                            ctdisplay.setSize(11)
                            ctdisplay.setTextColor("gold")
                            ctdisplay.draw(hunt)

                            #animate green circle
                            xdirectiongren = [8,-8]
                            ydirectiongren = [8,-8]
                            grexmove = random.choice(xdirectiongren)
                            greymove = random.choice(ydirectiongren)

                            greencenter = green.getCenter()
                            greenxpoint = greencenter.getX()
                            greenypoint = greencenter.getY()
                            radiusg = green.getRadius()

                            #reset click location
                            huntx = 0
                            hunty = 0

                            while (huntx < (greenxpoint-15) or huntx > (greenxpoint-15)) and (hunty < (greenypoint-15) or hunty > (greenypoint-15)):
        
                                    green.move(grexmove,greymove)
                                    radiusg = green.getRadius()
                                    greencenter = green.getCenter()
                                    greenxpoint = greencenter.getX()
                                    greenypoint = greencenter.getY()

                                    #undraw
                                    green.undraw()

                                    #redraw
                                    green = Circle(Point(greenxpoint,greenypoint), radiusg)
                                    green.setFill("green")
                                    green.draw(hunt)
                                    time.sleep(.03)

                                    #corners for bouncing
                                    corner1g = green.getP1()
                                    corner2g = green.getP2()
                                    corner1xg = corner1g.getX()
                                    corner1yg = corner1g.getY()
                                    corner2xg = corner2g.getX()
                                    corner2yg = corner2g.getY()

                                    #bounce away from the sides
                                    if corner1xg < 1 or corner2xg > 479:
                                        grexmove = -grexmove
                                    if corner1yg < 49 or corner2yg > 519:
                                        greymove = -greymove

                                    #check for click in game window
                                    gameclick = hunt.checkMouse()

                                    #update getX and getY for next loop
                                    if gameclick != None:
                                        huntx = gameclick.getX()
                                        hunty = gameclick.getY()

                            #undraw green circle after clicked
                            green.undraw()
                            huntx = 0
                            hunty = 0


                    #custom feature 2: hint button
                    #a blue  button added to the game window
                    #labeled "hint", when clicked chooses a grey
                    #circle at random to reveal. this adds 5
                    #to the click score. it can be done
                    #as many times as the player wants, though
                    #this is likely not a strategic choice

                    #hint button activation
                    if huntx > 312 and huntx < 348:
                        if hunty > 2 and hunty < 38:
                            print("Hint Activated. +5 to total score.")
                            clickct += 4
                            #undraw previous click count
                            ctdisplay.undraw()

                            #draw new click count
                            ctdisplay = Text(Point(453,20), str(clickct))
                            ctdisplay.setSize(11)
                            ctdisplay.setTextColor("gold")
                            ctdisplay.draw(hunt)

                            #randomly select from grey list
                            hintcircle = random.choice(grey)
                            hintcircle.setFill("grey")
                            
                    #for gold circle location
                    goldcent = gold.getCenter()
                    golx = goldcent.getX()
                    goly = goldcent.getY()

                    #if click in range of the gold circle
                    if huntx > (golx - 15) and huntx < (golx + 15):
                        if hunty > (goly - 15) and hunty < (goly + 15):

                            #change circle color
                            gold.setFill("gold")
                            
                            #winning actions below:
                            #combine all circles to a list for movement
                            combinelist = []
                            for i in range(len(tan)):
                                combinelist.append(tan[i])
                            for i in range(len(grey)):
                                combinelist.append(grey[i])
                            for i in range(len(white)):
                                combinelist.append(white[i])
                            combinelist.append(red)
                            combinelist.append(green)
                             
                            #move all circles downward together, leave gold one
                            for i in range(50):
                                for i in range(len(combinelist)):
                                    combinelist[i].move(0, 12)

                            #golden pete minigame
                            xdirectionlist = [5.5,-5.5]
                            ydirectionlist = [5.5,-5.5]
                            xmove = random.choice(xdirectionlist)
                            ymove = random.choice(ydirectionlist)

                            #until the circle disappears,
                            while gold.getRadius() > 0:
                                #move in randomly selected direction
                                gold.move(xmove,ymove)
                                #retreive radius value
                                radiusvalue = gold.getRadius()
                                #read for location
                                goldcenter = gold.getCenter()
                                goldxpoint = goldcenter.getX()
                                goldypoint = goldcenter.getY()
                                #undraw old, redraw new in new location
                                gold.undraw()
                                gold = Circle(Point(goldxpoint,goldypoint), radiusvalue - 0.17)
                                gold.setFill("gold")
                                gold.draw(hunt)
                                time.sleep(.05)

                                corner1 = gold.getP1()
                                corner2 = gold.getP2()
                                corner1x = corner1.getX()
                                corner1y = corner1.getY()
                                corner2x = corner2.getX()
                                corner2y = corner2.getY()
                                
                                if corner1x < 1 or corner2x > 479:
                                    xmove = -xmove
                                if corner1y < 49 or corner2y > 519:
                                    ymove = -ymove


                                #check for click in game window
                                gameclick = hunt.checkMouse()

                                if gameclick != None:
                                    huntx = gameclick.getX()
                                    hunty = gameclick.getY()

                                    
                                    if huntx > (goldxpoint - radiusvalue) and huntx < (goldxpoint + radiusvalue):
                                        if hunty > (goldypoint - radiusvalue) and hunty < (goldypoint + radiusvalue):

                                            #subtract 2 from click counter
                                            clickct -= 2

                                            #undraw previous click count
                                            ctdisplay.undraw()

                                            #draw new click count
                                            ctdisplay = Text(Point(453,20), str(clickct))
                                            ctdisplay.setSize(11)
                                            ctdisplay.setTextColor("gold")
                                            ctdisplay.draw(hunt)

                                
                            gold.undraw()
                            
                                                                    
                            #display you win, click here to continue
                            winmessage1 = Text(Point(240,275), "You Win!")
                            winmessage2 = Text(Point(240,300), "Click here to continue...")
                            winmessage2.setSize(8)
                            winmessage3 = Text(Point(240,225), ("Round Clicks: " + str(roundclicks)))
                            winmessage3.setSize(10)
                            winmessage4 = Text(Point(240,250), ("Round Clicks less than 10! -5 from total score!"))
                            winmessage4.setSize(12)
                            winmessage4.setStyle("bold")
                            winmessage1.draw(hunt)
                            winmessage2.draw(hunt)
                            winmessage3.draw(hunt)

                            if roundclicks < 11:
                                clickct -= 5
                                #undraw previous click count
                                ctdisplay.undraw()

                                #draw new click count
                                ctdisplay = Text(Point(453,20), str(clickct))
                                ctdisplay.setSize(11)
                                ctdisplay.setTextColor("gold")
                                ctdisplay.draw(hunt)
                                
                                winmessage4 = Text(Point(240,250), ("Round Clicks less than 10! -5 from total score!"))
                                winmessage4.setSize(12)
                                winmessage4.setStyle("bold")
                                winmessage4.draw(hunt)
                                hunt.setBackground("gold")
                                time.sleep(.5)
                                hunt.setBackground("white")
                                time.sleep(.5)
                                hunt.setBackground("gold")
                                time.sleep(.5)
                                hunt.setBackground("white")
                                time.sleep(.5)
                                hunt.setBackground("gold")
                                time.sleep(.5)
                                hunt.setBackground("white")
                                




                            #add to 5 count for rounds
                            counttofive += 1




                            #wait for click to start next round
                            hunt.getMouse()

                            #undraw previous round click count to update
                            rdclicks.undraw()

                            roundclicks = 0

                            #update display: clicks per round
                            rdclicks = Text(Point(149,20), roundclicks)
                            rdclicks.setSize(11)
                            rdclicks.setTextColor("gold")
                            rdclicks.draw(hunt)

                            #undraw winning messages
                            winmessage1.undraw()
                            winmessage2.undraw()
                            winmessage3.undraw()
                            winmessage4.undraw()

                            #round is over, restart while loop
                            roundfinish = 1

        #open scores file in append mode
        file = open("scores.txt","a")

        #combine name and score from game to a list
        combo = []
        combo.append(plname)
        combo.append(clickct)

        #write this list to the scores file on a new line
        file.write("\n"+str(combo))

        #close scores file
        file.close()

        #print game over message after undrawing you win messages
        winmessage1.undraw()
        winmessage2.undraw()
        winmessage3.undraw()
        winmessage4.undraw()

        over = Text(Point(240,230), "Game Over!")
        over.draw(hunt)
        over2 = Text(Point(240,250), "Click here to play again!")
        over2.draw(hunt)

        #wait for mouse click
        hunt.getMouse()

        #undraw current elements and restart!
        ctdisplay.undraw()
        rddisplay.undraw()
        rdclicks.undraw()
        for i in range(len(white)):
            white[i].undraw()
        for i in range(len(tan)):
            tan[i].undraw()
        for i in range(len(grey)):
            grey[i].undraw()
        gold.undraw()
        over.undraw()
        over2.undraw()
        main(90,150)  


    #from original ctrl panel loop,
    #start main from beginning if nothing was clicked
    #send 0,0 for x and y coords and wait .1 second
    #to prevent crashing from infinite loop
    else:
        time.sleep(.1)
        main(0,0)


#before even calling main function,
#open control panel:
name,newbox,exitb,ctrl = controlpanel()

#create game window
rounds, clicks, hunt = gamewindow()

#initialize clickx and y, wont do anything if set to 0 (no button here)
clickx = 0
clicky = 0

#call main function.
main(clickx,clicky)

