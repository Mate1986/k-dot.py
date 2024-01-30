import json

class HouseManager:
    def __init__(self):
        self.house = {}

    def add_resident(self, name, apartment):
        if apartment not in self.house:
            self.house[apartment] = []
        self.house[apartment].append(name)

    def remove_resident(self, name, apartment):
        if apartment in self.house and name in self.house[apartment]:
            self.house[apartment].remove(name)
            if len(self.house[apartment]) == 0:
                del self.house[apartment]

    def add_apartment(self, apartment, floor):
        if apartment not in self.house:
            self.house[apartment] = {"floor": floor, "residents": []}

    def remove_apartment(self, apartment):
        if apartment in self.house:
            del self.house[apartment]

    def assign_resident(self, name, apartment):
        if apartment in self.house:
            self.house[apartment]["residents"].append(name)

    def remove_resident_from_apartment(self, name, apartment):
        if apartment in self.house and name in self.house[apartment]["residents"]:
            self.house[apartment]["residents"].remove(name)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.house, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            self.house = json.load(file)

    def display_all_residents(self):
        for apartment, residents in self.house.items():
            print(f"Apartment: {apartment}")
            for resident in residents:
                print(resident)
            print()

    def display_all_apartments(self):
        for apartment, details in self.house.items():
            print(f"Apartment: {apartment}")
            print(f"Floor: {details['floor']}")
            print(f"Residents: {details['residents']}")
            print()

    def display_apartment_details(self, apartment):
        if apartment in self.house:
            details = self.house[apartment]
            print(f"Apartment: {apartment}")
            print(f"Floor: {details['floor']}")
            print(f"Residents: {details['residents']}")
        else:
            print("Apartment not found")

    def display_apartments_on_floor(self, floor):
        for apartment, details in self.house.items():
            if details['floor'] == floor:
                print(f"Apartment: {apartment}")
                print(f"Floor: {details['floor']}")
                print(f"Residents: {details['residents']}")
                print()

    def display_apartments_of_type(self, apartment_type):
        for apartment, details in self.house.items():
            if apartment.startswith(apartment_type):
                print(f"Apartment: {apartment}")
                print(f"Floor: {details['floor']}")
                print(f"Residents: {details['residents']}")
                print()

def main():
    manager = HouseManager()

    while True:
        print()
        print("1. Add resident to the house")
        print("2. Remove resident from the house")
        print("3. Add apartment to the house")
        print("4. Remove apartment from the house")
        print("5. Assign resident to apartment")
        print("6. Remove resident from apartment")
        print("7. Save information to file")
        print("8. Load information from file")
        print("9. Display residents list")
        print("10. Display apartments list")
        print("11. Display apartment details")
        print("12. Display apartments on floor")
        print("13. Display apartments of a certain type")
        print("14. Exit")
        print()

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of the resident: ")
            apartment = input("Enter the apartment number: ")
            manager.add_resident(name, apartment)
        elif choice == "2":
            name = input("Enter the name of the resident: ")
            apartment = input("Enter the apartment number: ")
            manager.remove_resident(name, apartment)
        elif choice == "3":
            apartment = input("Enter the apartment number: ")
            floor = int(input("Enter the floor number: "))
            manager.add_apartment(apartment, floor)
        elif choice == "4":
            apartment = input("Enter the apartment number: ")
            manager.remove_apartment(apartment)
        elif choice == "5":
            name = input("Enter the name of the resident: ")
            apartment = input("Enter the apartment number: ")
            manager.assign_resident(name, apartment)
        elif choice == "6":
            name = input("Enter the name of the resident: ")
            apartment = input("Enter the apartment number: ")
            manager.remove_resident_from_apartment(name, apartment)
        elif choice == "7":
            filename = input("Enter the filename to save to: ")
            manager.save_to_file(filename)
        elif choice == "8":
            filename = input("Enter the filename to load from: ")
            manager.load_from_file(filename)
        elif choice == "9":
            manager.display_all_residents()
        elif choice == "10":
            manager.display_all_apartments()
        elif choice == "11":
            apartment = input("Enter the apartment number: ")
            manager.display_apartment_details(apartment)
        elif choice == "12":
            floor = int(input("Enter the floor number: "))
            manager.display_apartments_on_floor(floor)
        elif choice == "13":
            apartment_type = input("Enter the type of apartment: ")
            manager.display_apartments_of_type(apartment_type)
        elif choice == "14":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()