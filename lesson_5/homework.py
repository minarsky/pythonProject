id_code = input("Please enter your ID: ")
# 131052-308T
bd_num = id_code[0:2]
bm_num = id_code[2:4]
by_num = id_code[4:6]
gender = id_code[7:10]
if id_code[6] == "+":
    by_century = "18"
elif id_code[6] == "-":
    by_century = "19"
elif id_code[6] == "A":
    by_century = "20"
if int(gender) % 2 == 0:
    gender_id = "Female"
else:
    gender_id = "Male"
if int(gender) in range(2, 900):
    birth_place = "Finland"
elif int(gender) in range(900, 1000):
    birth_place = "Wasn`t born if Finland"
print(f"ID: {id_code}.")
print(f"Gender: {gender_id}")
print(f"Birth date: {bd_num}.{bm_num}.{by_century}{by_num}")
print(f"Birth place: {birth_place}")