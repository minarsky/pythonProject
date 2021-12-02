courses = ["Math", "Physycs", "History", "Programming", "Literature", "Math"]
number = [4, 5, 23, 1, 9, 84]

set1 = set()
set2 = {}
print(type(set1))
print(type(set2))

set3 = {1, 4, 2, 5, 5, 5, 5, 5,}
print(set) #нет индекса и порядка и если courses то каждый раз хаотично

print(tuple(set(courses)))

set4 = {"Art", "English", "Biology", "Physycs"}

set5 = {"Programming", "Biology", "Art", "Math"}

print(set4.intersection(set5)) #находит сходства
print(set4.difference(set5)) #находит отличия

print(set4.union(set5)) #сложение без дубликатов и не меняет переменную
set4.add("Russian")
print(set4)

set4.clear() #отчистить
print(set4)

set4.update(set5) #как union меняет переменную
print(set4)