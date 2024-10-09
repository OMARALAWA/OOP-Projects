def increase(x):
    return x + 1

def decrease(x):
    return x - 1

def calculate(operation, x):
    return operation(x)

print(calculate(increase,5))
print(calculate(decrease,4))
# بالإمكان تمرير الدالة كمعامل لدلة أخرى

def parent():
    print("This is the parent function")
    def child1():
        print("This is child 1 function")
    def child2():
        print("This is child 2 function")

    child1()
    child2()
parent()
# تم انشاء دالتين داخل دالة الأب في المثال / بالإمكان تعرف دالة داخل دالة أخرى

def vote(age):
    def allow():
        print("You are allowed to vote")
    def not_allowed():
        print("You are not allowed to vote")
# مررنا كالعادة دالتين داخل الدالة الأب
    if age > 18:
        return allow
    else:
        return not_allowed
# ادخلنا شرط داخل الدوال
person1 = vote(22)
person2 = vote(15)
# اسندنا person1 + person 2 الى vote
person1()
person2()



