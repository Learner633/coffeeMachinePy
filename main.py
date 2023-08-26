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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(order_ingredients):
    """Returns True if ingredients are sufficient, and False if not"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total amount of coins inserted after calculation"""
    total_coins = int(input("How many Quarters: ")) * 0.25
    total_coins += int(input("How many Dimes: ")) * 0.1
    total_coins += int(input("How many Nickles: ")) * 0.05
    total_coins += int(input("How many Pennies: ")) * 0.01
    return total_coins


def make_coffee(ordered_drink):
    """Returns the quantity of resources after making an Order."""
    for resource in resources:
        resources[resource] -= ordered_drink[resource]
        return resources


switchOn = True

while switchOn:
    order = input('What would you like? (espresso/latte/cappuccino):')

    if order == "off":
        switchOn = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[order]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            payment_successful = True
            if payment < drink['cost']:
                print("Sorry that's not enough money. Money refunded.")
                payment_successful = False
            elif payment > drink['cost']:
                change = round((payment - drink['cost']) , 2)
                profit += drink['cost']
                make_coffee(drink["ingredients"])
                print(f"Here is ${change} dollars in change.")
                print(f"And here is your {drink}. Enjoy!.")
            else:
                profit += payment
                make_coffee(drink["ingredients"])
                print(f"Here is your {order}. Enjoy!.")
