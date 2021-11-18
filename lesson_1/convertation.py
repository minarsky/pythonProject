int_var = 500
float_var = 50.9
string_var_text = "Hello world"
string_var_num = "123.2"
bool_var= True

#int() - integer
#float() - float
#str() - string
#bool() - boolean

print(type(int_var))
int_var = str(int_var)
print(type(int_var))

print(string_var_text + int_var)
print(type(int_var))
print(string_var_text + str(float_var))
print(string_var_text + str(bool_var))

print(int_var)
print(float(int_var))

print(int(float_var))

print(type(int(float(string_var_num))))
print(int(float(string_var_num)))


print(bool(string_var_text))

#Alternative
print(string_var_text, int_var, True, None, 100000.2123)
print(float_var + float(string_var_num))
print(str(float_var) + string_var_num)