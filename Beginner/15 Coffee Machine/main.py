from machine_data import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coin_processor(quarters, dimes, nickels, pennies):
    return (quarters * 25) + (dimes * 10) + (nickels * 5) + pennies


def reduce_resources(water_needed, coffee_needed, milk_needed):
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
        reduce_resources(water_needed, coffee_needed, milk_needed)
    return resources


user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
if user_input == "report":
    for key in resources:
        print(key, ":", resources[key])

print(enough_resources(user_input))
