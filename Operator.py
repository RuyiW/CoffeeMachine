from main import MENU, resources


def print_report():
    for item in resources:
        if item == "water" or item == "milk":
            print(f"{item.title()}: {resources[item]}ml")
        elif item == "coffee":
            print(f"{item.title()}: {resources[item]}g")
        elif item == "money":
            print(f"{item.title()}: ${resources[item]}")


def greeting():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()


def check_resource(ingredients):
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            return ingredient
    return None


def get_ingredient(request):
    return MENU[request]["ingredients"]


def get_cost(request):
    return MENU[request]["cost"]


def process_coins():
    try:
        print("Please insert coins.")
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickle = int(input("How many nickles?: "))
        penny = int(input("How many pennies?: "))
        return quarter * 0.25 + dime * 0.1 + nickle * 0.05 + penny * 0.01
    except ValueError:
        print("Invalid coin numbers.")
        process_coins()


def check_transaction(inserted, price):
    if inserted < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if inserted > price:
            change = inserted - price
            print(f"Here is ${round(change, 2)} dollars in change.")
        resources["money"] = resources.get("money", 0) + price
        return True


def make_coffee(request, ingredients):
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {request}☕. Enjoy!")


def start():
    while True:
        user_input = greeting()
        if user_input == "off":
            break
        elif user_input == "report":
            print_report()
        elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
            ingredients = get_ingredient(user_input)
            shortage = check_resource(ingredients)
            if shortage is not None:
                print(f"Sorry there is not enough {shortage}.")
            else:
                inserted = process_coins()
                cost = get_cost(user_input)
                if check_transaction(inserted, cost):
                    make_coffee(user_input, ingredients)
        else:
            print("Invalid request.")

start()

