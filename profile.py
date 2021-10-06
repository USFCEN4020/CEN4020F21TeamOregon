from re import DOTALL
import csv


class Profile:
    def __init__(self, name, title, major, university, about):
        self.name = name
        self.title = title
        self.major = major
        self.university = university
        self.about = about


def profileMenu(username):
    global profileList, profileExists, user
    user = username
    profileExists = False
    profileList = []
    userProfile = Profile(username, "", "", "", "")


    profileFile = open("profile.txt", "r")
    for line in profileFile:
        if line != '\n':
            u, t, n, m, p = line.split('\t')
            profile = Profile(u, t, n, m, p)
            profileList.append(profile)
            if (profile.name == username):
                userProfile = profile
                profileExists = True
    profileFile.close()

    if profileExists:
        showProfile(userProfile)
    else:
        addProfileTitle(userProfile)
        addProfileMajor(userProfile)
        addProfileUniversity(userProfile)
        addProfileParagraph(userProfile)
        addExperience()
        addEducation()

    if len(profileList) == 0 or not profileExists:
        profileList.append(userProfile)

    profileFileWrite1 = open("profile.txt", 'w')
    profileFileWrite1.close()


    for profl in profileList:
        profileFileWrite = open("profile.txt", 'a')
        if profl.name == userProfile.name:
            profl = userProfile
        profileFileWrite.write(profl.name + '\t' +
                               profl.title + '\t' +
                               profl.major + '\t' +
                               profl.university + '\t' +
                               profl.about)
        profileFileWrite.close()

    return


def showProfile(userProfile):
    cmd = ""
    while (cmd != '0'):

        educationFile = open("profile_education.txt", 'r')
        print("")
        print("--------------------")
        print("|    My Profile    |")
        print("--------------------")
        print("")
        print(userProfile.name)
        print("")
        print("Title: " + userProfile.title)
        print("Major: " + userProfile.major)
        print("University: " + userProfile.university)
        print("About Me: " + userProfile.about)
        print("")

        print("")
        print("------------------------------")
        print("| '1' to edit title          |")
        print("| '2' to edit major          |")
        print("| '3' to edit university     |")
        print("| '4' to edit about info     |")
        print("| '5' to edit experience     |")
        print("| '6' to edit education      |")
        print("| '0' to return to main page |")
        print("------------------------------")
        cmd = input("What would you like to do: ")

        if (cmd == '1'):
            addProfileTitle(userProfile)
        elif (cmd == '2'):
            addProfileMajor(userProfile)
        elif (cmd == '3'):
            addProfileUniversity(userProfile)
        elif (cmd == '4'):
            addProfileParagraph(userProfile)
        elif (cmd == '5'):
            addExperience()
        elif (cmd == '6'):
            addEducation()
        elif (cmd == '0'):
            return
        else:
            print("Invalid input, please try again")
            print("")


def addProfileTitle(userProfile):
    print("")
    print("***********")
    print("*  Title  *")
    print("***********")
    cmd = input("Add a title or press '0' to return: ")

    if (cmd == '0'):
        return

    userProfile.title = cmd
    return


def addProfileMajor(userProfile):
    print("")
    print("**********")
    print("*  Major *")
    print("**********")
    cmd = input("Add a major or press '0' to return: ")

    if (cmd == '0'):
        return

    major = ""
    majorParse = cmd.split()
    for word in majorParse:
        major += word.capitalize() + " "

    userProfile.major = major
    return

def addProfileUniversity(userProfile):
    print("")
    print("***************")
    print("*  University *")
    print("***************")
    cmd = input("Add a university or press '0' to return: ")

    if (cmd == '0'):
        return

    university = ""
    universityParse = cmd.split()
    for word in universityParse:
        university += word.capitalize() + " "

    userProfile.university = university
    return


def addProfileParagraph(userProfile):
    print("")
    print("**************")
    print("*  About Me  *")
    print("**************")
    cmd = input("Add about info or press '0' to return: ")

    if (cmd == '0'):
        return

    userProfile.about = cmd
    return


def addExperience():
    keep_add = "y"
    decision = input("Would you like to enter experience in your profile? (y/n)")

    if (decision == "y" or decision == "Y"):

        while (keep_add == "y" or keep_add == "Y"):
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

    elif (decision == "n" or decision == "N"):
        print("No experience ")

    else:
        print("Invalid input please try again.")


def has_max_experience():
    count = 0
    for line in open("profile_experience.txt", "r"): count += 1
    if (count == 3):
        print("All permitted experiences have been entered.")
        return True
    return False


def saveExperience(t, e, ds, de, l, d):
    file = open("profile_experience.txt", "a")
    file.write(t + "\t" + e + "\t" + ds + "\t" + de + "\t" + l + "\t" + d + "\n")
    file.close()


def addEducation():
    keep_add = "y"

    while (keep_add == "y" or keep_add == "Y"):
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
