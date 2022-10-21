from datetime import datetime as dt

def info_logger(info):
    time = dt.now().strftime('%D_%H:%M')
    with open ('phonebook_log.csv', 'a', encoding="utf-8") as file:
        file.write('{};phonebook;{}\n'
                    .format(time, info))

