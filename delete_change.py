import write_read_delete_change

def delete():
    with open ('Phonebook_string.csv', 'r', encoding='utf-8', newline='') as file, open  ('Phonebook_column.csv', 'r', encoding='utf-8', newline='') as file2:
        lst = file.readlines()
        lst2 = file2.readlines()
        surname = input('Введите фамилию: ')
        pattern = re.compile(re.escape(surname))
        with open('Phonebook_string.csv', 'w', encoding='utf-8', newline='') as f:
            for i in lst:
                result = pattern.search(i)
                if result is None:
                    f.write(i)

def change():
    surname = 0 
    name = 1  
    phone_number = 2   
    description = 3  
    err = " "

    file = write_read_delete_change.read_file_string()
    new_file = file.split()
    for i in range(len(new_file)):
        
        if new_file[i][surname]==search[surname] and new_file[i][name]==search[name] and new_file[i][phone_number]==search[phone_number] and new_file[i][description]==search[description]:
            if update_data[surname] != err:
                new_file[i][surname] = update_data[surname]
            if update_data[name] != err:
                new_file[i][name] = update_data[name]
            if update_data[phone_number] != err:
                new_file[i][phone_number] = update_data[phone_number]
            if update_data[description] != err:
                new_file[i][description] = update_data[description]
            

                    
# def search():
#     surname = input('Введите фамилию: ')
#     file = write_read_delete_change.read_file_string()
#     new_file = file.split()
#     print(new_file)
#     if surname in file:
#         for i in range(len(new_file)):
#             if surname == new_file[i]:
#                 print("yes")
#                 #del new_file[i]
#                 # del new_file[i+1]
#                 # del new_file[i+2]
#                 # del new_file[i+3]
#     else:
#        print('Контакт не найден') 



"""
def del_request(value: list):
    """
    Создает диалог с пользователем, для удаления
    выбранной записи 
    :param value: список переменных (фамилия, имя, телефон, комментарий)
    :return: OK_RETURN/ERROR_RETURN
    """
    request_list = dr.request_list(di.load_data_phone(),value)
    if len(request_list) == 0:
        vd.print_message('НИЧЕГО НЕ НАЙДЕНО')
        return di.OK_RETURN
    else:
        vd.print_data(request_list)
    while True:
        del_number = int(input('Введите номер записи которую нужно удалить: '))
        if 1<=del_number<=len(request_list):
            return dr.del_data(di.load_data_phone(),request_list[del_number-1])
        else:
            vd.print_inp_err()

"""


# import search
# import write_read_delete_change

# def delete():
#     del_record = search.search()
#     new_del_record = list.append(del_record)
#     print(type(new_del_record))
#     file = write_read_delete_change.read_file_string()
#     new_file = file.split()
#     for i in range(len(new_file)):
#         if new_del_record[0] == new_file[i]:
#                 #print(new_file [i], new_file[i+1], new_file[i+2], new_file[i+3])
#             print("hd")
#         else:
#             print("f")   
        
#         # for i in range(len(new_file)):
#         #     if surname == new_file[i]:
#         #         print(new_file [i], new_file[i+1], new_file[i+2], new_file[i+3])
# #delete()    
    
    