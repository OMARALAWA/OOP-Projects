# إنشاء القائمة الأولى من الأرقام
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# إنشاء القائمة الجديدة التي تحتوي على مربعات الأرقام في القائمة الأولى
squared_list = [x**2 for x in original_list]

# طباعة القائمتين
print("Original list:", original_list)
print("Squared list:", squared_list)
