# # class Person:
# #     '''Pahum e informacia mardu masin'''
# #     def __init__(self, name, age):
# #         self.set_name(name)
# #         self.set_age(age)
# #     def get_name(self):
# #         return self.__name
    
# #     def set_name(self, new_name):
# #         if not isinstance(new_name, str):
# #             raise TypeError("Invalid type")
# #         if len(new_name) < 3:
# #             raise ValueError("Invalid value")
# #         self.__name = new_name

# #     def get_age(self):
# #         return self.__age

# #     def set_age(self, new_age):
# #         if not isinstance(new_age, (int, float)):
# #             raise TypeError("Invalid Type")
# #         if new_age < 10 or new_age > 100:
# #             raise ValueError("Invalid Value")
# #         self.__age = new_age
   
# #     def __str__(self):
# #         return f"Person - {self.name}"

# #     age = property(get_age)
# #     name= property(get_name, set_name)

# # p = Person("Aren", 15.0)
# # print(p.get_name())
# # p.set_name("Vardan")
# # print(p.get_name())

# # print(p.get_age())
# # print(p.age)
# # print(p.name)
# # p.name = "Vardan"
# # print(p.name)
# # print((p.age))
# # p.age = 85


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, new_name):
#         if not isinstance(new_name, str):
#             raise TypeError("Invalid type")
#         if len(new_name) < 3:
#             raise ValueError("Invalid value")
#         self.__name = new_name

#     # @property
#     # def age

# p = Person("Aren")
# print(p.name)







# Ստեղծել BankAccount class․
# Ատրիբուտներ և մեթոդներ՝
# private __balance
# deposit(amount) → գումար ավելացնում է (միայն եթե amount > 0)
# withdraw(amount) → գումար հանում է (միայն եթե բավարար գումար կա)
# get_balance() → վերադարձնում է balance-ը
# ❌ Չպետք է հնարավոր լինի balance-ը փոխել ուղիղ։

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        ...
    @property
    def balance(self): ##getter
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if not (isinstance(new_balance, int) or isinstance(new_balance, float)):
            raise TypeError('your value is invalid')
        if new_balance<0:
            raise ValueError('mexk a et mardy')
        

        self.__balance = new_balance

    def deposit(self, amount):
        if not amount>0:
            raise ValueError('xeloq mna')
        if not (isinstance(amount, int) or isinstance(amount, float)):
            raise TypeError('chi ylni')
        amount += self.balance
        self.balance = amount

    def withdraw(self, amount):
        if amount>self.balance:
            raise ValueError('apo kpi gorcit')
        amount = self.balance - amount
        self.balance = amount

    def get_balance(self):
        return self.balance

Arlen = BankAccount(100)
Arlen.deposit(10)
print(Arlen.get_balance())
Arlen.withdraw(10)
print(Arlen.get_balance())
