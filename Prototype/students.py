class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Dsa", "Aran"]:
            raise ValueError("Invaild house")
        self.name = name
        self._house = house

    
    def __str__(self): 
        return f"{self.name} from {self._house}"

    @classmethod
    def get(cls):
        name = input("What's your name? ")
        house = input("What's your house? ")
        return cls(name, house)



    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ("Dsa", "Aran"):
            raise ValueError("Invaild house")
        self._house = house



def main():
    student = Student.get()
    print(f"{student.name} from {student.house}")


if __name__ == "__main__":
    main()