# 1️⃣ Vehicle Class
# Ներկայացնում է ցանկացած տրանսպորտային միջոց։
# 📌 Ատրիբուտներ
# make
#  Տիպ՝ string
#  Արտադրող (օր․ "Toyota")
# model
#  Տիպ՝ string
#  Մոդել
# year
#  Տիպ՝ int
#  Թողարկման տարեթիվ

# 📌 Մեթոդներ
# description()
# Վերադարձնում է մեքենայի ամբողջական նկարագրությունը (string)
# age(current_year)
# Հաշվում է մեքենայի տարիքը
#  Վերադարձնում է → current_year - year
# 📌 Validation
# make, model → չեն կարող լինել դատարկ
# year → չի կարող լինել ապագայում
#  Սխալի դեպքում → raise ValueError

# 2️⃣ Car Class (Vehicle-ից ժառանգված)
# 📌 Լրացուցիչ ատրիբուտ
# number_of_doors (int)

# 📌 Մեթոդներ
# description()
# Վերագրել base class-ի մեթոդը և ավելացնել դռների քանակը

# 📌 Validation
# Դռների քանակը պետք է լինի > 0

from datetime import datetime

class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new):
        if not isinstance(new, str):
            raise TypeError("Invalid Type...")
        if not new:
            raise ValueError("Invalid Value!")
        self.__make = new

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new):
        if not isinstance(new, str):
            raise TypeError("Invalid Type...")
        if not new:
            raise ValueError("Invalid Value!")
        self.__model = new

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, new):
        if not isinstance(new, int):
            raise TypeError("Invalid Type...")
        if new < 1900 or new > datetime.now().year:
            raise ValueError("Invalid Value...")
        self.__year = new


    def description(self):
        return f'''Make - {self.make} \nModel - {self.model} \nYear - {self.year}'''
    
    def age(self):
        return datetime.now().year - self.year
    

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors


    @property
    def number_of_doors(self):
        return self.__number_of_doors
    
    @number_of_doors.setter
    def number_of_doors(self, new):
        if not isinstance(new, int):
            raise TypeError("Invalid Type")
        if new < 2 or new > 6:
            raise ValueError("Invalid Value")
        self.__number_of_doors = new

    def description(self):
        print("-------Car-------")
        return super().description() + f"\nNumber of doors - {self.number_of_doors}" + "\n----------------"
    
# c = Car("Toyota", "Camry", 2015, 4)
# print(c.description())
# print(c.age())


# 3️⃣ Truck Class (Vehicle-ից ժառանգված)
# 📌 Լրացուցիչ ատրիբուտ
# cargo_capacity (float, տոննա)

# 📌 Մեթոդներ
# description()
# Ներառել բեռնատարողությունը
# 📌 Validation
# cargo_capacity > 0

class Truck(Vehicle):
    def __init__(self, make: str, model: str, year: int, cargo_capacity: float) -> None:
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity
    
    @property
    def cargo_capacity(self):
        return self.__cargo_capacity
    
    @cargo_capacity.setter
    def cargo_capacity(self, new):
        if not isinstance(new, float):
            raise TypeError("bombomboooom")
        if new <= 0:
            return ValueError("bombombom")
        
        self.__cargo_capacity = new

    def description(self):
        return super().description() + f"\nCargo capacity - {self.cargo_capacity}"
    
# truck1 = Truck("Jeep", "tiribom", 2001, 20.5)
# print(truck1.description())



# 4️⃣ Motorcycle Class (Vehicle-ից ժառանգված)
# 📌 Լրացուցիչ ատրիբուտ
# has_sidecar (bool)

# 📌 Մեթոդներ
# description()
# Նշել՝ ունի կողային կցորդ, թե ոչ

class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, has_sidecar: bool) -> None:
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    @property
    def has_sidecar(self):
        return self.__has_sidecar
    
    @has_sidecar.setter
    def has_sidecar(self, new):
        if not isinstance(new, bool):
            raise TypeError("bombombom")
        
        self.__has_sidecar = new

    def description(self):
        return super().description() + f"\nHas sidecar - {self.has_sidecar}"



# moto1 = Motorcycle("kawasaki", "gldorik", 2025, True)
# print(moto1.description())

# 5️⃣ Fleet Class
# Կառավարում է բոլոր մեքենաները

# 📌 Ատրիբուտ
# vehicles → list

# 📌 Մեթոդներ
# add_vehicle(vehicle)
# Ավելացնում է մեքենան ցուցակում

# remove_vehicle(index)
# Հեռացնում է մեքենան ըստ ինդեքսի

# list_vehicles()
# Տպում է բոլոր մեքենաների description()-ները

# filter_by_type(vehicle_type)
# Վերադարձնում է տվյալ տիպի մեքենաները
#  (օր․ միայն Car)

# total_cargo_capacity()
# Հաշվում է բոլոր Truck-ների ընդհանուր բեռնատարողությունը

class Fleet:
    def __init__(self) -> None:
        self.vehicles = []

    def add_vehicle(self, new):
        if not isinstance(new, Vehicle):
            raise TypeError("bombombom")
        self.vehicles.append(new)

    def remove_vehicle(self, i):
        if i >= len(self.vehicles):
            raise ValueError("bombombom")
        self.vehicles.pop(i)


    def list_vehicle(self):
        for i in self.vehicles:
            print(i.description())
            print("--------------\n")

    def filter_by_type(self, typ):
        if not (typ == "Car" or typ == "Truck" or Typ == "Motorcycle"):
            raise TypeError("bombombom")
        for i in self.vehicles:
            if isinstance(i, Car):
                #heriq a stope please

        
    def total_cargo_capacity(self):


# 📌 Պարտադիր Դեմո Սցենար
# Ստեղծել՝


# 2 Car
# 1 Truck
# 1 Motorcycle
# Ստեղծել Fleet
# Ավելացնել բոլոր մեքենաները
# Տպել բոլոր մեքենաները
# Տպել միայն Truck-երը
# Հաշվել ընդհանուր բեռնատարողությունը

# ⭐ Բոնուս (ոչ պարտադիր)
# Ավելացնել ID յուրաքանչյուր մեքենայի համար


# Կամ ավելացնել որոնում ըստ make/model



