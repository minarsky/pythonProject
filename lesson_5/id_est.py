# for letter in "Python":
#
#     if letter == "h":
#         print("found it")
#         continue
#     print(f"current letter - {letter}")
while True:
    try:
        user_input = input("Please enter ID code: ")
        int(user_input)
        if len(user_input) != 11:
            raise UserWarning
    except ValueError:
        print("Your code is not numeric.")
        continue
    except UserWarning:

        if len(user_input) > 11:
            print("Your code is too long")
        elif len(user_input) < 11:
            print("Your code is too short")
        continue
    else:
        break

condition = True
while condition:
    user_choice = input("Please choose:\n1.Get data from ID\n2.Validate\n0.Exit\n->")
    if user_choice == "1":
        gender_num = user_input[0]
        by_num = user_input[1:3]
        bm_num = user_input[3:5]
        bd_num = user_input[5:7]
        birth_region = user_input[7:10]
        check_num = user_input[10]

        #Get gender of ID owner
        if int(gender_num) % 2 == 0:
            gender_id = "Female"
        else:
            gender_id = "Male"
        #Get year of birth first characters
        if gender_num == "1" or gender_num == "2":
            by_id = "18"
        elif gender_num == "3" or gender_num == "4":
            by_id = "19"
        elif gender_num == "5" or gender_num == "6":
            by_id = "20"
        elif gender_num == "7" or gender_num == "8":
            by_id = "21"

         #Get
        if int(birth_region) in range(1, 11):
            region = "Kuressaare haigla"
        elif int(birth_region) in range(11, 20):
            region = "Tartu Ülikooli Naistekliinik"
        elif int(birth_region) in range(21, 151):
            region = "Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)"
        elif int(birth_region) in range(151, 161):
            region = "Keila haigla"
        elif int(birth_region) in range(161, 221):
            region = "Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)"
        elif int(birth_region) in range(211, 271):
            region = "Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)"
        elif int(birth_region) in range(271, 370):
            region = "Maarjamõisa kliinikum (Tartu), Jõgeva haigla"
        elif int(birth_region) in range(371, 421):
            region = "Narva haigla"
        elif int(birth_region) in range(421, 471):
            region = "Pärnu haigla"
        elif int(birth_region) in range(471, 491):
            region = "Haapsalu haigla"
        elif int(birth_region) in range(491, 521):
            region = "Järvamaa haigla (Paide)"
        elif int(birth_region) in range(521, 571):
            region = "Rakvere haigla, Tapa haigla"
        elif int(birth_region) in range(571, 601):
            region = "Valga haigla"
        elif int(birth_region) in range(601, 651):
            region = "Viljandi haigla"
        elif int(birth_region) in range(651, 701):
            region = "Lõuna-Eesti haigla (Võru), Põlva haigla"
        print(f"ID: {user_input}")
        print(f"Gender: {gender_id}")
        print(f"Date of Birth: {bd_num}.{bm_num}.{by_id + by_num}")
        print(f"Region: {region}")
        print(f"Check num: {check_num}")
    elif user_choice == "2":
        id_code = user_input
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
    elif user_choice == "0":
        break
    else:
        print("Choise is out of range")
# """"""
# ID: 38803160272
# Gender: Male
# Date of Birth: 16.03.1988
# Region: Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)
# Check num : 2
# """"""
