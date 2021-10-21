from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
# menu_item = MenuItem()
menu = Menu()
available_menu = menu.get_items()
is_machine_off = False

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
        espresso = menu.find_drink("espresso")
        payment = money_machine.make_payment(espresso.cost)
        if payment:
            print("coffee")
            if coffee_machine.is_resource_sufficient(espresso):
                coffee_machine.make_coffee(espresso)

    # TODO 5: "Handles what happens when user enters latte"
    # TODO 6: "Handles what happens when user enters cappuccino"
