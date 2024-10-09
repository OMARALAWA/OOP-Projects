class Employee:
    total = 0
    salary_raise = 1.5

    def __init__(self, first_name, last_name, title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.salary = salary
        Employee.total += 1

    def info(self):
        return f'Name: {self.first_name} {self.last_name}, Jop title : {self.title}'

    @classmethod
    def change_raise(cls, amount):
        cls.salary_raise = amount

    @classmethod
    def from_string(cls, string):
        first_name, last_name, title, salary = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, title, salary)



# في التطبيق التالي قمنا بأستخدام الداله total التي تم ادراجها في الأعلى
print(Employee.total)
omar = Employee('Omar', 'Alawa', 'IT', 3000)
print(Employee.total)
# نقوم هذه الدالة بالتعرف على عدد الكائنات المدرجة تحت Employee

print('==========')

# في التطبيق التالي قمنا بأستخدام الدالة change raise
print(Employee.salary_raise)
Employee.change_raise(2.0)
print(Employee.salary_raise)
# نقوم في هذه الدالة بتغيير نسبة الزيادة بأستخدام classmethod@

print('==========')

# في الطبيق التالي قمنا باستخدام دالة from_string
ahmed = Employee.from_string('Ahmed-Kamal-Accountant-3000')
print(ahmed.info())
print(omar.info())
# قمنا بتعريف الموظف بإستخدم - بدلا نم '' , باأستخدام classmethod@

print('==========')

# del ahmed ==> لحذف الكائن من الذاكرة الجهاز
# print(ahmed) ==> سوف يظهر خطأ في التشغيل