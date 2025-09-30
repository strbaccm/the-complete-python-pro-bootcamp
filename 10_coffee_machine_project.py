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
}


# print resources
def print_resources(money):
    """Printing the resources."""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money:$ {money}")

# check if the resources are sufficient
def resources_sufficient(order):
    """Checks if the resources are sufficient."""
    if order == "espresso":
        milk = 0
    else:
        milk = MENU[order]["ingredients"]["milk"]
    water = MENU[order]["ingredients"]["water"]
    coffee = MENU[order]["ingredients"]["coffee"]

    if resources["milk"] < milk:
        print("There is not enough milk!")
        return False

    elif resources["water"] < water:
        print("There is not enough water!")
        return False

    elif resources["coffee"] < coffee:
        print("There is not enough coffee!")
        return False
    else:
        print("There is enough resources!")
        return True

#update resources
def update_resources(order):
    """Updating resources after ordering."""
    if order == "espresso":
        milk = 0
    else:
        milk = MENU[order]["ingredients"]["milk"]
    water = MENU[order]["ingredients"]["water"]
    coffee = MENU[order]["ingredients"]["coffee"]

    resources["milk"] -= milk
    resources["water"] -= water
    resources["coffee"] -= coffee



# inserting coins
def calculating_coins(order,money):
    """Inserting coins and calculating the score. U"""
    print("Insert coins!")
    quarters = int(input("Input number of quarters:"))
    dimes = int(input("Input number of dimes:"))
    nickles = int(input("Input number of nickles:"))
    pennies = int(input("Input number of pennies:"))
    score = round(0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies,2)
    print(f"The score is {score}")
    order_cost = MENU[order]["cost"]
    print(f"Cost of the order is {order_cost}")

    if score == order_cost:
        money += score
        update_resources(order)
    elif score > order_cost:
        money += score
        update_resources(order)
        print(f"The change is:{round(score - order_cost, 2)}")
    else:
        money += 0
        print("There is not enough money")

    return money

def coffee_machine():
    machine_on = True
    money = 0.0

    while machine_on:
        prompt = input("What would you like? (espresso/latte/cappuccino):")

        if prompt in ["espresso", "latte", "cappuccino"]:
            if resources_sufficient(prompt):
                money = calculating_coins(prompt, money)
        elif prompt == "resources":
            print_resources(money)
        elif prompt == "off":
            print("Turning the machine off! Bye bye!")
            machine_on = False
        else:
            print("Invalid input!")

coffee_machine()
