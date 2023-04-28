from auth import User
from project import Project
import datetime

# Function to prompt user for a valid date and return it as a datetime object
def get_date(prompt):
    while True:
        date_str = input(prompt + " (format: DD/MM/YYYY HH:MM): ")
        try:
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y %H:%M")
            return date
        except ValueError:
            print("Invalid date format.")

# Prompt user for registration or login
while True:
    print("1. Register")
    print("2. Login")
    choice = input("Enter choice: ")

    if choice == "1":
        User.register()
        user = User.users[-1]  # Get last registered user
        break
    elif choice == "2":
        user = User.login()
        break
    else:
        print("Invalid choice.")

# Prompt user for project options
while True:
    print("1. Create project")
    print("2. View all projects")
    print("3. Edit project")
    print("4. Delete project")
    print("5. Logout")
    choice = input("Enter choice: ")

    if choice == "1":
        # Prompt user for project details
        title = input("Enter project title: ")
        details = input("Enter project details: ")
        target = input("Enter project target amount: ")
        start_time = get_date("Enter project start time")
        end_time = get_date("Enter project end time")

        # Create new project
        project = Project(title, details, target, start_time, end_time, user)
        print("Project created.")
    elif choice == "2":
        # Print all projects
        for project in Project.projects:
            print("Title: " + project.title)
            print("Details: " + project.details)
            print("Target: " + str(project.target))
            print("Start time: " + str(project.start_time))
            print("End time: " + str(project.end_time))
            print("User: " + project.user.first_name + " " + project.user.last_name)
            print()
    elif choice == "3":
        # Prompt user for project to edit
        title = input("Enter project title: ")
        for project in Project.projects:
            if project.title == title and project.user == user:
                # Prompt user for new project details
                new_title = input("Enter new project title: ")
                new_details = input("Enter new project details: ")
                new_target = input("Enter new project target amount: ")
                new_start_time = get_date("Enter new project start time")
                new_end_time = get_date("Enter new project end time")

                # Edit project
                project.edit_project(new_title, new_details, new_target, new_start_time, new_end_time)
                print("Project edited.")
                break
        else:
            print("Project not found or you do not have permission to edit it.")
    elif choice == "4":
        # Prompt user for project to delete
        title = input("Enter project title: ")
        for project in Project.projects:
            if project.title == title and project.user == user:
                # Delete project
                project.delete_project()
                print("Project deleted.")
                break
        else:
            print("Project not found or you do not have permission to delete it.")
    elif choice == "5":
        break

        
