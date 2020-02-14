num_int = 5
num_float = 3.33
str_var = 'строка'
bool_var = (2*2 == 4)
obj_list = [num_int, num_float, str_var, bool_var]
obj_tuple = tuple(obj_list)
obj_dict = {num_int: bool_var, str_var: obj_list}
print(num_int, num_float, str_var, bool_var)
print(obj_tuple, obj_dict, sep=' // ')

num_int = int(input('Введите целое число: '))
num_float = float(input('Введите вещественное число: '))
str_var = input('Напечатайте текст: ')
print(num_int, str_var, num_float)
