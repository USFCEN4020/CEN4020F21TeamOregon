from re import DOTALL


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
        addExperience()
        addEducation()

def showProfile():


def addProfileTitle():


def addProfileMajor():


def addProfileUniversity():


def addProfileParagraph():


def addExperience():
    keep_add = "y"
    decision = input("Would you like to enter experience in your profile? (y/n)")

    if(decision == "y" or decision == "Y"):
        
        while(keep_add == "y" or keep_add == "Y"):
            if (has_max_experience):
                return
            title = input("Enter the title for your job: ")
            employer = input("Enter the employer for your job: ")
            date_started = input("Enter the date you started the job: ")
            date_ended = input("Enter the date ended the job: ")
            location = input("Enter the location for your job: ")
            description = input("Enter the description of what you did: ")
        
            saveExperience(title, employer, date_started, date_ended, location, description)

            keep_add = input("Would you like to add more experience?(y/n)")
           
        print("Experience successfully added")

    elif(decision == "n" or decision == "N"):
        print("No experience ")
    
    else:
        print("Invalid input please try again.")

def has_max_experience():
    count = 0
    for line in open("profile_experience.txt", "r"): count += 1
    if (count == 3 ):
        print("All permitted experiences have been entered.")
        return True
    return False

def saveExperience(t, e, ds, de, l, d):
    file = open("profile_experience.txt", "a")
    file.write(t + "\t" + e + "\t" + ds + "\t" + de + "\t" + l + "\t" + d + "\n")
    file.close()

def addEducation():
    keep_add = "y"

    while(keep_add == "y" or keep_add == "Y"):
        school_name = input("Enter the name of the school: ")
        degree = input("Enter the degree: ")
        years_attended = input("Enter the year you attended: ")
              
        saveEducation(school_name, degree, years_attended)

        keep_add = input("Would you like to add more education?(y/n)") 
    
    print("Education successfully added")


def saveEducation(s, d, y):
    file = open("profile_education.txt", "a")
    file.write(s + "\t" + d + "\t" + y + "\n")
    file.close()