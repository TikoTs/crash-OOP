#1
# We are defining a class named LibraryItem with the following subclasses: Book, Magazine, CD
# in creating subclasses we use inheritance and add unique attributes to each subclasses.
# class LibraryItem:
#     def __init__(self, title, subject, status):
#         self.title = title
#         self.subject = subject
#         self.status = status
#     def booking(self):
#         if self.status == 'available':
#             print('You can take this book')
#         elif self.status == 'occupied':
#             print('You can\'t take this book')
# class Book(LibraryItem):
#     def __init__(self, ISBN, authors, title, subject, status):
#         super().__init__()
#         self.ISBN = ISBN
#         self.authors = authors
# class Magazine(LibraryItem):
#     def __init__(self, journalName, volume, status):
#         super().__init__()
#         self.journalName = journalName
#         self.volume = volume
# class CD(LibraryItem):
#     def __init__(self, title, status):
#         self.title = title
#         self.status = status
#
#     def booking(self):
#         print('You can\'t take any CD')
# obj1 = LibraryItem('Samoseli Pirveli', 'book', 'available')
# obj2 = CD('Name', 'CD')
# obj1.booking()
# obj2.booking()


#2
# We are defining a class named Bank_Account which consists private attributes such as account_name and balance.
# Inside of the class constructors we are defining the deposit and withdraw methods.

# class Bank_Account:
#     def __init__(self, account_name, balance = 0):
#         self.__account_name = account_name
#         self.__balance = balance
#     def get_account_name(self):
#         return self.__account_name
#     def set_account_name(self, new_account_name):
#         self.__account_name = new_account_name
#     def get_account_balance(self):
#         return self.__balance
#     account_name_info = property(get_account_name,  set_account_name)
#     account_balance_info = property(get_account_balance)
#     def deposit(self, money):
#         self.__balance += money
#         return("თანხის შეტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {} ლარი"
#                .format(self.__balance))
#     def withdraw(self, money_back):
#         self.__balance -= money_back
#         return("თანხის გამოტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {} ლარი"
#                .format(self.__balance))
#
# costumer1 = Bank_Account('tiko', 1000)
# costumer = input("შეიყვანეთ მომხმარებლის სახელი: ")
# costumer_balance = int(input("შეიყვანეთ ანგარიშზე არსებული თანხის ოდენობა: "))
# if costumer == costumer1.account_name_info and\
#    costumer_balance == costumer1.account_balance_info:
#     code = int(input("შეიყვანეთ შესაბამისი კოდი, რომელი ოპერაციის შესრულებაც გსურთ: \n "
#                      "თანხის შეტანა:  1, თანხის გამოტანა:  2 \n"))
#     if code == 1:
#         deposit = int(input("შეიყვანეთ შესატანი თანხის ოდენობა: "))
#         if deposit>0:
#             print(costumer1.deposit(deposit))
#         elif deposit<=0:
#             print("უნდა შეიყვანოთ დადებითი რიცხვი")
#     elif code == 2:
#         withdraw = int(input("შეიყვანეთ გამოსატანი თანხის ოდენობა: "))
#         if withdraw <= costumer_balance:
#             print(costumer1.withdraw(withdraw))
#         else: print("ანგარიშზე საკმარისი თანხა არ არის")
#     else: print("შეიყვანეთ მხოლოდ 1 ან 2")
# else: print("მომხმარებლის სახელი ან ბალანსი არასწორია")




#3
# A simple code which calculates the distance between two points A and B.
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return "({}, {})".format(self.x, self.y)
#     def distance(self):
#         return ("The distance between the two points is: ", ((b_x-a_x)**2+(b_y-a_y)**2)**0.5)
#
# a_x = float(input("Input the X coordinate of point A"))
# a_y = float(input("Input the Y coordinate of point A"))
# a = Point(a_x, a_y)
# print(a)
# b_x = float(input("Input the X coordinate of point B"))
# b_y = float(input("Input the Y coordinate of point B"))
# b = Point(b_x, b_y)
# print(b)
# print(a.distance())




#4
# We are defining a class named Currency with the next atributes: value and unit. The value attribute indicates
#the balance and the unit indicates the currency(for example: "GEL","EUR","USD")
# class Currency:
#     def __init__(self, value, unit='GEL'):
#         self.value = value
#         self.unit = unit
#     def __str__(self):
#         if isinstance(self.value, int):
#             print(str(self.value) + '.00',self.unit)
#         else:
#             for each in str(self.value):
#                 index = str(self.value).find('.')
#                 print(str(self.value)[:index+3], self.unit)
#                 break
#     def ChangeTo(self,change_to_unit):
#         if self.unit == 'USD' and change_to_unit=='GEL':
#             new = self.value * 3.22
#             return new
#         elif self.unit == 'GEL' and change_to_unit == 'USD':
#             new = self.value*0.31
#             return new
#             # print((self.value*0.31), change_to_unit)
#         elif self.unit == 'EUR' and change_to_unit=='GEL':
#             print((self.value*3.56), change_to_unit)
#         elif self.unit == 'GEL' and change_to_unit=='EUR':
#             print((self.value * 0.28),change_to_unit)
#         elif self.unit == 'EUR' and change_to_unit == 'USD':
#             print((self.value*1.11), change_to_unit)
#         elif self.unit == 'USD' and change_to_unit=='EUR':
#             print((self.value*0.9), change_to_unit)
#     def __add__(self, other):
#         if isinstance(other,Currency):
#             if self.unit == other.unit:
#                 sum = self.value + other.value
#                 print(sum, self.unit)
#             elif self.unit == 'USD' and other.unit != 'USD':
#                 sum = self.value + other.ChangeTo(self.unit)
#                 print(sum,self.unit)
#         else:
#             sum = self.value + other
#             print(sum, self.unit)
#     def __radd__(self, other):
#         self.__add__(other)
#     def __mul__(self, other):
#         try:
#             multiple = self.value * other
#             print(multiple, self.unit)
#
#         except TypeError: print('გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვებზე')
#
#     def __rmul__(self, other):
#         self.__mul__(other)
#     def __gt__(self, other):
#         if self.unit == other.unit:
#             if self.value > other.value:
#                 return True
#             elif self.value==other.value:
#                 print('ერთმანეთის ტოლია')
#             else: print('ნაკლებია {} {}'.format(self.value, self.unit))
#
# obj1 = Currency(190, 'USD')
# obj2 = Currency(120,'USD')
# print(obj1<obj2)





