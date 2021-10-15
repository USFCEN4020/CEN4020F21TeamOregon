from profile import Profile
import profile as p1
import profile
from friend import Friend


def showProfile1(userProfile):
    print("")
    print("-------------------------------------")
    print(  userProfile.name + " Profile")
    print("-------------------------------------")
    print("")
    print(userProfile.name)
    print("")
    print("Title: " + userProfile.title)
    print("Major: " + userProfile.major)
    print("University: " + userProfile.university)
    print("About Me: " + userProfile.about)

    print("Experience: ")     
    experienceFile = open("profile_experience.txt", "r")
    for line in experienceFile:
        if line != '\n':
            u, t, e, ds, de, l, d = line.split('\t')
            if (u == userProfile):
                print("Title: " + t)
                print("Employer: " + e)
                print("Date started: " + ds)
                print("Date ended: " + de)
                print("Location: " + l)
                print("Description: " + d)
    experienceFile.close()

    print("\nEducation: ")
    educationFile = open("profile_education.txt", "r")
    for line in educationFile:
        if line != '\n':
            u, s, d, y= line.split('\t')
            if (u == userProfile):
                print("School name: " + s)
                print("Degree: " + d)
                print("Year entered: " + y)
    educationFile.close()

    print("-------------------------------------")




#from profile import showProfile
#SHOW FRIEND LIST FUNCTION
#login_name = username here hmm
#what is the username though? 
def friendList1(username):
    profileExists = False

    friendWithProfileCount = -1
    friendWithProfileMap = {}

    count_friend = -1
    print("-------------------------------------")
    print("| Friend List                       |")
    
    friendFile = open("friendList.txt", "r")
    profileFile = open("profile.txt", "r")

    for line in friendFile:
        if line != '\n':
            line = line.rstrip()
            u, fu = line.split('\t')

            #print("u: " + u + ", fu: " + fu + "|")
            if (u == username or fu == username):
                count_friend += 1
                #user friend 
                #friend user
                #when 1st user name is the user

                #when the username is the user
                if(u == username):
                    #check if has profile: 
                    for line in profileFile:
                        if line != '\n':
                            line = line.rstrip()
                            u, t, n, m, p = line.split('\t')
                            profile = Profile(u, t, n, m, p)
                            #print("THe name : |" + profile.name + "|" )
                            if (profile.name == fu):
                                #print("there a profile exist")
                                profileExists = True
                                friendWithProfileCount +=1

                    #profileFile.close()
                    if(profileExists):
                        friendWithProfileMap[friendWithProfileCount] = {fu}
                        print("Friend name: " + fu + ", "+ str(friendWithProfileCount) +"(has profile)")
                    else: print("Friend name: " + fu)
                    # else does not have 

                #when the 2nd username is the user
                else:
                    #check if friend has profile
                    for line in profileFile:
                        if line != '\n':
                            line = line.rstrip()
                            u, t, n, m, p = line.split('\t')
                            profile = Profile(u, t, n, m, p)
                            if (profile.name == u):
                                friendWithProfileCount +=1
                                profileExists = True
                    #profileFile.close()
                    if(profileExists):
                        friendWithProfileMap[friendWithProfileCount] = {u}
                        print("Friend username: " + u  + ", "+ str(friendWithProfileCount) +"(has profile)")
                    else: print("Friend username: " + u)
                
        profileExists = False

    #print("0 element in map: "+ str(friendWithProfileMap.get(0)).replace("{","").replace("}", "").replace("'",""))

    #print(str(d).replace("{","").replace("}", ""))

     
    #print("friend: " + str(count_friend))

    #print()
    if(count_friend == -1):
        print("| No friend to show                 |")
        print("-------------------------------------")
        profileFile.close()
        friendFile.close() 
    else:
        #optionInput = input("Do you want to view friends' profile(yes/no): ")
        #if optionInput == "yes":

        #print("this is the length: "+ str(len(friendWithProfileMap)))

        profileInputSelect = "0"
        
        while( profileInputSelect !=  "-1"):

            profileInputSelect = input("| Enter the coresspond number next to the has profile to see the profile "
                            + "or enter -1 to exit|")

            profileInputSelect = showProfileOptions_InputValidate1(profileInputSelect)

            #while int(profileInputSelect) > len(friendWithProfileMap):
            #if not friendWithProfileMap.has_key(int(profileInputSelect)):
            #while int(profileInputSelect) not in friendWithProfileMap or profileInputSelect != -1:
            if profileInputSelect in friendWithProfileMap:
                profileInputSelect = input("Please put an integer corespond to a has profile selection")
                print("Current profile input: " + profileInputSelect)
              
            #print()

            #selected a number in the range 
            elif profileInputSelect == -1:
                #testing
                print("exiting...")
            else: 
                #print("in the map!!")
                profileFile = open("profile.txt", "r")
                for line in profileFile:
                    if line != '\n':
                        u, t, n, m, p = line.split('\t')
                        profile = Profile(u, t, n, m, p)
                        nameToCompare = str(friendWithProfileMap.get(int(profileInputSelect))).replace("{","").replace("}", "").replace("'","")

                        #print("Profile name: " + profile.name)
                        #print("Name to compare: " + nameToCompare)
                        if (profile.name == nameToCompare):
                            #print("it is equal")
                            userProfile = profile
                            showProfile1(userProfile)
                profileFile.close()

            
            

def showProfileOptions_InputValidate1(userInput):
    while True:
        try:
            int(userInput)
        except ValueError:
            userInput = input("Please input an valid integer options")
            continue
        else:
            return userInput

def test():
    friendFileWrite = open("friendList.txt", 'a')
            
    friendFileWrite.write("Student Learner" + '\t' +
                    "Student2 Learner2" + '\n')
    friendFileWrite.close()

def add_to_friendList():
    friendFile = open("friendList.txt", 'a')
    friendFile.write("Student2 Learner2\tStudent Learner3\n")
    friendFile.write("Student2 Learner2\tStudent Learner4\n")

def set_testprofile():
    profileFile = open("profile.txt",'a')

    student = ["Student Learner3","Student Learner4","Student Learner5","Student Learner6"	]
    profile = "t\tM\tU\ta\n"
    for s in student:
        profileFile.write(s + '\t' + "a" + '\t' + "M"
                    +'\t'+"A" + '\t'+"c"+'\n')
        #profileFile.write()





#test()
#add_to_friendList()
#set_testprofile()
friendList1("Student2 Learner2")


    
    
    	


def get_exp():
    print("")

def get_edu():
    print("")




