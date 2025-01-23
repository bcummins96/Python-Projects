#
# Benjamin Cummins
# this program reads the contents of 2 files, combining the elements into pairs to store as a list.
# it then counts the occurences of each possible value and saves this report as a text file.
# sample text files are provided.


#define main function
def main():

    #function desc
    print("This program reads the contents of 2 files,")
    print("combining the elements into pairs to store as a list.")
    print("It then counts the occurences of each possible value")
    print("and saves this report as a text file.")
    print("")

    #prompt for filenames
    Lfile = input("Please enter left file: ")
    Rfile = input("Please enter right file: ")

    #run match function with this data
    matchresult = match(Lfile,Rfile)

    #run occurresult with returned value
    occurresult = occur(matchresult)

    #print table
    print("Alien Protein Analysis")
    print("Pair          Occurences")
    print("==========================")
    for i in range(8):
        current = occurresult[i]
        print(current[0],"           ",current[1])


#define match function
def match(x,y):
    print("Reading and Processing Protein Pairs...")
    print("")

    #open files
    xfile = open(x)
    yfile = open(y)

    #read into one data string
    xstr = xfile.read()
    ystr = yfile.read()

    #initialize lists
    xlist = []
    ylist = []
    mixlist = []

    #for loop to append lists
    for i in range(len(xstr)):
        xlist.append(xstr[i])
        ylist.append(ystr[i])

    
    #combine lists
    for i in range(len(ystr)):
        z = xlist[i] + ylist[i]
        mixlist.append(z)

    #close files
    xfile.close()
    yfile.close()

    return mixlist
    
#define occur function
def occur(mixlist):
    print("Counting Occurrences...")
    print("")

    #initialize list
    occurlist = []

    #initialize counts
    cGcount = 0
    mGcount = 0
    tGcount = 0
    sGcount = 0
    cVcount = 0
    mVcount = 0
    tVcount = 0
    sVcount = 0

    #for loop to count occurences
    for i in range(len(mixlist)):
        if mixlist[i] == "cG":
            cGcount += 1
        if mixlist[i] == "mG":
            mGcount += 1
        if mixlist[i] == "tG":
            tGcount += 1
        if mixlist[i] == "sG":
            sGcount += 1
        if mixlist[i] == "cV":
            cVcount += 1
        if mixlist[i] == "mV":
            mVcount += 1
        if mixlist[i] == "tV":
            tVcount += 1
        if mixlist[i] == "sV":
            sVcount += 1

    #create mini lists
    cGlist = ["cG", cGcount]
    mGlist = ["mG", mGcount]
    tGlist = ["tG", tGcount]
    sGlist = ["sG", sGcount]
    cVlist = ["cV", cGcount]
    mVlist = ["mV", mGcount]
    tVlist = ["tV", tGcount]
    sVlist = ["sV", sGcount]

    #add to master list
    occurlist.append(cGlist)
    occurlist.append(mGlist)
    occurlist.append(tGlist)
    occurlist.append(sGlist)
    occurlist.append(cVlist)
    occurlist.append(mVlist)
    occurlist.append(tVlist)
    occurlist.append(sVlist)
    

    #return value        
    return occurlist
    

main()

