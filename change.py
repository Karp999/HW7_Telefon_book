from unicodedata import name
from HW7_Telefon_book.search import search
import write_read_delete_change

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

