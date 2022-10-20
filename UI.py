import search
import write_read
import delete_change

def menu():
    m = input('''Поиск контакта в телефонной книге 1: введите 1.
             \nПоиск контакта в телефонной книге 2: введите 2
             \nРедактировать контакт: введите 3.
             \nУдалить контакт: введите 4. 
             \nСоздать новую запись, сохранить в телефонной книге 1 (строка): введите 5. 
             \nСоздать новую запись, сохранить в в телефонной книге 2 (столбец): введите 6. 
             \nВыход: введите 0.\n''')

    match m:
        case '1':
            return search.search_string()
        case '2':
            return search.search_column()
        case '3':
            return
        case '4':
            return delete_change.delete()    
        case '5':
            return write_read.write_file_string()
        case '6':
            return write_read.write_file_column()
        case '0':
            return