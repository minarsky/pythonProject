x = 5
sample_set = ["one", "two", "three"]
student = {"name": "John", "age": "30", "courses": ["Math", "Biology", "Art"], "none_type": None, "none_type2": None, 1:"int_key", 0.2: "float_key", x: "variable", "var_key": x}
#True - 1 False - 0

print(student.get("job"))
print(student.get("courses")[1])

print(student["courses"].append("Hello world"))
print(student["courses"])

print(student.get("job", [1, 2, 3]))

#student["age"] = 25
print(student)
#student["phone"] = "5555-5555-55"
print(student)

student.update({"name": "Jack", "age": 25, "phone": "555-55"})
print(student)

print(student)
age = student.pop("age")
print(student)
print(age)

print(student.keys())
print(student.values())
print(list(student.items()))