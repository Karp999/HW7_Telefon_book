import search
import write_read_delete_change


def menu():
    m = input('''Поиск контакта: введите 1.
             \nРедактировать контакт: введите 2.
             \nУдалить контакт: введите 3. 
             \nСоздать новую запись, сохранить в строку: введите 4. 
             \nСоздать новую запись, сохранить в столбец: введите 5. 
             \nВыход: введите 0.\n''')

    match m:
        case '1':
            return search.search()
        case '2':
            return change.change()
        case '3': 
            return delete_change.delete() #не удаляет у меня
        case '4':
            return write_read_delete_change.write_file_string()
        case '5':
            return write_read_delete_change.write_file_column()

menu()