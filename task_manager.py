#=====importing libraries===========
from datetime import date 
from datetime import datetime
from tabulate import tabulate
import os

""""Functions"""

def save_users(): 
    """Opens user.txt and returns data as a list of lists."""
    list = []
    with open("user.txt", "r")as file:
        for line in file:
            list.append(make_list(line))
    return list


def save_tasks(): 
    """Saves tasks.txt to memory as list of lists"""
    list = []
    with open("tasks.txt", "r")as file:
        for line in file:
            list.append(make_list(line))
    return list
    

def reg_user(): 
    """
    Registers a new user, performing validation checks and appends 
    new user to user.txt
    """
    valid_user = False
    valid_pass = False
    
    # Validation loop until registration is successful
    while valid_user == False:
        # Request inputs for new username and password
        new_user = input("Enter new username: ")
    
        # Error if username is registered already
        if new_user not in username_list:
            valid_user = True
        else:
            print("This user already exists!")
            
    # If username is valid ask for password
    if valid_user == True:    
        new_password = input("Enter your desired password: ")
        # Accept unique passwords
        if new_password not in password_list:
            valid_pass = True
        else:
            print("This password is not secure.")
    
    if valid_user == True and valid_pass == True:
        # Request confirmation of password
        password_confirmation = input("Confirm your password: ")

        # Check if passwords match and write to user.txt if they
        # do, else print error
        if password_confirmation == new_password:
            with open("./user.txt", "a") as add_login:
                add_login.write("\n" +new_user + ", " + new_password)
            print("\nUser created!\n")
        else:
            print("Passwords do not match, New user not created.")


def add_task(assign_user): 
    """
    Asks for input details to create a new task and append to tasks.txt.
    """
    # Request user input
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter a description of the task: ")
    datetime_today = date.today()
    today = datetime.strftime(datetime_today, "%d %b %Y")
    due_date = input("Enter due date (DD Mon YYYY): ")
    
    # Open the tasks file and add new task using appropriate formatting
    with open("./tasks.txt", "a") as taskfile:
        taskfile.write("\n" + assign_user + ", " + task_title + ", " + 
                        task_description + ", " + today + ", " + 
                        due_date + ", " + "No")
        

def view_all(): 
    """
    This function reads the tasks.txt file and prints the data 
    to the terminal.
    """
    with open("./tasks.txt", "r") as va_tasks:
        for line in va_tasks:
            make_list(line)
            print_line(make_list(line))


def view_mine(): 
    """View current user's tasks, and make changes as required"""
    # Create new list to store current user's tasks
    current_task_list = [] 
    with open("./tasks.txt", "r") as va_tasks:
        has_tasks = False 
        # Used for titling and menu selection
        task_number = 0 

        # make list of tasks and print to screen
        for line in va_tasks: 
            current_task = make_list(line)
            if current_task[0] == username:
                print(f"Task {task_number + 1}")
                print_line(make_list(line))
                has_tasks = True
                task_number += 1
                current_task_list.append(current_task)
        if has_tasks == False:
            print("Current user has no pending tasks.")

    # menu selection to edit tasks    
    while True: 
        # Keep prompting for input until valid choice is entered
        try:
            selection = int(input("Enter a task number to make changes" 
                                  + " or \"-1\" to exit: ")) 
        except selection < -1 or Exception:
            print("Invalid selection, please try again.")
        else:
            pass
        
        # If valid selection is made move into sub menu
        if (selection > 0 and 
        current_task_list[selection - 1][5] == "No"):
            # Create a list of all tasks to edit
            all_user_task_list = save_tasks() 
            # Used to make sure lines are written correctly
            written = False 

            with open("tasks.txt", "w") as file:
                # Selecting how to edit the file
                edit = input("""Enter 'e' To edit current task.
Enter 'c' to complete current task.
Enter selection: """).lower()
                if edit == 'e':
                    edit_what = input("""Enter 'u' to assign task to \
a different user.
Enter 'd' to change the due date.
Enter selection: """).lower()
                    
                    if edit_what != 'u' and edit_what != 'd':
                        print("Invalid selection!")
                        break
                    
                    # Used to match current user tasks to task file
                    counter = 0 
                    
                    # Loop through the stored list making any 
                    # necessary changes
                    for i in range(len(all_user_task_list)):
                        if all_user_task_list[i][0] == username:
                            counter += 1
                            
                            # Changing username
                            if (counter == selection and 
                                edit_what == 'u'):
                                change_user = input("Enter new user: ")
                                # Changing assigned user
                                if change_user in username_list: 
                                    all_user_task_list[i][0] = \
                                        change_user
                                else:
                                    print("User does not exist!")
                                    

                            # Change due date
                            elif (counter == selection and 
                                  edit_what == 'd'):
                                change_date = input("Enter new due date"
                                                     + 
                                                    "(YYYY-MM-DD): ")
                                all_user_task_list[i][4] = change_date

                        # Updating task list with changes        
                        if written == True:
                            file.write("\n")
                        # Writing new list to file
                        file.write(all_user_task_list[i][0] + ", " + 
                                   all_user_task_list[i][1] + ", " + 
                                   all_user_task_list[i][2] + ", " + 
                                   all_user_task_list[i][3] + ", " + 
                                   all_user_task_list[i][4] + ", " + 
                                   all_user_task_list[i][5])

                        written = True

                # Setting a task as complete
                elif edit == 'c':                                                              
                    counter = 0
                    for i in range(len(all_user_task_list)):
                        if all_user_task_list[i][0] == username:
                            counter += 1
                            if counter == selection:
                                all_user_task_list[i][5] = "Yes"
                        
                        if written == True:
                            file.write("\n")
                        # Writing new list to file
                        file.write(all_user_task_list[i][0] + ", " + 
                                   all_user_task_list[i][1] + ", " + 
                                   all_user_task_list[i][2] + ", " + 
                                   all_user_task_list[i][3] + ", " + 
                                   all_user_task_list[i][4] + ", " + 
                                   all_user_task_list[i][5])
                        written = True

        # Breaking the loop                
        elif selection == -1: 
            break 
        else:
            print("Invalid input!")
    

def populate_lists():
    """Generates username_list & password_list"""
    with open("./user.txt", "r") as login_db:
        # Adding to list line by line.
        for line in login_db: 
            # stripping \n
            line = line.strip() 
            # splitting terms into list items
            split_info = line.split(", ") 

            # Appending each lines info into respective lists
            username_list.append(split_info[0])
            password_list.append(split_info[1])


def print_line(line): 
    """
    Prints to screen formatted output of an input list of lists 
    containing task data.
    """

    print("_" * 70)
    print("Task:" + " " * 17 + line[1])
    print("Assigned to:" + " " * 10 + line[0])
    print("Date asigned:" + " " * 9 + line[3])
    print("Due date:" + " " * 13 + line[4])
    print("Task complete?" + " " * 8 + line[5])
    print("Task description:")
    print(" " + line[2])
    print("_" * 70 + "\n")


def print_reports(): 
    """Prints user and task reports from txt files"""
    with open("task_overview.txt", "r") as task_report:
        print_report = task_report.read()
        print(print_report)

    print("\n")

    with open("user_overview.txt", "r") as user_report:
        print_report = user_report.read()
        print(print_report)


def make_list(line): 
    """Making the list from txt input."""
    line = str(line)
    line = line.strip()
    line_list = line.split(", ")
    return line_list


def generate_task_overview(): 
    """Save task data in txt file, used for reports"""
    # Opening t_overview to write txt
    with open("task_overview.txt", "w") as t_overview:
        # variables for data tracking
        total_tasks = len(task_list) 
        total_complete = 0
        incomplete = 0
        overdue = 0
        # looping through tasks counting statuses
        for i in range(total_tasks): # Counting completed tasks
            if task_list[i][5] == "Yes":
                total_complete += 1
            else: # incomplete and overdue tasks are counted 
                incomplete += 1
                if (datetime.strptime(task_list[i][3],"%d %b %Y") > 
                datetime.strptime(task_list[i][4],"%d %b %Y")):
                    overdue += 1
        percent_incomplete = int(float((incomplete / total_tasks) * 100))
        percent_overdue = int(float((overdue / total_tasks) * 100))

        # Task Overview file is generated
        t_overview.write("Tasks Overview" + "\n" + "_" * 50 + "\n\n" +
                         "Total Number of Tasks: " + " " * 14 +
                         str(total_tasks) + "\n"
                         "Total Number of Completed Tasks: " + " " * 4 +
                         str(total_complete) + "\n" + 
                         "Total Number of Incomplete tasks: " + " " * 3 
                         + str(incomplete) + "\n" +
                         "Total Number of Tasks Overdue: " + " " * 6 +
                         str(overdue) + "\n" +
                         "Total Percentage Incomplete: " + " " * 8 +  
                         str(percent_incomplete) + "\n" +
                         "Total Percentage Overdue: " + " " * 11 +
                         str(percent_overdue) + "\n")


def generate_user_overview(): 
    """Save user data in txt file, used for reports"""
    with open("user_overview.txt", "w") as u_overview:
        total_users = len(user_list)
        total_tasks = len(task_list)
        # First line of doc contains these two numeric values
        u_overview.write("User Overview\n" + "_" * 50 + "\n")
        u_overview.write("Total Number of Users: " + 
                         str(total_users) + "\n" +
                         "Total Number of tasks: " + 
                         str(total_tasks) + 
                         "\n\n" + 
                         "User Task Data:" + "\n")
        
        # Creating list of lists (2D array) to store data for table 
        table_data = []
        # Loop through users (i)
        for i in range(total_users):
            # Create variables to store and calculate report data
            tasks_assigned = 0
            tasks_complete = 0
            overdue_tasks = 0
            
            # Count tasks and count how many complete and how 
            # many overdue.
            for j in range(total_tasks):
                if task_list[j][0] == user_list[i][0]:
                    tasks_assigned += 1 
                    if task_list[j][5] == "Yes":
                        tasks_complete += 1 
                    elif task_list[j][3] > task_list[j][4]:
                        overdue_tasks += 1
            
            # Do calculations for rest of user data. If / else 
            # structures to deal with incorrect reports when no 
            # tasks assigned
            percent_assigned = int(float((tasks_assigned / 
                                          total_tasks) * 100))
            if tasks_assigned > 0:
                percent_complete = int(float((tasks_complete / 
                                              tasks_assigned) * 100))
                percent_overdue = int(float((overdue_tasks / 
                                             tasks_assigned) * 100))
            else:
                percent_complete = 100
                percent_overdue = 0
               
            percent_incomplete = int(float(100 - percent_complete))
            # Writing to file line by line for each user
            
            table_data.append([user_list[i][0], 
                               tasks_assigned, 
                               percent_assigned,
                               percent_complete,
                               percent_incomplete,
                               percent_overdue])

        u_overview.write(tabulate(table_data, headers=["Username", 
                                                    "Tasks",
                                                    "% Assigned",
                                                    "% Complete",
                                                    "% Incomplete",
                                                    "% Overdue"]) +"\n")
               
        
"""End functions"""

#====Login Section====
# Setting the state of logged_in to false, 
# program will move on once logged in
logged_in = False

# Initialising lists to be used to store login info
username_list = []
password_list = []

# Reads and saves user data into lists
populate_lists() 

# Repeat login loop while credentials are incorrect or invalid
while logged_in == False:
    
    # save entered username and password into variables
    username = input("Enter Username (Case sensitive): ")
    password = input("Enter Password (Case sensitive): ")

    # loop through username list to check login credentials
    for i in range(len(username_list)):
        
        user_match = False
        pass_match = False

        user_check = username_list[i]
        pass_check = password_list[i]
        
        # If there is a match change state to true for username and 
        # password
        if username == user_check:
            user_match = True
        if password == pass_check:
            pass_match = True
        
        # check if login credentials are correct  and login if username 
        # and password match database
        if user_match is True and pass_match is True:
            logged_in = True
            print("Login successful!")

        # In this elif only the username will match, usernames should be 
        # unique so break out of loop so that loop stops running
        elif user_match is True:
            print("Incorrect Password")
            break

    # This will only print once the check loop is completed and login 
    # was not successful
    if logged_in == False and user_match == False:
        print("\nInvalid Credentials, user does not exist.\n")

# ========Menu items========
while True:
    # Updates lists with any new users that have been created
    populate_lists()    
    
    # Show menu and enter input as lowercase
    if username == "admin":
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
: ''').lower()
    else:
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
        
    # Create lists
    populate_lists()

    # Register a user
    if menu == 'r': 
        if username == "admin":
            reg_user()
        else: 
            print("You are not logged in as an administrator, " + 
                  "this option is disabled.")
        
    elif menu == 'a':
        # Request user to assign work to and check if user exists in 
        # user database
        assign_user = input("Enter user to assign task to: ")
        if assign_user in username_list:
            add_task(assign_user)
        # If the user does not exist an error message is displayed        
        else:
            print("""The user you are trying to assign work to does \
not exist. 
Please contact an admin.
""")
    # Prints all tasks
    elif menu == 'va': 
        view_all()
    # Prints current user's tasks
    elif menu == 'vm': 
        view_mine() 
    # count and display total number of tasks and users, Admin only
    elif menu == 'ds' and username == "admin": 
        # Generate reports if they dont already exist
        if os.path.exists("user_overview.txt") == False:
            generate_user_overview()
        if os.path.exists("task_overview.txt") == False:
            generate_task_overview()

        print_reports()
    
    # Generate reports
    elif menu == 'gr': 
        # Load into memory updated task list and user list
        user_list = save_users()
        task_list = save_tasks()
        
        # Call functions to generate txt files
        generate_task_overview()

        generate_user_overview()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")