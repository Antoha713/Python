class Student:
    def __init__(self, pib: str, group_number: str, birth_date: str = None, address: str = None):
        self.__pib = pib
        self.__group_number = group_number
        self.__birth_date = birth_date
        self.__address = address