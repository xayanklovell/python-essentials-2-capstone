import os 
import random

def generate_data_file():
    os.makedirs("data", exist_ok=True)

    names = [
        "  lIsA nDlOvU  ",
        " tHaBo mOkOeNa ",
        "  aMINA pATEL ",
        " SIPHO dlamini  ",
        "  nAlEdI KHUMALO ",
        "jOhAn bOtHa  ",
        "  ZINHLE zulu ",
        " kabelo MOLEFE  ",
    ]

    with open("data/students.txt", "w", encoding="utf-8") as data_file:
        for name in names:
            score = random.randint(0, 100)
            data_file.write(f"{name} ,  {score}  \n")

    return "data/students.txt"

def load_students():
    students = []

    with open("data/students.txt", "r", encoding="utf-8") as data_file:
        for line in data_file:
            name, score = line.strip().split(",")

            name = " ".join(name.strip().lower().split()).title()
            score = int(score.strip())

            students.append((name, score))

    return students