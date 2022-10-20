import logging

def change():
    surname = 0 
    name = 1  
    phone_number = 2   
    description = 3  
    err = " "

    file = write_read_delete_change.read_file_string()
    new_file = file.split()
    for i in range(len(new_file)):
        if new_file[i][surname]== search(surname) and new_file[i][name]==search[name] and new_file[i][phone_number]==search[phone_number] and new_file[i][description]==search[description]:
            if search[surname] != err:
                new_file[i][surname] = write_file_string(surname)
            if search[name] != err:
                new_file[i][name] = write_file_string(surname)
            if search[phone_number] != err:
                new_file[i][phone_number] = write_file_string(surname)
            if search[description] != err:
                new_file[i][description] = write_file_string(surname)
        return new_file
