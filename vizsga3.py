import json

class HouseManager:
    def __init__(self):
        self.residents = []
        self.apartments = []

    def add_resident(self, name):
        self.residents.append(name)
        print(f"{name} hozzáadva a lakókhoz.")

    def remove_resident(self, name):
        if name in self.residents:
            self.residents.remove(name)
            print(f"{name} eltávolítva a lakók közül.")
        else:
            print(f"{name} nem található a lakók között.")

    def add_apartment(self, number, floor, type):
        for apartment in self.apartments:
            if apartment["number"] == number:
                print(f"{number}. lakás már létezik.")
                return
        self.apartments.append({"number": number, "floor": floor, "type": type})
        print(f"{number}. lakás hozzáadva.")

    def remove_apartment(self, number):
        for apartment in self.apartments:
            if apartment["number"] == number:
                self.apartments.remove(apartment)
                print(f"{number}. lakás eltávolítva.")
                return
        print(f"{number}. lakás nem található.")

    def assign_resident(self, resident, apartment_number):
        for apartment in self.apartments:
            if apartment["number"] == apartment_number:
                apartment["residents"] = apartment.get("residents", []) + [resident]
                print(f"{resident} hozzárendelve a {apartment_number}. lakáshoz.")
                return
        print(f"{apartment_number}. lakás nem található.")

    def remove_resident_from_apartment(self, resident, apartment_number):
        for apartment in self.apartments:
            if apartment["number"] == apartment_number:
                if "residents" in apartment and resident in apartment["residents"]:
                    apartment["residents"].remove(resident)
                    print(f"{resident} eltávolítva a {apartment_number}. lakásból.")
                else:
                    print(f"{resident} nem található a {apartment_number}. lakásban.")
                return
        print(f"{apartment_number}. lakás nem található.")

    def save_data(self, filename):
        data = {"residents": self.residents, "apartments": self.apartments}
        with open(filename, "w") as file:
            json.dump(data, file)
        print("Adatok mentése sikeres.")

    def load_data(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            self.residents = data.get("residents", [])
            self.apartments = data.get("apartments", [])
        print("Adatok betöltése sikeres.")

    def display_residents(self):
        print("Lakók listája:")
        for resident in self.residents:
            print(resident)

    def display_apartments(self):
        print("Lakások listája:")
        for apartment in self.apartments:
            print(f"{apartment['number']}. lakás - {apartment['type']}, {apartment['floor']}. emelet")

    def display_apartment_info(self, apartment_number):
        for apartment in self.apartments:
            if apartment["number"] == apartment_number:
                print(f"{apartment_number}. lakás információi:")
                print(f"Típus: {apartment['type']}")
                print(f"Emelet: {apartment['floor']}")
                print("Lakók:")
                for resident in apartment.get("residents", []):
                    print(resident)
                return
        print(f"{apartment_number}. lakás nem található.")

    def display_apartments_on_floor(self, floor):
        print(f"{floor}. emelet lakásai:")
        for apartment in self.apartments:
            if apartment["floor"] == floor:
                print(f"{apartment['number']}. lakás - {apartment['type']}")

    def display_apartments_by_type(self, type):
        print(f"{type} típusú lakások:")
        for apartment in self.apartments:
            if apartment["type"] == type:
                print(f"{apartment['number']}. lakás - {apartment['floor']}. emelet")

# Példa használat:

manager = HouseManager()

while True:
    print("\n------ Házkezelő Alkalmazás ------")
    print("1. Lakók hozzáadása")
    print("2. Lakók eltávolítása")
    print("3. Lakások hozzáadása")
    print("4. Lakások törlése")
    print("5. Lakók hozzárendelése a lakáshoz")
    print("6. Lakók eltávolítása a lakásból")
    print("7. Információk mentése fájlba")
    print("8. Információk letöltése fájlból")
    print("9. Lakók teljes listájának megjelenítése")
    print("10. Lakások teljes listájának megjelenítése")
    print("11. Információk megjelenítése egy adott lakásról")
    print("12. Információk megjelenítése egy adott emeleten lévő lakásokról")
    print("13. Információk megjelenítése azonos típusú lakásokról")
    print("0. Kilépés")

    choice = input("Válassz egy lehetőséget: ")

    if choice == "1":
        name = input("Add meg a lakó nevét: ")
        manager.add_resident(name)
    elif choice == "2":
        name = input("Add meg a lakó nevét: ")
        manager.remove_resident(name)
    elif choice == "3":
        number = input("Add meg a lakás számát: ")
        floor = input("Add meg a lakás emeletét: ")
        type = input("Add meg a lakás típusát: ")
        manager.add_apartment(number, floor, type)
    elif choice == "4":
        number = input("Add meg a lakás számát: ")
        manager.remove_apartment(number)
    elif choice == "5":
        resident = input("Add meg a lakó nevét: ")
        apartment_number = input("Add meg a lakás számát: ")
        manager.assign_resident(resident, apartment_number)
    elif choice == "6":
        resident = input("Add meg a lakó nevét: ")
        apartment_number = input("Add meg a lakás számát: ")
        manager.remove_resident_from_apartment(resident, apartment_number)
    elif choice == "7":
        filename = input("Add meg a fájl nevét: ")
        manager.save_data(filename)
    elif choice == "8":
        filename = input("Add meg a fájl nevét: ")
        manager.load_data(filename)
    elif choice == "9":
        manager.display_residents()
    elif choice == "10":
        manager.display_apartments()
    elif choice == "11":
        apartment_number = input("Add meg a lakás számát: ")
        manager.display_apartment_info(apartment_number)
    elif choice == "12":
        floor = input("Add meg az emelet számát: ")
        manager.display_apartments_on_floor(floor)
    elif choice == "13":
        type = input("Add meg a lakás típusát: ")
        manager.display_apartments_by_type(type)
    elif choice == "0":
        break
    else:
        print("Érvénytelen választás.")
