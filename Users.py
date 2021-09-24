import random
from views import mainPage
from validatePass import validatePass


class User:

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.loggedIn = True


def home(user):
    play_story()
    print("\nPlease type either: 'Login' or 'Register' or press '1' to see a video of a sucessful student who used InCollege!")
    a = input("What would you like to do: ")
    if (a == "register" or a == "Register"):
        register()
    elif (a == "Login" or a == "login"):
        login(user)
    elif(int(a) == 1):
        play_video()
    else:
        print("Choose a valid option")
        home('')


# 'r'- open a file for reading, 'w' - open a file for writing, '+' open a file for reading and writing
def register():
    print("-----------------------------")
    print("Welcome to the InCollege App!")
    print("-----------------------------")
    file = open("usernames.txt", "a")  # - file will be created if not present
    file2 = open("passwords.txt", "a")  # - file will be created if not present
    file3 = open("accounts.txt", "a")
    # Checks if there are already 5 accounts made this way
    if has_max_users():
        home('')

    # Checks if there is a duplicate username
    print("(Press '0' to return)")
    u = input("Please enter a unique username: ")
    if username_exists(u):
        print("Error, Username already created! Returning home")
        home('')

    if u == "0":
        home('')

    file.write(u + "\n")
    print("Note password requirements: minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, one non-alpha character")
    p = input("Please enter a valid password: ")
    res = validatePass(p)

    while res is False:
        if res is False:
            print("Error, Please meet password requirements:")
            print("---------------------------------------------")
            print("-minimum of 8 characters")
            print("-maximum of 12 characters")
            print("-at least one capital letter")
            print("-one digit, one non-alpha character")
            print("---------------------------------------------")
        p = input("Re-enter Password: ")
        res = validatePass(p)
    file2.write(p + "\n")
    Fname = input("What is your first name?: ")
    Lname = input("What is your last name?: ")

    file3.write(Fname + " " + Lname + "\n")

    file.close()
    file2.close()
    file3.close()
   

    print("\nHello, " + Fname)
    print("Account Created!")
    print("Entering main page....")
    mainPage()


def login(user):
    print("--------------------------")
    print("InCollege Login")
    print("--------------------------")
    file = open("usernames.txt", "a")
    file2 = open("passwords.txt", "a")
    indexU = 0
    

    filename = "usernames.txt"
    with open(filename) as file:
        linesU = file.readlines()
        linesU = [line.rstrip() for line in linesU]

    filename = "passwords.txt"
    with open(filename) as file:
        linesP = file.readlines()
        linesP = [line.rstrip() for line in linesP]

        print("(Press '0' to return)")
    u = input("Username:")
    with open('usernames.txt') as f:
        if u in f.read():
            indexU = linesU.index(u)
            u = True
        elif u == "0":
            home('')
        else:
            flag = False
            while flag == False:
                with open('usernames.txt') as f:
                    if u in f.read():
                        indexU = linesU.index(u)
                        break
                    else:
                        print("Error, Username is not recognized")
                        x = input("Enter username: ")
                        with open('usernames.txt') as f:
                            if x in f.read():
                                indexU = linesU.index(u)
                                flag = True
                                break
                            else:
                                flag = False
    file.close()
    file2.close()

    p = input("Password: ")
    flag = validatePass(p)


    if p == linesP[indexU]:
        mainPage()
    else:
        while p != linesP[indexU]:
            print("Error, Incorrect password")
            p = input("Enter password: ")
            if p == linesP[indexU]:
                break
        mainPage()

#def Get_or_find account():

def has_max_users():
    count = 0
    for line in open("usernames.txt", "r"): count += 1
    if count == 5 or count > 5:
        print("All permitted accounts have been created, please come backlater")
        return True
    return False


def username_exists(u):
    with open('usernames.txt') as f:
        if u in f.read():
            return True
        return False

def play_video():
    print("Video is now playing\n")
    a = input("Press '0' for home." )
    if(int(a) == 0):
        home('')

def play_story():
    n = random.randint(1, 3)
    if n == 1:
        story_1()
    elif n == 2:
        story_2()
    elif n == 3:
        story_3()
    
def story_1():
    return print("John L. Miller, 25 years at Microsoft, Amazon, Google, etc. C++, C, Java, Basic, etc. PhD.\n" +
    "'I loved computers. I taught myself to program in high school,\n" +
    "and thought I was pretty good at it (Apple Basic and 6502 assembler)\n" +
    "by the time I graduated. I got a job typesetting at a newspaper,\n" +
    "and enrolled in university part time, taking programming classes.'\n")
def story_2():
    return print("Hazim Hardeman, Communications Program Graduate, 2015\nWhen " +
    "Hazim Hardeman started at Community College of Philadelphia in 2012, his goals\n" +
    "were to raise his GPA and transfer to Temple University. He accomplished that and much more,\n"
    +"graduating from the College in 2015 with an associate degree in Communications with High Honors,")
def story_3():
    return print("Mark Zuckerberg has already accomplished much in his short life. In 2004,\n" +
    "he launched Facebook with a handful of his fellow college students, and 10 years later, the\n" +
    "website has more than 1 billion active users around the globe, and more than $12 billion in annual revenues.\n" +
    "'Helping a billion people connect is amazing, humbling and by far the thing I am most proud of in my life.'")
    


if __name__ == "__home('')__":
    home('')

home('')
