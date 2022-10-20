import logging

def logger(dt, log):
    with open ("log.txt", "a", encording = "utf-8") as file:
        file.write(log + "\n")
        return