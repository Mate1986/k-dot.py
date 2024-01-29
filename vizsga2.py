def add_resident(self, resident):
    self.residents.append(resident)

def remove_resident(self, resident):
    self.residents.remove(resident)

def add_apartment(self, apartment):
    self.apartments.append(apartment)

def remove_apartment(self, apartment):
    self.apartments.remove(apartment)

def assign_resident(self, resident, apartment):
    apartment.add_resident(resident)

def unassign_resident(self, resident, apartment):
    apartment.remove_resident(resident)

def save_info(self, filename):
    with open(filename, 'w') as file:
        file.write(f"Address: {self.address}\n")
        file.write("Residents:\n")
        for resident in self.residents:
            file.write(f"- {resident}\n")
        file.write("Apartments:\n")
        for apartment in self.apartments:
            file.write(f"- {apartment}\n")

def load_info(self, filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        self.address = lines[0].split(': ')[1].strip()
        self.residents = []
        self.apartments = []
        residents_section = False
        apartments_section = False
        for line in lines[1:]:
            line = line.strip()
            if line == "Residents:":
                residents_section = True
                apartments_section = False
            elif line == "Apartments:":
                residents_section = False
                apartments_section = True
            elif residents_section:
                self.residents.append(line[2:])
            elif apartments_section:
                self.apartments.append(line[2:])
def add_resident(self, resident):
    self.residents.append(resident)

def remove_resident(self, resident):
    self.residents.remove(resident)

def __str__(self):
    return f"Apartment {self.number} - Floor: {self.floor}, Rooms: {self.room_count}"
def __str__(self):
    return self.name
