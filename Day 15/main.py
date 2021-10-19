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
    def check_resources():
        print("checking........")
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

        total_doll = quart_doll + dimes_doll + nickles_doll + pennies_doll
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


    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        report()
    elif user_input == "off":
        off()
    elif user_input == "espresso":
        check_resources()
        money += make_coffee()
    elif user_input == "latte":
        money += make_coffee()
    elif user_input == "cappuccino":
        money += make_coffee()

