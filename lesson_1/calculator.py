a = float(input("side A: "))
b = float(input("side B: "))
c = float(input("side C: "))

half_p = (a + b + c) / 2


area = (half_p * (half_p - a) * (half_p - b) * (half_p - c)) ** 0.5
print(area)
