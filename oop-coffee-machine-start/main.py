from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money_machine = MoneyMachine()

status = True
while status:
    order = input(f' What would you like? ({menu.get_items()}):').lower()
    if order == "report":
        machine.report()
        money_machine.report()
    elif order == 'off':
        status = False
    else:
        if menu.find_drink(order):
            drink = menu.find_drink(order)

            if machine.is_resource_sufficient(drink):

                if money_machine.make_payment(drink.cost):
                    machine.make_coffee(drink)
