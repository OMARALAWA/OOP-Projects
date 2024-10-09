class Employee:
    def __init__(self, first_name, last_name, title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.salary = salary

    def info(self):
        return f'Name: {self.first_name} {self.last_name}, Jop title : {self.title}'

    def change_salary(self, addition):
        self.salary = self.salary + addition
        return self.salary

ahmed = Employee('Ahmed', 'Kareem', 'programming', 3000)
omar = Employee('Omar', 'Alawa', 'Information technology', 5500)

print(omar.info())
print(omar.salary)
print(ahmed.last_name)
print(ahmed.info())

omar.change_salary(500)
print(omar.salary)


print('==========')


# del ahmed ==> لحذف الكائن من الذاكرة الجهاز
# print(ahmed) ==> سوف يظهر خطأ في التشغيل