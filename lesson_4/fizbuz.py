"""
В числовом диопозоне от 0 до 100
    если число делится на 3 без остатка, написать число + Fizz
    если число делится на 5 без остатка, написать число + Buzz
    если число делится на 3 и на 5 без остатка, написать число + FizzBuzz

"""
def fizz_buzz(start_num, end_num):
    for num in range(start_num, end_num):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{num}, FizzBuzz")
        elif num % 5 == 0:
            print(f"{num}, Buzz")
        elif num % 3 == 0:
            print(f"{num}, Fizz")
fizz_buzz(50, 1001)
# x = 50
# if x == 50:
#     print("x is 50")
# elif x == 10:
#     print("X is 10")
# elif x > 100:
#     print("X is greater than 100")
# elif x <= 100:
#     print("X is smaller than 100")