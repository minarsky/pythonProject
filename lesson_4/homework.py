# chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
# id = [5, 0, 1, 0, 3, 1, 4, 3, 7, 5, 6]
# print((1 * 5 + 1 * 3 + 5 * 3 + 6 * 1 + 7 * 4 + 8 * 3 + 9 * 7 + 1 * 5)% 11)

id_code = input("Please enter your ID: ")
# if len(id_code) == 11:
#     print("Your ID code is: ", id_code)
# elif len(id_code) > 11 or len(id_code) < 11:
#     print("Wrong ID")
#
# id = id_code
#
#
# if int(id[0] * chk1[0] + id[1] * chk1[1] + id[2] * chk1[2] + id[3] * chk1[3] + id[4] * chk1[4] + id[5] * chk1[5] +
#     id[6] * chk1[6] + id[7] * chk1[7] + id[8] * chk1[8] + id[9] * chk1[9])% 11 == int(id[10]):
#     print("Your ID code is valid")
# elif int(id[0] * chk2[0] + id[1] * chk2[1] + id[2] * chk2[2] + id[3] * chk2[3] + id[4] * chk2[4] + id[5] * chk2[5] +
#     id[6] * chk2[6] + id[7] * chk2[7] + id[8] * chk2[8] + id[9] * chk2[9])% 11 == int(id[10]):
#     print("Your ID code is valid")
# else:
#     print("Your code is invalid")

id_code = input("Please enter your ID: ")
chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

cnt = 0
result = 0
for num in chk1:
    result += num * int(id_code[cnt])
    cnt += 1
check_num = result % 11

if int(id_code[-1]) == check_num:
    print(f"Your ID is {id_code}")
    print("ID is valid")
elif check_num == 10:
    cnt = 0
    result = 0
    for num in chk2:
        result += num * int(id_code[cnt])
        cnt += 1
    check_num = result % 11
    if int(id_code[-1]) == check_num:
        print(f"Your ID is {id_code}")
        print("ID is valid")
    else:
        print("Your ID is invalid")
else:
    print("Your ID is invalid")