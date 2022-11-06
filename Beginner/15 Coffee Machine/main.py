from machine_data import MENU
import os

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coin_processor(quarters, dimes, nickels, pennies):
    return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)


def reduce_resources(coffee_type):
    try:
        water_needed = MENU[f"{coffee_type}"]["ingredients"]["water"]
        coffee_needed = MENU[f"{coffee_type}"]["ingredients"]["coffee"]
        milk_needed = MENU[f"{coffee_type}"]["ingredients"]["milk"]
    except KeyError:
        milk_needed = 0
    resources["milk"] -= milk_needed
    resources["water"] -= water_needed
    resources["coffee"] -= coffee_needed
    return resources


def enough_resources(coffee_type):
    try:
        water_needed = MENU[f"{coffee_type}"]["ingredients"]["water"]
        coffee_needed = MENU[f"{coffee_type}"]["ingredients"]["coffee"]
        milk_needed = MENU[f"{coffee_type}"]["ingredients"]["milk"]
    except KeyError:
        milk_needed = 0
    if (
        resources["water"] > water_needed
        and resources["coffee"] > coffee_needed
        and resources["milk"] > milk_needed
    ):
        return True
    print(f"Not enough resources left to make a {coffee_type}.")
    return False


machine_on = True


def coffee_machine(resources):
    global machine_on
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        for key in resources:
            print(key, ":", resources[key])
    elif user_input == "off":
        machine_on = False
    elif enough_resources(user_input):
        coffee_cost = MENU[f"{user_input}"]["cost"]
        print(f"{user_input} is ${coffee_cost}")
        print("Please insert coins:")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        money_inserted = coin_processor(quarters, dimes, nickels, pennies)
        if coffee_cost <= money_inserted:
            resources = reduce_resources(user_input)
            change = money_inserted - coffee_cost
            print(f"Your change: ${change}")
            print(f"Here's your {user_input}, enjoy!")
        else:
            print("Not enough money.")
    while machine_on:
        coffee_machine(resources)


os.system("cls")
coffee_machine(resources)
