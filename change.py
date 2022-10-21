import write_read
import logger
import re


def askAboutChanging(): 
    questionC = input('''Что вы хотите изменить?
            \nВведите 1 для замены фамилии:
            \nВведите 2 для замены имени:
            \nВведите 3 для замены номера телефона: 
            \nВведите 4 для замены описания контакта: 
            \nДля выхода введите 0: .\n''')

    match questionC:
        case '1':
            with open('Phonebook_string.csv', 'r+', encoding='utf-8', newline='') as file1:
                bookString = write_read.read_file_string()
                record1 = bookString.split()
                for i in range(len(record1)):
                    surname = input("Введите фамилию: ") 
                    print(record1)
                    if surname == record1[i]:
                        index = record1.index(surname)
                        print(index)
                        newSurname = input("Введите новую фамилию абонента: ")
                        a = (bookString.replace(record1[index], newSurname))
                        print(a)
                        print("Фамилия абонента успешно изменена на:", newSurname)
                        result = pattern.search(i)
                        if result is None:
                            file1.write(i)

                
         








                    # return
                    # #     record[i][surname] = write_read(surname)     
                return 
        # case '2':
        #     name = input("Введите имя: ") 
        #     file = write_read.read_file_string()
        #     record = file.split()
        #     for i in range(len(record)):
        #     if surname == record[i] and name == record[i] and phone_number == record[i] and description == record[i]:
        #     if search[surname] != err:
        #         record[i][surname] = write_file_string(surname)
        #     if search[name] != err:
        #         record[i][name] = write_file_string(surname)
        #     if search[phone_number] != err:
        #         record[i][phone_number] = write_file_string(surname)
        #     if search[description] != err:
        #         record[i][description] = write_file_string(surname)        
        #     return change (name)
        # case '3': 
        #     phone_number = input("Введите номер телефона: ") 
        #     file = write_read.read_file_string()
        #     record = file.split()
        #     for i in range(len(record)):
        #     if surname == record[i] and name == record[i] and phone_number == record[i] and description == record[i]:
        #     if search[surname] != err:
        #         record[i][surname] = write_file_string(surname)
        #     if search[name] != err:
        #         record[i][name] = write_file_string(surname)
        #     if search[phone_number] != err:
        #         record[i][phone_number] = write_file_string(surname)
        #     if search[description] != err:
        #         record[i][description] = write_file_string(surname)        
        #     return change (phone_number) 
        # case '4':
        #     description = input("Введите описание контакта: ") 
        #     file = write_read.read_file_string()
        #     record = file.split()
        #     for i in range(len(record)):
        #     if surname == record[i] and name == record[i] and phone_number == record[i] and description == record[i]:
        #     if search[surname] != err:
        #         record[i][surname] = write_file_string(surname)
        #     if search[name] != err:
        #         record[i][name] = write_file_string(surname)
        #     if search[phone_number] != err:
        #         record[i][phone_number] = write_file_string(surname)
        #     if search[description] != err:
        #         record[i][description] = write_file_string(surname)        
        #     return change (description)
        # case '0':
            return

               # logger.info_logger(f'Удаление записи: {pattern}')

# def change(record):
    
#         if surname == record[i] and name == record[i] and phone_number == record[i] and description == record[i]:
#             if search[surname] != err:
#                 record[i][surname] = write_file_string(surname)
#             if search[name] != err:
#                 record[i][name] = write_file_string(surname)
#             if search[phone_number] != err:
#                 record[i][phone_number] = write_file_string(surname)
#             if search[description] != err:
#                 record[i][description] = write_file_string(surname)
#         return record

# # запись изменений
# def writer_too(phone_numbers):
#     with open('names.csv', 'w', encoding='utf-8', newline='') as csvfile:
#         fieldnames = ['first_name', 'contact info']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         for key in phone_numbers.keys():
#             writer.writerow({'first_name': key, 'contact info': phone_numbers[key]})