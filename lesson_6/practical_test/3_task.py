a, b, c = input("please enter triangle sides: ").split()
if float(c) ** 2 == float(a) ** 2 + float(b) ** 2:
    print("Triangle is rectangular")
else:
    print("Triangle is not rectangular")
