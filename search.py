import write_read_delete_change
import logger

def search():
    surname = logger.input('Введите фамилию: ')
    file = write_read_delete_change.read_file_string()
    new_file = file.split()
    if surname in file:
        for i in range(len(new_file)):
            if surname == new_file[i]:
                logger.print(new_file [i], new_file[i+1], new_file[i+2], new_file[i+3])
    else:
       logger.print('Контакт не найден') 

