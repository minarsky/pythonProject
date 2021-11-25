string_sample1 = "Hello world world world world"
string_sample2 = "first letteRis lowERcase"
string_sample3 = " extral whjitespace string eee "
string_sample4 = "der Fluß"
simple_string = "hello"


print(len(string_sample1))
print(len("12312312231"))
# [start_index:stop_index:step]
print(string_sample1[1:12:2])
print(string_sample1[6:11])
sliced_string = string_sample1[6:11]
print(sliced_string)
print("hello world"[2:10])

print("World" in string_sample1)
print(string_sample1.upper())
print(string_sample4.lower())
print(string_sample4.casefold())
#обрезает по краям (rstrip справа lstrip слева)
print(string_sample3.strip(" e"))
print(string_sample3.lstrip().rstrip())

print(string_sample1.replace("world", "planet"))
print(string_sample1.replace(" ", "*", 2))
print(string_sample1.replace(" ", "*", 2).replace("w","9"))


print(string_sample1.count("o", 5, 10))
#rfind с конца строки
print(string_sample1.find("world"))

a = "hello"
b = "world"

print(a + " " + b)

salary = 1000
text = "johns salary is {2}, {0}, {1}"
print(text.format(salary, True, 213.32))

price_string = "this {product:} costs {price:} eur"
print(price_string.format(product="computer", price=1000))
 