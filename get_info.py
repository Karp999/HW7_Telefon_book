import logger

def get_info ():
    info = []
    surname = logger.input('Введите фамилию: ')
    info.append(surname)
    name = logger.input('Введите имя: ')
    info.append(name)
    phone_number = logger.input('Введите номер телефона: ')
    info.append(phone_number)
    description = logger.input('Введите описание: ')
    info.append(description)
    return info