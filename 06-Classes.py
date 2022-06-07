
from audioop import add
from datetime import datetime
import csv
import os
os.system('cls')

print('\n#####################################################')
print("Complete explanation")
print('#####################################################')


class Item:  # Parent Class
    # ITEMS BELOW ARE NAMED:  Class Attribute
    pay_rate = 0.8  # pay rate after 20% discount
    # create a list of all Items (element autmatically appended on __init__)
    all = []

    # int / float: force the param to be of a type
    def __init__(self, name: str, price: float, quantity=0):
        # assert: controls parameters inputs. If invalid a AssertionError is raised
        # Run validations one the received arguments
        assert price >= 0, f"Price {price} is not a number greater or equal to 0"
        assert isinstance(
            quantity, int) and quantity >= 0, f"Price {quantity} is not a integer greater or equal to 0"

        # ITEMS BELOW ARE NAMED: Instance Attribute
        self.price = price
        self.quantity = quantity

        # creating read only attribute
        # _ = Public Attribute
        # __ = Private Attribute
        self.__name = name

        # Add item to list of items
        Item.all.append(self)

    # ITEM BELOW ARE NAMED: Instance Method
    def calculate_total_price(self):
        return self.quantity * self.price

    def apply_discount(self):
        # if Item.pay_rate as below, method always gets the Class Attribute
        # # self.price = self.price * Item.pay_rate
        # if self.pay_rate as below, method searches for instance attribute first. if found
        #   uses that. if not, uses the class attribute
        self.price = self.price * self.pay_rate

    # change how the object is printed when using instance
    def __repr__(self):
        # self.__class__.__name__ = gets the correct class name
        return f'{self.__class__.__name__}("{self.name}", {self.price}, {self.quantity})'

    # creating a class method
    @classmethod
    def instantiate_from_csv(cls):
        with open('06-items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    # create a static method
    @staticmethod
    def is_integer(num):
        # count out floats that are point 0
        # For i.e: 5.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # property decorator creating read only attribute (create getter)
    # if attribute created like this you can't assign value to it anymore
    #       using "object.attribute = 'x'"
    @property
    def name(self):
        return self.__name

    # making a setter
    @name.setter
    def name(self, value):
        # control input
        if len(value) > 15:
            raise Exception("The name is too long")
        # setting the attribute
        self.__name = value

    # creating private method that will only be used inside the class
    def __calc_stock(self):
        return 15

    def consultStock(self):
        return f"Stock currently is: {self.__calc_stock()}"


class Phone(Item):  # Child Class
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # call super initializer
        super().__init__(name, price, quantity)
        # verify new attributes
        assert broken_phones >= 0, f"Broken Phones has to be greater or equal to 0."

        # assign new attributes
        self.broken_phne = broken_phones

    def apply_discount(self, additionalDiscount):
        super().apply_discount()
        additionalDiscount = 1 - (additionalDiscount / 100)
        self.price = self.price * additionalDiscount


# -------------------------------------------------
# Print all attributes of a object
# # print(Item.__dict__)  # print all class level attributes
# # print(i1.__dict__)   # print all instance level attributes

# -------------------------------------------------
# Create several objects (they are automatically added to the Item.all Class Attribute)
# # item1 = Item("Phone", 100, 1)
# # item2 = Item("Laptop", 1000, 3)
# # item3 = Item("Cable", 10, 5)
# # item4 = Item("Mouse", 50, 5)
# # item5 = Item("Keyboard", 75, 5)

# print name and price if item
# # for instance in Item.all:
# #     print(f"Name: {instance.name}")
# #     print(f"Price: {instance.calculate_total_price()}")

# print all objects with the __repr__ method
# # print(Item.all)

# -------------------------------------------------
# instantiate objects from a CSV using a classmethod
# class methods pass the class as attribute instead of the instance
# # Item.instantiate_from_csv()
# # print(Item.all)


# -------------------------------------------------
# calling a static method
# # print(Item.is_integer(7.0))  # returns true.
# # print(Item.is_integer(7.5))  # returns false.

# -------------------------------------------------
# create instances of child class
# # phone1 = Phone("jscPhonev10", 500, 5, 1)
# # phone2 = Phone("jscPhonev10", 700, 3, 1)
# # Item1 = Item("Laptop", 223.2, 11)
# # print(Item.all)

# call parent class method
# # print(phone1.calculate_total_price())

# -------------------------------------------------
# # Read-only property
# reading the property name
# # i1 = Item("Laptop", 1254.15, 3)
# # print(i1.name)

# setting property with '__' does not work. Returns a error
# # i1.__name = "test"
# # print(i1.name)

# -------------------------------------------------
# using setter
# i1 = Item("Laptop", 1254.15, 3)
# print(i1.name)
# setting a string with more than 15 chars returns a exception
# as programmed in the setter
# # i1.name = "changed changed changed changed"
# # print(i1.name)

# -------------------------------------------------
# polymorphism = re-writing a existing function do to something different
# # i1 = Item("Lap", 1000, 2)
# # p1 = Phone("Poco", 100, 3)

# parent class does one discount
# # print(f"{i1.name} Price before discount: {i1.price}")
# # i1.apply_discount()
# # print(f"{i1.name} Price AFTER discount: {i1.price}")

# child class does parent class discount + discount passed on parameter
# # print(f"{p1.name} Price before discount: {p1.price}")
# # p1.apply_discount(10)
# # print(f"{p1.name} Price AFTER discount: {p1.price}")

# -------------------------------------------------
# Object Oriented Programming Concepts
#
# Encapsulation = is not allowing the direct access to a attribute
#                   as done with 'name' in line 33 and 83 creating '@property'
#
# Abstraction  = only showing necessary attributes or methods
#                   and hiding unnecessary attributes
#                   (Ex: line 97 private method definition  and 100 callint private method)
#
# Inheritance = re-use code across our classes
#                   ex: re-use code on child classes
#
# Polymorphism = use of a single type entity to represent different types in different scenarios
#                   First examle len() that does a different thing depending on the param
#                       string param = returns size of the string
#                       array param  = quantity of elements of the array
#                   Second example in line 115. 'apply_discount()' does the standard discount
#                       calling super().apply_discount() from parent class
#                       plus parameter passed additional discount


# TERMINATE THE APP
quit()


print('\n#####################################################')
print("Simple example")
print('\n#####################################################')
# exemplo de classe


class Pessoa:
    def __init__(self, nome, ano_nasc, peso, altura):
        self.nome = nome
        self.ano_nasc = ano_nasc
        self.peso = peso
        self.altura = altura

        # self.ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
        # ou
        self.ano_atual = int('{:%Y}'.format(datetime.now()))
        self.idade = self.ano_atual - self.ano_nasc

    def imc(self) -> float:
        return self.peso / (self.altura ** 2)


p = Pessoa("Eduard", 1983, 77, 1.83)
print(f'{p.nome} possui IMC de {p.imc():.2f}')
print(f'{p.nome} tem {p.idade} anos.')

print('\n#####################################################')
# exemplo de Herança


class Programmer(Pessoa):
    def __init__(self, nome, ano_nasc, peso, altura, language, wpm, experience):
        super().__init__(nome, ano_nasc, peso, altura)
        self.language = language
        self.wpm = wpm
        self.experience = experience

    def getCurriculumStr(self):
        return f'Prog. {self.nome} programs in {self.language} and has {self.experience} years of exp.'


prog = Programmer("Luke", 1866, 105, 2.15, "Node.js", 585, 55)
print("Calling Class function: ", prog.getCurriculumStr())
print("Calling parent Class func.: {:.3f}".format(prog.imc()))
