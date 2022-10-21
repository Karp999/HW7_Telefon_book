import write_read
import logger
import csv

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
                surname = input("Введите фамилию, которую желаете изменить: ") 
                for i in range(len(record1)):
                    if surname in record1:
                        newSurname = input("Введите новую фамилию абонента: ")
                        a = (bookString.replace(surname, newSurname))
                        print("Фамилия абонента успешно изменена на:", newSurname)
                        file1.write(a)
                    else:
                        break
                logger.info_logger(f'Изменение записи: {newSurname}')
                return  
        case '2':
            with open('Phonebook_string.csv', 'r+', encoding='utf-8', newline='') as file1:
                bookString = write_read.read_file_string()
                record1 = bookString.split()
                description = input("Введите имя, которое желаете изменить: ") 
                for i in range(len(record1)):
                    if description in record1[i]:
                        newName = input("Введите новое имя абонента: ")
                        b = (bookString.replace(record1[i], newName))
                        print("Имя абонента успешно изменено на:", newName)
                        file1.write(b)
                    else:
                        break
                logger.info_logger(f'Изменение записи: {newName}')
                return 
        case '3': 
            with open('Phonebook_string.csv', 'r+', encoding='utf-8', newline='') as file1:
                bookString = write_read.read_file_string()
                record1 = bookString.split()
                description = input("Введите номер, который желаете изменить: ") 
                for i in range(len(record1)):
                    if description in record1[i]:
                        newNumber = input("Введите новый номер абонента: ")
                        b = (bookString.replace(record1[i], newNumber))
                        print("Номер абонента успешно изменено на:", newNumber)
                        file1.write(b)
                    else:
                        break
                logger.info_logger(f'Изменение записи: {newNumber}')
                return 
        case '4':
            with open('Phonebook_string.csv', 'r+', encoding='utf-8', newline='') as file1:
                bookString = write_read.read_file_string()
                record1 = bookString.split()
                description = input("Введите старое описание абонента: ") 
                for i in range(len(record1)):
                    if description in record1[i]:
                        newDescription = input("Введите новое описание абонента: ")
                        b = (bookString.replace(record1[i], newDescription))
                        print("Описание абонента успешно изменено на:", newDescription)
                        file1.write(b)
                    else:
                        break
                logger.info_logger(f'Изменение записи: {newDescription}')
                return 
        case '0':
            return