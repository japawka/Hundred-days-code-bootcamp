MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def generate_report():
    for key, value in resources.items():
        print(key, ':', value)


def make_drink(order, resources):
    resources['water'] -= MENU[order]["ingredients"]['water']
    if order != 'espresso':
        resources['milk'] -= MENU[order]["ingredients"]['milk']
    resources['coffee'] -= MENU[order]["ingredients"]['coffee']


def check_resources(order, resources):
    global empty
    if resources['water'] < MENU[order]["ingredients"]['water']:
        empty = "water"
        return empty
    elif order != 'espresso' and resources['milk'] < MENU[order]["ingredients"]['milk']:
        empty = "milk"
        return empty
    elif resources['coffee'] < MENU[order]["ingredients"]['coffee']:
        empty = "coffee"
        return empty
    else:
        return True


def collect_money(quarters, dimes, nickles, pennies):

    total_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total_money


def check_money(order, total_money):
    price = MENU[order]['cost']
    if total_money >= price:
        resources['money'] += price
        print(f'here is {round(total_money - price, 2)} in change ')
        return True
    else:
        print("Sorry, that's not enough money")


def machine():
    status = True
    while status:
        order = input(' What would you like? (espresso/latte/cappuccino):').lower()
        if order == "report":
            generate_report()
        elif order == 'off':
            status = False
        else:
            result = check_resources(order, resources)

            if result == True:
                print("Please insert coins")
                quarters = int(input("how many quarters? "))
                dimes = int(input("how many dimes? "))
                nickles = int(input("how many nickles? "))
                pennies = int(input("how many pennies? "))
                inserted_money = collect_money(quarters, dimes, nickles, pennies)

                if check_money(order, inserted_money):
                    make_drink(order, resources)
                    print(f"Here is your {order}")
            else:
                print(f" Sorry there is not enough {empty}.")


machine()
