from data import MENU, resources


def sum(quarter, dime, nickel, penny):
    total = (quarter*.25)+(dime*.1)+(nickel*.05)+(penny*.01)
    return total




def check_ingredients(drink):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']

    if drink == 'report':
        print(f"Water: {water}")
        print(f"Milk: {milk}")
        print(f"Coffee: {coffee}")
        return True
    else:
        req_water = MENU[f'{drink}']['ingredients']['water']
        req_milk = MENU[f'{drink}']['ingredients']['milk']
        req_coffee = MENU[f'{drink}']['ingredients']['coffee']

        if water < req_water or milk<req_milk or coffee < req_coffee :
            if water < req_water:
                print("Sorry not enough water")
            if milk < req_milk:
                print("Sorry not enough milk")
            if coffee < req_coffee:
                print("Sorry not enough coffee")
            return True
        else:
            resources['water'] -= req_water
            resources['milk'] -= req_milk
            resources['coffee'] -= req_coffee
            return False


def check_price(coins, cost):
    if coins < cost:
        print("Sorry! That's not enough money. Money Refunded.")
        return True


def make_coffee(drink):
    cost = MENU[drink]['cost']
    print(f"\nThe cost would be ${cost}.\n")
    print("Please insert coins:")
    quarter = int(input("How many quarters? "))
    dime = int(input("How many dimes? "))
    nickel = int(input("How many nickels? "))
    penny = int(input("How many pennies? "))
    coins = sum(quarter, dime, nickel, penny)
    if not check_price(coins, cost):
        change = cost - coins
        print(f"Here is your ${change} change. ")
        print(f"Here is your {drink} ☕. Enjoy!. ")






on = True


while on is not False:
    drink = input("\nWhat would you like? (espresso/latte/cappuccino): ")
    if check_ingredients(drink) == True:
        break
    elif check_ingredients(drink) == False:
        make_coffee(drink)


