#This Assignment uses the four OOP principles: Abstraction, Encapsulation, Inheritance, and Polymorphism
#The case study is based on 3 Major  religions in Nigeria and their characteristics.
#The religions are Christianity, Islam, and Ifa.
#To run the code, simply execute this file.  python index.py


from abc import ABC, abstractmethod

#Abstraction: Blueprint for all religions
class AbstractReligion(ABC):
    @abstractmethod
    def worship_style(self):
        pass

    @abstractmethod
    def get_sacred_texts(self):
        pass

    @abstractmethod
    def get_rituals(self):
        pass

#Encapsulation: Base Religion class
class Religion(AbstractReligion):
    def __init__(self, name, founder):
        self.name = name
        self.founder = founder
        self.__sacred_texts = []  # Private
        self.__rituals = []       # Private

    def add_sacred_text(self, text):
        self.__sacred_texts.append(text)

    def add_ritual(self, ritual):
        self.__rituals.append(ritual)

    def get_sacred_texts(self):
        return self.__sacred_texts

    def get_rituals(self):
        return self.__rituals

    def worship_style(self):
        print(f"{self.name} has its own unique way of worship.")

# Inheritance +  Polymorphism: Specific religions
class Christianity(Religion):
    def __init__(self):
        super().__init__("Christianity", "Jesus Christ")

    def worship_style(self):
        print("Christians worship in churches, pray, and read the Bible.")

class Islam(Religion):
    def __init__(self):
        super().__init__("Islam", "Prophet Muhammad")

    def worship_style(self):
        print("Muslims pray in mosques, follow the Quran, and perform daily prayers (Salat).")

class Ifa(Religion):
    def __init__(self):
        super().__init__("Ifa", "orisha Orunmila")

    def worship_style(self):
        print(" Ifá religion, worship style is deeply rooted in divination, ritual, and oral tradition, guided by spiritual practitioners known as Babalawos and Iyanifas.")
        

# Testing all religions
def main():
    christianity = Christianity()
    islam = Islam()
    ifa = Ifa()

    #Add sacred texts
    christianity.add_sacred_text("Bible")
    islam.add_sacred_text("Quran")
    ifa.add_sacred_text("Odu Ifa")

    #Add rituals
    christianity.add_ritual("Holy Communion")
    islam.add_ritual("Salat")
    ifa.add_ritual("Divination")

    #Worship style s (Polymorphism)
    christianity.worship_style()
    islam.worship_style()
    ifa.worship_style()

    #Sacred texts and rituals (Encapsulation)
    print("\nSacred Texts:")
    print("Christianity:", christianity.get_sacred_texts())
    print("Islam:", islam.get_sacred_texts())
    print("Ifa:", ifa.get_sacred_texts())

    print("\nRituals:")
    print("Christianity:", christianity.get_rituals())
    print("Islam:", islam.get_rituals())
    print("Ifa:", ifa.get_rituals())

if __name__ == "__main__":
    main()