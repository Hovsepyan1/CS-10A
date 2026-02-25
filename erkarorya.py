# Ստեղծել Student class, որը կունենա․
# Ատրիբուտներ
# ● name
# ● age
# ● grade
# Մեթոդներ
# ● display_info() → տպում է ուսանողի մասին տեղեկատվություն
# ● is_excellent() → վերադարձնում է True, եթե grade ≥ 18, հակառակ դեպքում False



# class Student:
#     def __init__(this, name, age, grade):
#         this.name = name
#         this.age = age
#         this.grade = grade

#     def display_info(this):
#         print(f"{this.name} is {this.age} years old and has grade of {this.grade}")

#     def is_excellent(this):
#         return f"is {this.name} excellent student?-{this.grade >= 18}"
    
# x = Student("Aren", 15, 17)
# x.display_info()
# print(x.is_excellent())



# 2․ Ստեղծել Car class, որը կունենա․
# Ատրիբուտներ
# ● brand
# ● year
# ● mileage
# Մեթոդներ
# ● display_info() → տպում է մեքենայի մասին տեղեկատվություն
# ● needs_service() → վերադարձնում է True, եթե mileage ≥ 100000, հակառակ դեպքում
# False

# class Car:
#     def __init__(self, brand, year, mileage):
#         self.brand = brand
#         self.year = year
#         self.mileage = mileage

#     def display_info(self):
#         print(f"{self.brand} of year {self.year} has rode {self.mileage} miles")

#     def needs_service(self):
#         return f"is it worth buying the {self.brand} car? - {self.mileage<=100000}"
    
# y = Car("BMW", 1989, 100001)
# y.display_info()
# print(y.needs_service())



# 3. Ստեղծել Rectangle class․
# Ատրիբուտներ
# ● width
# ● height
# Մեթոդներ
# ● area() → վերադարձնում է մակերեսը
# ● is_square() → վերադարձնում է True, եթե width = height, հակառակ դեպքում False


# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return f"the rectangle has area of {self.width * self.height}"
    
#     def is_square(self):
#         return f"is it square? - {self.width == self.height}"
    

# z = Rectangle(10, 10)
# print(z.area())
# print(z.is_square())


# 4. Ստեղծել Employee class․
# Ատրիբուտներ
# ● name
# ● salary
# ● experience_years
# Մեթոդներ
# ● display_info() → տպում է աշխատողի տվյալները
# ● is_senior() → վերադարձնում է True, եթե experience_years ≥ 5, հակառակ դեպքում
# False

# class Employee:
#     def __init__(self, name, salary, exp):
#         self.name = name
#         self.salary = salary
#         self.exp = exp
    
#     def display_info(self):
#         return f"{self.name} is robbing the company by {self.salary} every month and has experience of {self.exp}"
    
#     def is_senior(self):
#         return f"is {self.name} senior? - {self.exp >= 5}"
    
# slave = Employee("Qerop", 9000, 6)
# print(slave.display_info())
# print(slave.is_senior())





# 5. Ստեղծել Product class․
# Ատրիբուտներ
# ● name
# ● price
# ● quantity
# Մեթոդներ
# ● total_price() → վերադարձնում է ընդհանուր արժեքը (price * quantity)
# ● is_available() → վերադարձնում է True, եթե quantity > 0, հակառակ դեպքում False

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_price(self):
#         return f"total price is {self.price * self.quantity}"
    
#     def is_available(self):
#         return f"is {self.name} available? - {self.quantity > 0}"
    
# prod = Product("soap", 100, 10)
# print(prod.total_price())
# print(prod.is_available())

# from functools import wraps
# def type_check(expected_type):
#     def decorator(fn):
#         @wraps(fn)
#         def inner(*args, **kwargs):
#             print(f"Args = {args}, kwargs = {kwargs}")
#             for i in args:
#                 if not isinstance(i, expected_type):
#                     raise TypeError("sxal tip es tvel")
#             for i in kwargs.values():
#                  if not isinstance(i, expected_type):
#                     raise TypeError("sxal tip es tvel")
#             return fn(*args, **kwargs)
#         return inner
#     return decorator

# @type_check(int)
# def add(a:int, b: int) -> int: 
#     '''Addition'''
#     return a + b
# print(add(3, b=5)) # 8
# # print(add(3, "5")) # TypeError

# Ստեղծել validate_range դեկորատոր, որը․
# ● Ստուգում է, որ ֆունկցիայի վերադարձվող թիվը լինի [min_val, max_val]
# միջակայքում
# ● Եթե ոչ → գցում է ValueError
# def expected_range(min_val,max_val):
#     def validate_range(function):
#         def inner(*args,**kwargs):
#             r=function(*args,**kwargs)
#             if r not in range(min_val,max_val):
#                 raise ValueError("Sxal arjeq e")
#             return r
#         return inner
#     return validate_range

# @expected_range(0, 100)
# def get_number():
#     return 57
# print(get_number()) # ValueError

# Իրականացնել handle_specific(exception_type) դեկորատոր, որը․
# ● Բռնում է միայն նշված exception-ը
# ● Տպում է "Handled <ExceptionName>"
# ● Այլ exception-ները չի բռնում

# def handle_specific(exception_type):
#     def decorator(fn):
#         def inner(*args , **kwargs):
#             try :
#                 foo=fn(*args,**kwargs)
#             except exception_type as e :
#                 print(e)
#             else:
#                 return foo
#         return inner
#     return decorator

# @handle_specific(ZeroDivisionError)
# def divide(a, b):
#     return a / b
# divide(10, "0") # Handled ZeroDivisionError

# 10 / "0"
# try:
#     a = 10
#     b = "0"
#     print(a/b)
# except TypeError:
#     print("brnel em typerror")

# Տրված է orders.txt ֆայլը հետևյալ ձևաչափով
#  ID,Customer name, Total price
# Տպել բոլոր պատվերները, որոնց Total price >= 10000
# Փոխել 4 id ունեցող պատվերի արժեքը 15000 և գրել ֆայլում

# f = open("orders.txt", "r+")
# lines = f.readlines()
# print(lines)
# orders = []
# for i in lines:
#     info = i.strip().split(",")
#     orders.append(info)
#     if int(info[2]) >= 10000:
#         print(",".join(info))

# print(orders)

# for i in orders:
#     if i[0] == "4":
#         i[2] = "15000"

# f.seek(0)
# for i in range(len(orders)):
#     orders[i] = ",".join(orders[i]) + "\n"
# print(orders)

# f.writelines(orders)

# w w+


class dec:
    def __init__(self, func):
        def dunc(*args, **kwargs):
            return func(*args, **kwargs)
        
    def __call__(self, *args, **kwds):
        print("Aaa")
@dec
def foo():
    print("hi")

foo()