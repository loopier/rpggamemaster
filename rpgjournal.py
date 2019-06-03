import datetime 

def getDateStamp():
    return "{:%Y%m%d-%H%M%S}".format(datetime.datetime.now())

def openJournal(filename=None):
    try:
        # filename = "journals/" + str(filename)
        with open(filename, "w+") as file:
            file.write("alo\n")
    except Exception as e:
        print("Error opening journal")
        print(type(e).__name__, ":", e)

def promptForNewJournal():
    pass

openJournal()
openJournal("journals/one.md")
openJournal("journals/two.md")
