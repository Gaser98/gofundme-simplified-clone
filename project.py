import datetime

class Project:
    projects = []

    def __init__(self, title, details, target, start_time, end_time, user):
        self.title = title
        self.details = details
        self.target = target
        self.start_time = start_time
        self.end_time = end_time
        self.user = user
        Project.projects.append(self)

    def edit_project(self, title, details, target, start_time, end_time):
        self.title = title
        self.details = details
        self.target = target
        self.start_time = start_time
        self.end_time = end_time

    def delete_project(self):
        Project.projects.remove
