import os
# print("Hello, World!!")

grade = [32, 76, 35, 76, 90]
result = sum(grade)/len(grade)
# print(grade)
grade.append(108)
# print(grade[1])

tuple_grade = (32, 76, 35, 76, 90)    #immutable
tuple_grade = tuple_grade + (100,)
# print(tuple_grade)

set_grade = {32, 76, 35, 79}
# print(set_grade)

set_one = {2, 4, 5, 9}
set_two = {2, 4, 8, 10, 12}
# print(set_one.union(set_two))

my_var ="hello, world!"
for char in my_var:
    print(char)

