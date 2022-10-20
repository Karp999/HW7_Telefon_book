import write_read_delete_change

def askAboutChanging(): 
    questionC = input(''' Что вы хотите изменить?
            \nВведите 1 для замены фамилии:
            \nВведите 2 для замены имени:
            \nВведите 3 для замены номера телефона: 
            \nВведите 4 для замены описания контакта: 
            \nДля выхода введите 0: .\n''')

    match questionC:
        case '1':
            return change(surname)
        case '2':
            return change (name)
        case '3': 
            return change (phone_number) 
        case '4':
            return change (description)

def change():
    
    surname = input("Введите фамилию: ") 
    name = input("Введите имя: ")   
    phone_number = input("Введите номер телефона: ")    
    description = input("Введите описание контакта: ")    
    
    file = write_read_delete_change.read_file_string()
    new_file = file.split()
    for i in range(len(new_file)):
        if surname == new_file[i] and name == new_file[i] and phone_number == new_file[i] and description == new_file[i]:
            if search[surname] != err:
                new_file[i][surname] = write_file_string(surname)
            if search[name] != err:
                new_file[i][name] = write_file_string(surname)
            if search[phone_number] != err:
                new_file[i][phone_number] = write_file_string(surname)
            if search[description] != err:
                new_file[i][description] = write_file_string(surname)
        return new_file
