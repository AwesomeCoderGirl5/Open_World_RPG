from cupcake_factory_pics import base1,base2,topping1_v1,topping1_v2,topping2_v1,topping2_v2,topping3_v1,topping3_v2
import time
print("Welcome to Cupcake Factory! Here you can create your own cupcake!")
print("choose your base")
time.sleep(1)
base1()
print("unfrosted")#showcasing the bases
time.sleep(1)
base2()
print("frosted")
time.sleep(2.5)
#starts here
base_type = input("Which base would you like, unfrosted or frosted?")
if base_type == "unfrosted":
    print("great choice")
    base1()
    decoration = input("Would you like swirly icing, sprinkles,silver beads or plain?")
    if decoration == "swirly icing":
        topping2_v1()
        print("looks delicious")
        print("This will cost £2.50")
        time.sleep(1)
        print("-£2.50")
        print("enjoy your day!")
        topping2_v1()
        
    if decoration == "sprinkles":
        topping1_v1()
        print("looks delicious")
        print("This will cost £2.50")
        time.sleep(1)
        print("-£2.50")
        print("enjoy your day!")
        topping1_v1()
        
    if decoration == "silver beads":
        topping3_v1()
        print("looks delicious")
        print("This will cost £2.50")
        time.sleep(1)
        print("-£2.50")
        print("enjoy your day!")
        topping3_v1()
        
    if decoration == "plain":
        base1()
        print("looks delicious")
        print("This will cost £2")
        time.sleep(1)
        print("-£2")
        print("enjoy your day!")
        base1()
    
if base_type == "frosted":
    print("great choice")
    base2()
    decoration = input("Would you like swirly icing, sprinkles,silver beads or plain?")
    if decoration == "swirly icing":
        topping2_v2()
        print("looks delicious")
        print("This will cost £3.50")
        time.sleep(1)
        print("-£3.50")
        print("enjoy your day!")
        topping2_v2()
        
    if decoration == "sprinkles":
        topping1_v2()
        print("looks delicious")
        print("This will cost £3.50")
        time.sleep(1)
        print("-£3.50")
        print("enjoy your day!")
        topping1_v2()
        
    if decoration == "silver beads":
        topping3_v2()
        print("looks delicious")
        print("This will cost £3.50")
        time.sleep(1)
        print("-£3.50")
        print("enjoy your day!")
        topping3_v2()
        
    if decoration == "plain":
        base2()
        print("looks delicious")
        print("This will cost £3")
        time.sleep(1)
        print("-£3")
        print("enjoy your day!")
        base2() 