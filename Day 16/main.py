from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()
available_menu = menu.get_items()
is_machine_off = False


def coffee_process(drink):
    drink_name = menu.find_drink(drink)
    if coffee_machine.is_resource_sufficient(drink_name):
        drink_payment = money_machine.make_payment(drink_name.cost)
        if drink_payment:
            coffee_machine.make_coffee(drink_name)


while not is_machine_off:
    # TODO 1: "Prompt User on what they want"
    user_prompt = input(f"What would you like? {available_menu}: ")
    # TODO 2: "Turn off the coffee machine by pressing 'off'"
    if user_prompt == "off":
        is_machine_off = True
    # TODO 3: "Print Report: Should print report"
    elif user_prompt == "report":
        coffee_machine.report()
        money_machine.report()
    # TODO 4: "Handles what happens when user enters espresso"
    elif user_prompt == "espresso":
        coffee_process("espresso")
    # TODO 5: "Handles what happens when user enters latte"
    elif user_prompt == "latte":
        coffee_process("latte")
    # TODO 6: "Handles what happens when user enters cappuccino"
    elif user_prompt == "cappuccino":
        coffee_process("cappuccino")
    else:
        print("please choose from one of the option")
