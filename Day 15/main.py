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
money = 0
is_machine_off = False


def off():
    global is_machine_off
    is_machine_off = True


while not is_machine_off:
    def remove_resources():
        resource = {}
        water_resources = resources['water']
        milk_resources = resources['milk']
        coffee_resource = resources['coffee']

        water_requirement = MENU[user_input]['ingredients']['water']
        if user_input == "espresso":
            milk_requirement = 0
            coffee_requirement = MENU[user_input]['ingredients']['coffee']
        else:
            milk_requirement = MENU[user_input]['ingredients']['milk']
            coffee_requirement = MENU[user_input]['ingredients']['coffee']

        resource['water'] = water_resources - water_requirement
        resource['milk'] = milk_resources - milk_requirement
        resource['coffee'] = coffee_resource - coffee_requirement

        return resource


    def check_resources():
        # print("checking........")
        water = MENU[user_input]['ingredients']['water']
        if user_input == "espresso":
            milk = 0
            coffee = MENU[user_input]['ingredients']['coffee']
        else:
            coffee = MENU[user_input]['ingredients']['coffee']
            milk = MENU[user_input]['ingredients']['milk']

        if water > resources['water']:
            print("There is not enough water")
            return True
        elif milk > resources['milk']:
            print("There is not enough milk")
            return True
        elif coffee > resources['coffee']:
            print("There is not enough Coffee")
        else:
            return False


    def make_coffee():
        user_amount = process_payment()
        cost = MENU[user_input]['cost']
        if user_amount < cost:
            print("Sorry that's not enough money, Money refunded")
        elif user_amount > cost:
            user_change = user_amount - cost
            print(f"This is your change ${user_change}")
            print(f"Your {user_input} is ready ")
            return cost
        else:
            print(f"Your {user_input} is ready ")
            return cost


    def process_coin(quarter, dimes, nickles, pennies):
        quart_doll = quarter * 0.25
        dimes_doll = dimes * 0.10
        nickles_doll = nickles * 0.05
        pennies_doll = pennies * 0.01

        total_doll = round(quart_doll + dimes_doll + nickles_doll + pennies_doll, 2)
        return total_doll


    def process_payment():
        print("Please insert coins")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))

        total = process_coin(quarters, dimes, nickles, pennies)

        return total


    def report():
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {money}$")


    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        report()
    elif user_input == "off":
        off()
    elif user_input == "espresso":
        resources_value = check_resources()
        if resources_value:
            is_machine_off = True
        else:
            resources = remove_resources()
            money += make_coffee()
    elif user_input == "latte":
        resources_value = check_resources()
        if resources_value:
            is_machine_off = True
        else:
            resources = remove_resources()
            money += make_coffee()
    elif user_input == "cappuccino":
        resources_value = check_resources()
        if resources_value:
            is_machine_off = True
        else:
            resources = remove_resources()
            money += make_coffee()
