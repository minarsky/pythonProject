user_name = input("name: ")

user_surname = input("surname: ")

a = int(input("current_year: "))
b = int(input("year_of_birth: "))

current_age = a - b

x = 152
y = 132

code_2 = int((x % y * 13) ** 0.5)
code_1 = "354"
code_3 = 132
secret_code = code_1 + "-" + str(code_2) + "-" + str(code_3)
print(secret_code)
print("Hello " + user_name + " " + user_surname + ". " + "You are" + " " + str(current_age) + " " + "years old. Your secret code is" + " " + secret_code + ".")


print(f"hello {user_name} {user_surname}. You are {current_age} years old. Your secret code is {secret_code}")as