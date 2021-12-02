courses = ["Math", "Physycs", "History", "Programming", "Literature"]
number = [4, 5, 23, 1, 9, 84]
print(courses)


#courses[0] = "Biology"
#print(courses)


#courses[0:3] = "Biology", "Art", "Russian"


#courses.append("Art")
#print(courses)

#courses.insert(0,"art")
#print(courses)

#courses2 = ["Art", "English"]
#courses.extend(courses2)
#print(courses)

a = courses.remove("Math")
b = courses.pop(0) #если пусто то последний элемент
print(a)
print(b)
print(courses)
courses.reverse()
print(courses)
print(list(reversed(courses)))

number.sort() #сортирует в алфавитном порядке
#courses.sort(reverse=True) #в обратном порядке
print(number)

print(min(number))
print(max(courses)) #тоже по алфавиту
print(sum(number))
print(courses.index("History"))
print("Math" in courses) #проверка на наличие

sample = "hello world"
print(list(sample))
courses_str = "***".join(courses)
print(str(courses))
print(courses_str)

print(sample.split(" "))

courses2 = courses.copy()
courses2[0] = "Art"
courses[1] = "english"
print(courses)
print(courses2)