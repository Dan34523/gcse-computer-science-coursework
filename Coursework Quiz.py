# Imports the module for GUI
from tkinter import *

contents = None
usernames = []
line = None
current = 0
level = None
score = 0
subject = None
current_user = None
quizzes_taken = "Quizzes Taken:\n"

# Creates a window and renames the title to Quiz
root = Tk()
root.title("Quiz")
root.resizable(0, 0)


# Brings up the registration fields when the register button is pressed from the login screen
def registerpart1():
    usernameEntry.grid_forget()
    usernameLabel.grid_forget()
    passwordEntry.grid_forget()
    passwordLabel.grid_forget()
    registerButton.grid_forget()
    loginButton.grid_forget()
    statusLabel.grid_forget()

    registerInfo.grid(columnspan=2)
    nameLabel.grid(row=1, sticky=E)
    nameEntry.grid(row=1, column=1, sticky=W)
    ageLabel.grid(row=2, sticky=E)
    ageEntry.grid(row=2, column=1, sticky=W)
    year_groupLabel.grid(row=3, sticky=E)
    year_groupEntry.grid(row=3, column=1, sticky=W)
    newusernameLabel.grid(row=4, sticky=E)
    newusernameEntry.grid(row=4, column=1, sticky=W)
    newpasswordLabel.grid(row=5, sticky=E)
    newpasswordEntry.grid(row=5, column=1, sticky=W)
    registerconfirm.grid(row=6, columnspan=2, sticky=E, ipadx=5)


def check_if_username_exists(new_username):
    global usernames
    with open("User Logins.txt", "r") as f:
        lines = f.read().splitlines()
        usernames = []
        for detail in lines:
            usernames.append(detail.split("|")[2])
        if new_username in usernames:
            return True
        else:
            return False


# Processes all the data provided by the user in registerpart1()
def registerpart2():
    name = nameEntry.get()
    age = ageEntry.get()
    if newusernameEntry.get() == "":
        username = "{}{}".format(name[:3], age)
    else:
        username = newusernameEntry.get()
    year_group = year_groupEntry.get()
    newpassword = newpasswordEntry.get()

    if check_if_username_exists(username):
        registerInfo.config(text="Username already exists, please enter\ndifferent username")
        newusernameEntry.delete(0, END)
        newpasswordEntry.delete(0, END)
        root.after(4000, lambda: registerInfo.config(text="If you leave username blank, the program will assign one for you.\nThis may conflict with other usernames so your own will work best"))
        return

    with open("User Logins.txt", "a") as f:
        f.write("{}|{}|{}|{}|{}\n".format(name, age, username, year_group, newpassword))

    registerInfo.grid_forget()
    nameLabel.grid_forget()
    nameEntry.grid_forget()
    ageLabel.grid_forget()
    ageEntry.grid_forget()
    year_groupLabel.grid_forget()
    year_groupEntry.grid_forget()
    newusernameLabel.grid_forget()
    newusernameEntry.grid_forget()
    newpasswordLabel.grid_forget()
    newpasswordEntry.grid_forget()
    registerconfirm.grid_forget()

    restartLabel.grid()


# Checks if user has registered before logging in - prevents errors during login stage
def login_not_found():
    global usernames
    with open("User Logins.txt", "r") as f:
        lines = f.read().splitlines()
        usernames = []
        for detail in lines:
            usernames.append(detail.split("|")[2])
        if usernameEntry.get() not in usernames:
            return True
        else:
            return False


# Checks whether the username and password matches the record
def login():
    global details, current_user
    with open("User Logins.txt", "r") as f:
        lines = f.read().splitlines()
        for detail in lines:
            if detail.split("|")[2] == usernameEntry.get():
                details = detail
                break
        if login_not_found():
            statusLabel.config(text="User Details not found. Please register and try again")
            usernameEntry.delete(0, END)
            passwordEntry.delete(0, END)
            return

    if usernameEntry.get() == details.split("|")[2] and passwordEntry.get() == details.split("|")[4]:

        current_user = usernameEntry.get()

        usernameLabel.grid_forget()
        usernameEntry.grid_forget()
        passwordLabel.grid_forget()
        passwordEntry.grid_forget()
        loginButton.grid_forget()
        statusLabel.grid_forget()
        registerButton.grid_forget()

        takeQuiz.grid(columnspan=2, padx=5, pady=5)
        generateReport.grid(row=1, columnspan=2, padx=5, pady=5)

    else:
        statusLabel.config(text="Incorrect Password")
        root.after(3000, lambda: statusLabel.config(text=""))
        usernameEntry.delete(0, END)
        passwordEntry.delete(0, END)


def take_quiz():
    takeQuiz.grid_forget()
    generateReport.grid_forget()

    difficultySelectionLabel.grid(columnspan=2, padx=5, pady=5)
    easyButton.grid(row=1, columnspan=2, pady=2)
    mediumButton.grid(row=2, columnspan=2)
    hardButton.grid(row=3, columnspan=2, pady=2)


def choose_subject(difficulty):
    global level
    subjectLabel.grid(row=0, columnspan=2)
    physicsButton.grid(row=1, columnspan=2)
    mathsButton.grid(row=2, columnspan=2)
    genknowledgeButton.grid(row=3, columnspan=2)
    level = difficulty


def easy():
    difficultySelectionLabel.grid_forget()
    easyButton.grid_forget()
    mediumButton.grid_forget()
    hardButton.grid_forget()
    choose_subject("easy")


def medium():
    difficultySelectionLabel.grid_forget()
    easyButton.grid_forget()
    mediumButton.grid_forget()
    hardButton.grid_forget()
    choose_subject("medium")


def hard():
    difficultySelectionLabel.grid_forget()
    easyButton.grid_forget()
    mediumButton.grid_forget()
    hardButton.grid_forget()
    choose_subject("hard")


def physics():
    global level, contents, subject
    subject = "Physics"
    with open("Physics Questions.txt", "r") as f:
        contents = f.read().splitlines()
        if level == "easy":
            contents = contents[:5]
        elif level == "medium":
            contents = contents[5:10]
        elif level == "hard":
            contents = contents[10:]
        do_quiz(contents)


def genknowledge():
    global level, contents, subject
    subject = "General knowledge"
    with open("General Knowledge Questions.txt", "r") as f:
        contents = f.read().splitlines()
        if level == "easy":
            contents = contents[:5]
        elif level == "medium":
            contents = contents[5:10]
        elif level == "hard":
            contents = contents[10:]
        do_quiz(contents)


def maths():
    global level, contents, subject
    subject = "Maths"
    with open("Maths Questions.txt", "r") as f:
        contents = f.read().splitlines()
        if level == "easy":
            contents = contents[:5]
        elif level == "medium":
            contents = contents[5:10]
        elif level == "hard":
            contents = contents[10:]
        do_quiz(contents)


def click_a():
    global line, score, contents, current
    if line.split("|")[1] == "a":
        score += 1
    current += 1
    do_quiz(contents)


def click_b():
    global line, score, contents, current
    if line.split("|")[1] == "b":
        score += 1
    current += 1
    do_quiz(contents)


def click_c():
    global line, score, contents, current
    if line.split("|")[1] == "c":
        score += 1
    current += 1
    do_quiz(contents)


def click_d():
    global line, score, contents, current
    if line.split("|")[1] == "d":
        score += 1
    current += 1
    do_quiz(contents)


def do_quiz(questions):
    global line, current, level
    try:
        line = questions[current]
    except IndexError:
        final(level, subject)
    subjectLabel.grid_forget()
    physicsButton.grid_forget()
    mathsButton.grid_forget()
    genknowledgeButton.grid_forget()
    question.config(text=(line.split("|")[0]))
    if level == "easy":
        optionA.config(text=line.split("|")[2])
        optionB.config(text=line.split("|")[3])

        question.grid(columnspan=2)
        chooseA.grid(row=1, column=0, sticky=E)
        optionA.grid(row=1, column=1, sticky=W)
        chooseB.grid(row=2, column=0, sticky=E, pady=3)
        optionB.grid(row=2, column=1, sticky=W)

    elif level == "medium":
        optionA.config(text=line.split("|")[2])
        optionB.config(text=line.split("|")[3])
        optionC.config(text=line.split("|")[4])

        question.grid(columnspan=2)
        chooseA.grid(row=1, column=0, sticky=E)
        optionA.grid(row=1, column=1, sticky=W)
        chooseB.grid(row=2, column=0, sticky=E, pady=3)
        optionB.grid(row=2, column=1, sticky=W)
        chooseC.grid(row=3, column=0, sticky=E, pady=3)
        optionC.grid(row=3, column=1, sticky=W)

    elif level == "hard":
        optionA.config(text=line.split("|")[2])
        optionB.config(text=line.split("|")[3])
        optionC.config(text=line.split("|")[4])
        optionD.config(text=line.split("|")[5])

        question.grid(columnspan=2)
        chooseA.grid(row=1, column=0, sticky=E)
        optionA.grid(row=1, column=1, sticky=W)
        chooseB.grid(row=2, column=0, sticky=E, pady=3)
        optionB.grid(row=2, column=1, sticky=W)
        chooseC.grid(row=3, column=0, sticky=E, pady=3)
        optionC.grid(row=3, column=1, sticky=W)
        chooseD.grid(row=4, column=0, sticky=E, pady=3)
        optionD.grid(row=4, column=1, sticky=W)


def final(difficulty, topic):
    if difficulty == "easy":
        if score < 3:
            grade = "Fail"
        else:
            grade = "Pass"
    elif difficulty == "medium":
        if score == 0:
            grade = "Fail"
        elif score <= 4:
            grade = "Pass"
        else:
            grade = "Merit"
    else:
        if score == 0:
            grade = "Fail"
        elif score == 1:
            grade = "Pass"
        elif score <= 3:
            grade = "Merit"
        else:
            grade = "Distinction"
    percentage = (score / 5) * 100
    with open("Global Statistics.txt", "a") as f:
        f.write("{}|{}|{}|{}|{}|{}\n".format(current_user, topic, difficulty, score, percentage, grade))

    question.destroy()
    optionA.destroy()
    optionB.destroy()
    optionC.destroy()
    optionD.destroy()
    chooseA.destroy()
    chooseB.destroy()
    chooseC.destroy()
    chooseD.destroy()

    scoreLabel.config(text="You got {}/5".format(score))
    percentageLabel.config(text="That is {}%".format(percentage))
    gradeLabel.config(text="Grade: {}".format(grade))

    finishLabel.grid()
    scoreLabel.grid(row=1)
    percentageLabel.grid(row=2)
    gradeLabel.grid(row=3)


def generate_report():
    takeQuiz.grid_forget()
    generateReport.grid_forget()

    userreportButton.grid(columnspan=2, padx=5, pady=5)
    classreportButton.grid(columnspan=2, padx=5, pady=5)


def user_report():
    userreportButton.grid_forget()
    classreportButton.grid_forget()

    chooseuserLabel.grid(row=0, column=0, columnspan=2)
    chooseuserEntry.grid(row=1, column=0, columnspan=2)
    chooseuserConfirm.grid(row=2, column=0, columnspan=2)


def user_report_part2():
    global quizzes_taken, usernames
    if chooseuserEntry.get() in usernames:
        with open("Global Statistics.txt", "r") as f:
            results = f.read().splitlines()
        for result in results:
            if result.split("|")[0] == chooseuserEntry.get():
                quizzes_taken = "{}Subject: {}\tDifficulty: {}\tGrade: {}\n".format(quizzes_taken, result.split("|")[1], result.split("|")[2], result.split("|")[5])
        chooseuserLabel.grid_forget()
        chooseuserEntry.grid_forget()
        chooseuserConfirm.grid_forget()
        userreportLabel.config(text=quizzes_taken)
        userreportLabel.grid(padx=10, pady=10)
    else:
        chooseuserLabel.config(text="User not found")
        chooseuserEntry.delete(0, END)
        root.after(3000, lambda: chooseuserLabel.config(text="Write the username you wish to generate a report for"))
        return


def class_report():
    userreportButton.grid_forget()
    classreportButton.grid_forget()
    subjectreportLabel.grid(row=0, columnspan=2, padx=10, pady=5)
    subjectEntry.grid(row=2, columnspan=2, padx=10)
    difficultyreportLabel.grid(row=4, columnspan=2, padx=10, pady=5)
    difficultyEntry.grid(row=5, columnspan=2, padx=10)
    choosereportConfirm.grid(row=6, column=1, sticky=E)


def class_report_part2():
    subjectchosen = subjectEntry.get().lower()
    difficultychosen = difficultyEntry.get().lower()
    total = 0
    highest_score = 0
    scores = []
    if subjectchosen.lower() not in ["maths", "physics", "general knowledge"] or difficultychosen.lower() not in ["easy", "medium", "hard"]:
        subjectEntry.delete(0, END)
        difficultyEntry.delete(0, END)
        subjectreportLabel.config(text="Please enter correct subject")
        difficultyreportLabel.config(text="Please enter correct difficulty")
        root.after(3000, lambda: subjectreportLabel.config(text="Select the subject you want to generate a report on\nOptions are: Maths, Physics or General Knowledge"))
        difficultyreportLabel.config(text="Select the difficulty\nOptions are: Easy, Medium or Hard")
        return
    else:
        with open("Global Statistics.txt", "r") as f:
            results = f.read().splitlines()
        for result in results:
            if result.split("|")[1].lower() == subjectchosen and result.split("|")[2].lower() == difficultychosen:
                total += float(result.split("|")[4])
                scores.append("{},{}".format(result.split("|")[0], result.split("|")[4]))
                if float(result.split("|")[4]) > float(highest_score):
                    highest_score = result.split("|")[4]

    average = round((total / len(scores)), 2)
    subjectreportLabel.grid_forget()
    subjectEntry.grid_forget()
    difficultyreportLabel.grid_forget()
    difficultyEntry.grid_forget()
    choosereportConfirm.grid_forget()
    highestachievers = ""
    for person in scores:
        if person.split(",")[1] == highest_score:
            highestachievers = "{} {}".format(highestachievers, person.split(",")[0])
    highestscoreLabel.config(text="The highest score was {} achieved by:\n{}".format(highest_score, highestachievers))
    averagescoreLabel.config(text="The average score was {}".format(average))
    highestscoreLabel.grid(row=0, columnspan=2, padx=10, pady=10)
    averagescoreLabel.grid(row=1, columnspan=2, padx=10, pady=10)


# The widgets for the login screen
usernameLabel = Label(root, text="Username:")
usernameEntry = Entry(root)
passwordLabel = Label(root, text="Password:")
passwordEntry = Entry(root, show="*")
loginButton = Button(root, text="Login", command=login)
registerButton = Button(root, text="Register Here", command=registerpart1)
statusLabel = Label(root, text="", width=40)

# The widgets for the register screen
registerInfo = Label(root, text="If you leave username blank, the program will assign one for you.\nThis may conflict with other usernames so your own will work best", width=50)
nameEntry = Entry(root)
nameLabel = Label(root, text="Name:")
ageEntry = Entry(root)
ageLabel = Label(root, text="Age:")
year_groupEntry = Entry(root)
year_groupLabel = Label(root, text="Year Group:")
newusernameEntry = Entry(root)
newusernameLabel = Label(root, text="Username:")
newpasswordEntry = Entry(root, show="*")
newpasswordLabel = Label(root, text="New Password:")
registerconfirm = Button(root, text="Next", command=registerpart2)
restartLabel = Label(root, text="Please restart the program and login\n\nYour username is the first 3 letters of your name\nfollowed by your age unless you made your\nown username.")

# Options after logging in
takeQuiz = Button(root, text="Take the Quiz", width=30, command=take_quiz)
generateReport = Button(root, text="Generate a report", width=30, command=generate_report)

# Buttons to choose subjects and difficulty
difficultySelectionLabel = Label(root, text="Choose the difficulty. If you choose a\nlower difficulty you are capped at a lower grade")
easyButton = Button(root, text="Easy", command=easy, width=20)
mediumButton = Button(root, text="Medium", command=medium, width=20)
hardButton = Button(root, text="Hard", command=hard, width=20)
subjectLabel = Label(root, text="Select the subject you wish to take a quiz on", width=40)
physicsButton = Button(root, text="Physics", command=physics, width=20)
genknowledgeButton = Button(root, text="General Knowledge", command=genknowledge, width=20)
mathsButton = Button(root, text="Maths", command=maths, width=20)

# Questions and answer widgets
question = Label(root, text="", width=50, wraplength=200)
chooseA = Button(root, text="A", width=3, command=click_a)
optionA = Label(root, text="", width=20)
chooseB = Button(root, text="B", width=3, command=click_b)
optionB = Label(root, text="", width=20)
chooseC = Button(root, text="C", width=3, command=click_c)
optionC = Label(root, text="", width=20)
chooseD = Button(root, text="D", width=3, command=click_d)
optionD = Label(root, text="", width=20)

# Widgets for the final screen
finishLabel = Label(root, text="Congrats! You have finished the quiz. See below for your scores.")
scoreLabel = Label(root, text="")
percentageLabel = Label(root, text="")
gradeLabel = Label(root, text="")

# Widgets for generating a report
userreportButton = Button(root, text="Generate for a specific user", command=user_report, width=30)
classreportButton = Button(root, text="Generate for all users", command=class_report, width=30)
chooseuserLabel = Label(root, text="Write the username you wish to generate a report for", wraplength=300, width=40)
chooseuserEntry = Entry(root)
chooseuserConfirm = Button(root, text="Next", command=user_report_part2, width=10)
userreportLabel = Label(root, text=quizzes_taken)
subjectreportLabel = Label(root, text="Select the subject you want to generate a report on\nOptions are: Maths, Physics or General Knowledge")
subjectEntry = Entry(root)
difficultyreportLabel = Label(root, text="Select the difficulty\nOptions are: Easy, Medium or Hard")
difficultyEntry = Entry(root)
choosereportConfirm = Button(root, text="Next", command=class_report_part2)
highestscoreLabel = Label(root, text="")
averagescoreLabel = Label(root, text="", width=40)

# Places the login widgets in their correct positions for when the user opens the program
usernameLabel.grid(row=0, column=0, sticky=E)
usernameEntry.grid(row=0, column=1, sticky=W)
passwordLabel.grid(row=1, column=0, sticky=E)
passwordEntry.grid(row=1, column=1, sticky=W)
statusLabel.grid(row=2, columnspan=2)
loginButton.grid(row=3)
registerButton.grid(row=3, column=1)

root.mainloop()
