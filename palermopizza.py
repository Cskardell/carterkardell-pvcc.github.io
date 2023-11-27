PR_S = 9.99
PR_M = 12.99
PR_L = 17.99
PR_X = 21.99
PR_DR = 3.99
PR_BR = 6.99
S_TAX = 0.055
num_pizza = 0
subtotal = 0
price_pizza = 0
num_drink = 0
num_bread = 0
import datetime

def main():
    another_order = True
    while another_order:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order more food (Y or N)? ")
        if yesno.lower() == "n":
            another_order = False
            print("Thank you for your business!")


def get_user_data():
    global pizza_size, num_pizza, num_drink, num_bread
    pizza_size = input("What size pizza would you like (S, M, L, or X)? ")
    num_pizza = int(input("How many of those pizzas would you like? "))
    num_drink = int(input("How many drinks would you like? "))
    num_bread = int(input("How many orders of bread would you like? "))


def perform_calculations():
    global price_pizza, pizza_total, drink_total, br_total, sales_tax, total
    if pizza_size == "S":
        price_pizza = PR_S
    elif pizza_size == "M":
        price_pizza = PR_M
    elif pizza_size == "L":
        price_pizza = PR_L
    elif pizza_size == "X":
        price_pizza = PR_X

    pizza_total = price_pizza * num_pizza
    drink_total = PR_DR * num_drink
    br_total = PR_BR * num_bread
    sales_tax = (pizza_total + drink_total + br_total) * S_TAX
    total = pizza_total + drink_total + br_total + sales_tax


def display_results():
    global line, moneyf
    moneyf = "15.2f"
    line = "___________________________________"

    print("THANK YOU FOR ORDERING WITH PALERMO PIZZA!")
    print(line)
    print("Pizza Total $", format(pizza_total, moneyf))
    print("Bread Total $", format(br_total, moneyf))
    print("Drink Total $", format(drink_total, moneyf))
    print("Sales Tax   $", format(sales_tax, moneyf))
    print("Total       $", format(total, moneyf))
    print (line)
    print(str(datetime.datetime.now()))
main()