# Benjamin Cummins
# this program retreives data from an excel file and summarizes it to a table.

# levels are Platinum or Gold
# industries are Sports, Technology, Food, Media, Service
# sales.csv file is included

#define total function
def total(level,industry):

    #print table header
    print("")
    print("Summary for "+ industry + " " + level + " customers")
    print("")
    print("Company          Contact       State          Total")
    print("="*80)

    #open files
    sales = open("sales.csv")

    #read data into saleslist
    saleslist = sales.readlines()

    #series of if loops based on user input determine what will be shown

    #gold series
    if level == "Gold" and industry == "Food":

        #run through list
        for i in range(100):

            #select specified input
            if (saleslist[i].count("Gold") != 0) and (saleslist[i].count("Food") != 0):

                #split the row in the list into a small list
                y = saleslist[i].split(",")

                #add number values
                j = float(y[5])
                k = float(y[6])
                l = float(y[7])
                m = float(y[8])
                addition = j + k + l + m

                #print company name, contact, state and total
                print(y[0], "\t", y[1], "\t", "\t", y[2], "\t", addition)

    #gold series
    if level == "Gold" and industry == "Media":

        #run through list
        for i in range(100):

            #select specified input
            if (saleslist[i].count("Gold") != 0) and (saleslist[i].count("Media") != 0):

                #split the row in the list into a small list
                y = saleslist[i].split(",")

                #add number values
                j = float(y[5])
                k = float(y[6])
                l = float(y[7])
                m = float(y[8])
                addition = j + k + l + m

                #print company name, contact, state and total
                print(y[0], "\t", y[1], "\t", "\t", y[2], "\t", addition)

    #gold series
    if level == "Gold" and industry == "Technology":

        #run through list
        for i in range(100):

            #select specified input
            if (saleslist[i].count("Gold") != 0) and (saleslist[i].count("Technology") != 0):

                #split the row in the list into a small list
                y = saleslist[i].split(",")

                #add number values
                j = float(y[5])
                k = float(y[6])
                l = float(y[7])
                m = float(y[8])
                addition = j + k + l + m

                #print company name, contact, state and total
                print(y[0], "\t", y[1], "\t", "\t", y[2], "\t", addition)

    #gold series
    if level == "Gold" and industry == "Sports":

        #run through list
        for i in range(100):

            #select specified input
            if (saleslist[i].count("Gold") != 0) and (saleslist[i].count("Sports") != 0):

                #split the row in the list into a small list
                y = saleslist[i].split(",")

                #add number values
                j = float(y[5])
                k = float(y[6])
                l = float(y[7])
                m = float(y[8])
                addition = j + k + l + m

                #print company name, contact, state and total
                print(y[0], "\t", y[1], "\t", "\t", y[2], "\t", addition)

    #gold series
    if level == "Gold" and industry == "Service":

        #run through list
        for i in range(100):

            #select specified input
            if (saleslist[i].count("Gold") != 0) and (saleslist[i].count("Service") != 0):

                #split the row in the list into a small list
                y = saleslist[i].split(",")

                #add number values
                j = float(y[5])
                k = float(y[6])
                l = float(y[7])
                m = float(y[8])
                addition = j + k + l + m

                #print company name, contact, state and total
                print(y[0], "\t", y[1], "\t", "\t", y[2], "\t", addition)


#Begin platinum series


    #Platinum series
    if level == "Platinum" and industry == "Food":

        #run through list
        for i in range(100):

            #select specified input
            if (saleslist[i].count("Platinum") != 0) and (saleslist[i].count("Food") != 0):

                #split the row in the list into a small list
                y = saleslist[i].split(",")

                #add number values
                j = float(y[5])
                k = float(y[6])
                l = float(y[7])
                m = float(y[8])
                addition = j + k + l + m

                #print company name, contact, state and total
                print(y[0], "\t", y[1], "\t", "\t", y[2], "\t", addition)

    #Platinum series
    if level == "Platinum" and industry == "Media":

        #run through list
        for i in range(100):

            #select specified input
            if (saleslist[i].count("Platinum") != 0) and (saleslist[i].count("Media") != 0):

                #split the row in the list into a small list
                y = saleslist[i].split(",")

                #add number values
                j = float(y[5])
                k = float(y[6])
                l = float(y[7])
                m = float(y[8])
                addition = j + k + l + m

                #print company name, contact, state and total
                print(y[0], "\t", y[1], "\t", "\t", y[2], "\t", addition)

    #Platinum series
    if level == "Platinum" and industry == "Technology":

        #run through list
        for i in range(100):

            #select specified input
            if (saleslist[i].count("Platinum") != 0) and (saleslist[i].count("Technology") != 0):

                #split the row in the list into a small list
                y = saleslist[i].split(",")

                #add number values
                j = float(y[5])
                k = float(y[6])
                l = float(y[7])
                m = float(y[8])
                addition = j + k + l + m

                #print company name, contact, state and total
                print(y[0], "\t", y[1], "\t", "\t", y[2], "\t", addition)

    #Platinum series
    if level == "Platinum" and industry == "Sports":

        #run through list
        for i in range(100):

            #select specified input
            if (saleslist[i].count("Platinum") != 0) and (saleslist[i].count("Sports") != 0):

                #split the row in the list into a small list
                y = saleslist[i].split(",")

                #add number values
                j = float(y[5])
                k = float(y[6])
                l = float(y[7])
                m = float(y[8])
                addition = j + k + l + m

                #print company name, contact, state and total
                print(y[0], "\t", y[1], "\t", "\t", y[2], "\t", addition)

    #Platinum series
    if level == "Platinum" and industry == "Service":

        #run through list
        for i in range(100):

            #select specified input
            if (saleslist[i].count("Platinum") != 0) and (saleslist[i].count("Service") != 0):

                #split the row in the list into a small list
                y = saleslist[i].split(",")

                #add number values
                j = float(y[5])
                k = float(y[6])
                l = float(y[7])
                m = float(y[8])
                addition = j + k + l + m

                #print company name, contact, state and total
                print(y[0], "\t", y[1], "\t", "\t", y[2], "\t", addition)



#testing 
total("Gold", "Sports")