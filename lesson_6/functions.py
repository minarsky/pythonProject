def squares(number):
    result = number ** 2
    return result

def no_argument():
    number = 25 ** 0.5
    return number

def sqrt(number):
    return number ** 0.5

def print_message(name, age, profession):
    return print(f"Hi my name is {name}, I am {age} years old. I work as a {profession}")

# emp_list = [("Jack Smith", 25, "Programmer"), ("Mary Gold", 18, "Teacher"), ("Bob Summers", 30, "Builder" )]
#
# for employee in emp_list:
#     print_message(employee[0], employee[1], employee[2])
#
# for x, y, z in emp_list:
#     print_message(x, y, z)

# y = 200
# result = squares(y)
# result2 = no_argument()
# print(result)
# print(result2)

user_name, user_age, user_profession = input("enter name, age, profession: ").split(", ")
print_message(user_name, user_age, user_profession)