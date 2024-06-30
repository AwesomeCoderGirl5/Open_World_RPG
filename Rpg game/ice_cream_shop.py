from ascii_art import icecream_plain,icecream_flake,icecream_sprinkles,icecream_fscombo
import time
print("Welcome to Frosty's Ice Cream Parlour")
print("Costs: plain costs £1 , with flake cost £1.50 , with sprinkles cost £1.25, both flake and sprinkles cost £1.75")#costs
topping_choice = input("Choose flake ,sprinkles or plain")#first choice
if topping_choice == "flake":
    icecream_flake()#print ice cream
    combination = input("Add sprinkles?").upper()
    if combination[0] == "Y":
        icecream_fscombo()
        print("that'll cost £1.75 please")
        time.sleep(1)#rp sim thing
        print("-£1.75")
        print("Thank you for stopping by at Frosty's Ice Cream Parlour! Enjoy your ice cream!")
        icecream_fscombo()
        #want a combination or not
    if combination[0] == "N":
        print("that'll cost £1.50 please")
        time.sleep(1)#rp sim thing
        print("-£1.50")
        print("Thank you for stopping by at Frosty's Ice Cream Parlour! Enjoy your ice cream!")
        icecream_flake()
        
if topping_choice == "sprinkles":
    icecream_sprinkles()
    combination = input("Add flake?").upper()
    if combination[0] == "Y":
        icecream_fscombo()
        print("that'll cost £1.75 please")
        time.sleep(1)
        print("-£1.75")
        print("Thank you for stopping by at Frosty's Ice Cream Parlour! Enjoy your ice cream!")
        icecream_fscombo()
    if combination[0] == "N":
        print("that'll cost £1.25 please")
        time.sleep(1)
        print("-£1.25")
        print("Thank you for stopping by at Frosty's Ice Cream Parlour! Enjoy your ice cream!")
        icecream_sprinkles()
        
if topping_choice == "plain":
    icecream_plain()
    combination = input("Add flake?").upper()
    if combination[0] == "Y":
        icecream_flake()
        print("that'll cost £1.50 please")
        time.sleep(1)
        print("-£1.50")
        print("Thank you for stopping by at Frosty's Ice Cream Parlour! Enjoy your ice cream!")
        icecream_flake()
    if combination[0] == "N":
        print("that'll cost £1 please")
        time.sleep(1)
        print("-£1")
        print("Thank you for stopping by at Frosty's Ice Cream Parlour! Enjoy your ice cream!")
        icecream_plain()