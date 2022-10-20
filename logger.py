import logging

def logger(log):
    with open ("log.txt", "a+", encording = "utf-8") as file:
        file.write(log + "\n")
        return