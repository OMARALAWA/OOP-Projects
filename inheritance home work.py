class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

class Project:
    def __init__(self, name, description, days_required, is_completed):
        self.name = name
        self.description = description
        self.days_required = days_required
        self.is_completed = is_completed

class Programmer(Employee):
    def __init__(self, first_name, last_name, salary, lang, projects):
        super().__init__(first_name, last_name, salary)
        self.lang = lang
        self.projects = projects

    def print_projects(self):
        for project in self.projects:
            print(f"Project Name: {project.name}")
            print(f"Description: {project.description}")
            print(f"Days Required: {project.days_required}")
            print(f"Completed: {project.is_completed}")
            print("-" * 20)

# مثال على الاستخدام
project1 = Project("Website Development", "Developing a company website", 30, False)
project2 = Project("App Development", "Creating a mobile application", 45, True)

programmer = Programmer("Ali", "Khalid", 8000, "Python", [project1, project2])
programmer.print_projects()
