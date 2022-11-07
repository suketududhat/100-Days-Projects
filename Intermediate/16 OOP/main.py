from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
if user_input == "report":
    coffee_maker.report()
elif user_input == "off":
    None
else:
    drink = menu.find_drink(user_input)
    print(MenuItem(drink))
