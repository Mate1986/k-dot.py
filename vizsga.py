with open("file.txt", "r") as file:
    content = file.read()
    print(content)
import json

class House:
    def __init__(self, name):
        self.name = name
        self.residents = []
        self.apartments = {}

    def add_resident(self, resident):
        self.residents.append(resident)

    def remove_resident(self, resident):
        if resident in self.residents:
            self.residents.remove(resident)
        else:
            print("A lakó nem található.")

    def add_apartment(self, apartment):
        if apartment in self.apartments:
            print("A lakás már létezik.")
        else:
            self.apartments[apartment] = []

    def remove_apartment(self, apartment):
        if apartment in self.apartments:
            del self.apartments[apartment]
        else:
            print("A lakás nem található.")

    def assign_resident(self, resident, apartment):
        if apartment in self.apartments:
            self.apartments[apartment].append(resident)
        else:
            print("A lakás nem található.")

    def remove_resident_from_apartment(self, resident, apartment):
        if apartment in self.apartments:
            if resident in self.apartments[apartment]:
                self.apartments[apartment].remove(resident)
            else:
                print("A lakó nem található a lakásban.")
        else:
            print("A lakás nem található.")

    def save_info(self, file_name):
        data = {
            'name': self.name,
            'residents': self.residents,
            'apartments': self.apartments
        }
        with open(file_name, 'w') as file:
            json.dump(data, file)

    @classmethod
    def load_info(cls, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
            house = cls(data['name'])
            house.residents = data['residents']
            house.apartments = data['apartments']
            return house

    def display_residents(self):
        print("Ház lakói:")
        for resident in self.residents:
            print(resident)

    def display_apartments(self):
        print("Lakások:")
        for apartment, residents in self.apartments.items():
            print(f"{apartment}: {', '.join(residents)}")


house = House("My House")

house.add_resident("John")
house.add_resident("Jane")
house.add_resident("David")

house.add_apartment("Apartment 1")
house.add_apartment("Apartment 2")

house.assign_resident("John", "Apartment 1")
house.assign_resident("Jane", "Apartment 2")

house.display_residents()
house.display_apartments()

house.save_info("house_data.json")

loaded_house = House.load_info("house_data.json")
loaded_house.display_residents()
loaded_house.display_apartments()