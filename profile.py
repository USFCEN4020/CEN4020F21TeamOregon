def profileMenu(username):

    global user
    user = username

    # show profile if one created
    # else add profile info
    profileFile = open("profile.txt", "r")
    if username in profileFile:
        showProfile()
    else:
        addProfileTitle()
        addProfileMajor()
        addProfileUniversity()
        addProfileParagraph()



def showProfile():


def addProfileTitle():


def addProfileMajor():


def addProfileUniversity():


def addProfileParagraph():
