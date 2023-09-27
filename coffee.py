# Import constants from separate menu module
from menu import MENU, resources


# Print a report of current resource amounts
def report(resources: dict):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


# Turn off the coffee machine
def off():
    print("Shutting down.............")
    exit()


# Check if there are enough resources to make the drink
def check_resources(menu: dict, drink: str, resources: dict):
    drink_ingredients = menu[drink]["ingredients"]

    # Loop through ingredients
    for ingredient in drink_ingredients:
        # Loop through resources
        for resource in resources:
            # Compare ingredient to resource
            if ingredient == resource:
                # Check if ingredient exceeds resource
                if drink_ingredients[ingredient] > resources[resource]:
                    print(f"There is not enough {resource}")

                    # Special case for coffee
                    if ingredient == "coffee":
                        return False

                else:
                    # Special case for coffee
                    if ingredient == "coffee":
                        return True

            else:
                continue


# Accept coins from user
def process_coins():
    print("Please insert coins.")

    # Accept coin amounts
    quarters = input("How many quarters?: ")
    while not quarters.isdigit():
        print("Invalid Input! Try again.")
        quarters = input("How many quarters?: ")
    quarters = int(quarters)
        
    dimes = input("How many dimes?: ")
    while not dimes.isdigit():
        print("Invalid Input! Try again.")
        dimes = input("How many dimes?: ")
    dimes = int(dimes)
        
    nickles = input("How many nickles?: ")
    while not nickles.isdigit():
        print("Invalid Input! Try again.")
        nickles = input("How many nickles?: ")
    nickles = int(nickles)
        
    pennies = input("How many pennies?: ")
    while not pennies.isdigit():
        print("Invalid Input! Try again.")
        pennies = input("How many pennies?: ")
    pennies = int(pennies)
    
    # Calculate total
    money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies

    return money


# Check if transaction is successful
def check_transaction(menu: dict, drink: str, money: float):
    cost = menu[drink]["cost"]

    if money >= cost:
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# Update resources based on drink ingredients
def update_resources(resources: dict, menu: dict, drink: str):
    drink_ingredients = menu[drink]["ingredients"]
    drink_cost = menu[drink]["cost"]

    for ingredient in drink_ingredients:
        for resource in resources:
            if ingredient == resource:
                resources[resource] -= drink_ingredients[ingredient]
            else:
                continue

    resources["money"] += drink_cost

    return resources


# Main program loop
while True:
    # Ask for drink choice
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Validate input
    while not user_input in ["espresso", "latte", "cappuccino", "report", "off"]:
        print("Invalid input! Try again.")
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Print report
    if user_input == "report":
        report(resources)

    # Turn off
    elif user_input == "off":
        off()

    # Make coffee
    else:
        if check_resources(MENU, user_input, resources):
            entered_amount = process_coins()
            if check_transaction(MENU, user_input, entered_amount):
                change = entered_amount - MENU[user_input]["cost"]
                resources = update_resources(resources, MENU, user_input)
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {user_input}. ENJOY")
            else:
                continue
        else:
            continue
