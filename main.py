# / # / # PROJECT OF DAY 15 # / # / #

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


# def take_order():
#     order = input("What would you like? (espresso/latte/cappuccino): ").lower()

#     if order == "off":
#         exit()
#     elif order == "report":
#         print(f"Water: {resources['water']}ml\n"
#               f"Milk: {resources['milk']}ml\n"
#               f"Coffee: {resources['coffee']}g\n"
#               f"Money: ${profit}")
#         return take_order()
#     elif order == "espresso" or order == "latte" or order == "cappuccino":
#         coffee_choice = order
#         return coffee_choice
#     else:
#         print("Option not accepted. Please ask for available coffee.\n")
#         return take_order()


# def check_availability():
#     coffee_choice = take_order()
#     selection = MENU[coffee_choice]["ingredients"]

#     for item in resources:
#         if item not in selection:
#             pass
#         elif resources[item] > selection[item]:
#             return coffee_choice
#         else:
#             print(f"Sorry there is no enough {item}.")
#             check_availability()


# def resource_machine():
#     coffee_choice = check_availability()
#     value_q = 0.25
#     value_d = 0.10
#     value_n = 0.05
#     value_p = 0.01
#     cost = MENU[coffee_choice]["cost"]
#     selection = MENU[coffee_choice]["ingredients"]

#     print("Please insert coins.")

#     quarters = int(input("How many quarters?: "))
#     dimes = int(input("How many dimes?: "))
#     nickles = int(input("How many nickles?: "))
#     pennies = int(input("How many pennies?: "))
#     sum_coins = (value_q * quarters) + (value_d * dimes) + (value_n * nickles) + (value_p * pennies)
#     change = "{:.2f}".format(sum_coins - cost)

#     if sum_coins < cost:
#         print("Sorry that's not enough money. Money refunded.")
#         check_availability()
#     else:
#         global profit
#         profit += cost
#         for item in resources:
#             if item not in selection:
#                 pass
#             else:
#                 resources[item] -= selection[item]
#         print(f"Here is ${change} in change. Here is your {coffee_choice} ☕️. Enjoy!")
#         check_availability()


# check_availability()
# resource_machine()


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")

    sum_coins = int(input("How many quarters?: ")) * 0.25
    sum_coins += int(input("How many dimes?: ")) * 0.10
    sum_coins += int(input("How many nickles?: ")) * 0.05
    sum_coins += int(input("How many pennies?: ")) * 0.01
    return sum_coins


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, False if money is insufficient."""
    if money_received >= drink_cost:
        change = "{:.2f}".format(money_received - drink_cost)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

# TODO: 1-. Ask "What would you like? (espresso/latte/cappuccino): "

# TODO: 2-. If input is "off" terminate the program.

# TODO: 3-. If input is "report" show the amount of resources left (and money). TODO: 1-.

# TODO: 4-. If input is {coffee_choice} check for availability. If available TODO: 5-. Else TODO: 8-.

# TODO: 5-. Say "Please insert coins." "How many quarters/dimes/nickles/pennies?: "

# TODO: 6-. If {sum_coins} not enough for {coffee_choice} say "Sorry that's not enough money. Money refunded." TODO: 1-.

# TODO: 7-. Say "Here is ${change} in change." "Here is your {coffee_choice} ☕️. Enjoy!" TODO: 1-.

# TODO: 8-. Say "Sorry there is not enough {resource}." TODO: 1-.
