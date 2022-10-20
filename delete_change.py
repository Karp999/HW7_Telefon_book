import write_read_delete_change

def search():
    surname = input('Введите фамилию: ')
    file = write_read_delete_change.read_file_string()
    new_file = file.split()
    print(new_file)
    if surname in file:
        for i in range(len(new_file)):
            if surname == new_file[i]:
                print("yes")
                #del new_file[i]
                # del new_file[i+1]
                # del new_file[i+2]
                # del new_file[i+3]
    else:
       print('Контакт не найден') 



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
    
    