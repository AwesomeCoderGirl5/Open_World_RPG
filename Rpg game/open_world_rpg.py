from rpg_pics import bridge1,bridge2,bridge3,plain_road,shop1,shop2,insideHome,upstairs,upstairs_sleeping,upstairs_chest,forest_LVL1,plain_forest,forest_town,forest_cave,forest_LVL2,forest_LVL3,ruined_village
import time
from random import randint
from random import choice
inventory = []
weapons = {}
#making it a lot more like animal crossing with an rpg fighting element
def forest_Level_5(health,gold_coins):#buffed mage plus worm rematch final boss
    forest_LVL3()
    print("Mage: You came back... Are you ready to face me - and my monsters?")
    time.sleep(2.5)
    print("You: I'm ready.")
    time.sleep(2.5)
    print("Mage: Well then, prepare for a challenge!")
    time.sleep(1)
    print("FINAL BOSS!")
    enemy_health = 150
    print(f"""  Enemy Health = {enemy_health}
             _____________________
            |_____________________|
            Your health = {health}
            """)
    print("enemy also has 18 damage resistance with a 50% chance and 40 attack strength")
    fight(150,100,18,gold_coins,5)
    print("Mage: Grrr... ")
    time.sleep(1)
    print("You see that there is no sign of the giant worm that accompanied him")
    time.sleep(1)
    print("The journey has been long and difficult. You're just going to assume it's dead as well.")
    time.sleep(2.5)
    print("Well Done! You have beaten the game!")
    stats = (f"""  Your stats:
              Weapons obtained: {weapons}
              There are 4 weapons to collect
              Gold coins collected: {gold_coins}
              Items collected: {inventory}
            """)
    print(stats)
    input()
    exit()


    
def forest_Level_4(health,gold_coins):#seeing decruction - gearing up
    plain_forest()
    input()
    ruined_village()
    print("You see that the monsters are already wrecking villages!")
    input()
    print("Villager: A giant worm destroyed our village! Can you help us?")
    time.sleep(2.5)
    print("You: I fought the mage who released that monster, he's not yet dead though.... I'll help you")
    time.sleep(2.5)
    print("Villager: I recovered a chest from the damage - take what you need")
    input()
    print(f""" The chest contained:
    ___
   |_-_| The chest contained:
         - 2x healing potions
         - 1x obsidian sword
         - 3x loaves of bread
         - 75 gold coins
     """)
    inventory.append("3x loaves of bread")
    inventory.append("2x healing potions")
    gold_coins = gold_coins + 75
    weapons["obsidian_sword"] = 30
    time.sleep(1)
    print("Villager: Good luck! We have been threatened for too long by the mage and his monsters...")
    time.sleep(2.5)
    print("You: Don't worry, I'll find him....")
    input()
    plain_forest()
    forest_Level_5(100,gold_coins)
    
def forest_Level_3(health,gold_coins):#you encouter mage for first time
    plain_forest()
    print("Health:")
    print(health)
    if health < 100 and "icecream" or "cupcake" in inventory:
        print("You can eat the food you bought earlier on to restore your health")
        time.sleep(0.5)
        print("You open your inventory...")
        time.sleep(1.5)
        print(inventory)
        choose = input("enter the food you want to eat")
        if choose == "icecream":
            print("You eat the ice cream...")
            time.sleep(1)
            health = 100
            inventory.remove("icecream")
        elif choose == "cupcake":
            print("You eat the cupcake...")
            time.sleep(1)
            health = 100
            inventory.remove("cupcake")
        else:
            print("You must choose a food")
            choose = input("enter the food you want to eat")    
            
    print("Gold coins:")
    print(gold_coins)
    input()
    enchantments = ["super strength","invisiblity","night vision","knockback","poison resistant"]
    print("You come across an enchanted orchard")
    time.sleep(1)
    print("Full of magical apples of all kinds")
    time.sleep(1)
    print("Said to do all kinds of things, like strength or invisiblity, or night vision")
    pick == input("Would you like to pick one?").upper()
    if "Y" in pick:
        print("You take an apple off one of the trees")
        time.sleep(1)
        print("You hold it in your hand")
        time.sleep(1)
        enchant = random.choice(enchantments)
        print("It is enchanted with", enchant)
        enchant_apple = "enchanted apple " + enchant
        inventory.append(enchant_apple)
        print("You put it into your inventory")
        input()
        plain_forest()
        input()
        forest_LVL3()
        input()
        print("You encounter the evil mage!")
        time.sleep(1.5)
        print("You: You were the one who released the monsters!")
        time.sleep(2.5)
        print("Mage: Yes! My monsters will terrorize the land!")
        time.sleep(2.5)
        print("You: Not if I can help it!")
        time.sleep(1)
        enemy_health = 116
        print(f"""  Enemy Health = {enemy_health}
             _____________________
            |_____________________|
            Your health = {health}
             """)
        print("enemy also has 15 damage resistance with a 50% chance and 30 attack strength")
        fight(116,100,15,gold_coins,3)
        print("Well done")
        time.sleep(1)
        print("Mage: I'll be back...")
        time.sleep(2)
        input()
        #exit()
        forest_Level_4(100,gold_coins)    

    if "N" in pick:
        plain_forest()
        input()
        forest_LVL3()
        input()
        print("You encounter the evil mage!")
        time.sleep(1.5)
        print("You: You were the one who released the monsters!")
        time.sleep(2.5)
        print("Mage: Yes! My monsters will terrorize the land!")
        time.sleep(2.5)
        print("You: Not if I can help it!")
        time.sleep(1)
        enemy_health = 116
        print(f"""  Enemy Health = {enemy_health}
             _____________________
            |_____________________|
            Your health = {health}
             """)
        print("enemy also has 15 damage resistance with a 50% chance and 30 attack strength")
        fight(116,100,15,gold_coins,3)
        print("Well done")
        time.sleep(1)
        print("Mage: I'll be back...")
        time.sleep(2)
        input()
        #exit()
        forest_Level_4(100,gold_coins)  

def forest_Level_2(health,gold_coins):
    plain_forest()
    direction = input("do you want to go left or right?")
    if direction == "left":
        print("you discover a forest village")
        forest_town()#another village
        input()
        print("all your health is healed here due to the campfire")
        health = 100
        print("health:")
        print(health)
        choice = ""
        while choice != "talk to the villagers":
            choice = input("Do you want to explore the houses for a chest or talk to the villagers?")
            if choice == "explore the houses":
                insideHome()
                print("it looks just like your home!")
                input()
                upstairs()
                print("You see a villager upstairs!")
                time.sleep(2.5)
                print("Villager: What are you doing in my house?")
                time.sleep(2.5)
                print("You: I was trying to find a chest.")
                time.sleep(2.5)
                print("Villager: One of those adventurers, hmmm? Well, you should have asked first.")
        
            if choice == "talk to the villagers":
                time.sleep(2.5)
                print("Villager: Hello, adventurer. What brings you here?")
                time.sleep(2.5)
                print("You: This is an interesting place. I want to find more items to help me survive in this forest.")
                time.sleep(2.5)
                print("Villager:Ah, I see. I can sell you some things")
                time.sleep(2.5)
                print("The villager shows you inside their house")
                time.sleep(2.5)
                insideHome()
                print("You: Wow! It's just like my home")
                time.sleep(1)
                upstairs()
                while "gold_sword" not in weapons:
                    print("Villager: Here, I have a gold sword - 50 gold , a strength potion - 25 gold , a torch - 20 gold and a map -30 gold")
                    buy = input("What would you like to buy off the Villager?")
                    if buy == "gold sword":
                        print("That'll be 50 gold")
                        if gold_coins < 50:
                            print("Sorry you don't have enough gold")
                        gold_coins = gold_coins - 50
                        weapons["gold_sword"] = 18
                        print("Bought!")
                    
                    if buy == "strength potion":
                        print("That'll be 25 gold")
                        if gold_coins < 25:
                            print("Sorry you don't have enough gold")
                        gold_coins = gold_coins - 25
                        inventory.append("strength_potion")
                        print("Bought!")
                        
                    if buy == "torch":
                        print("That'll be 20 gold")
                        if gold_coins < 20:
                            print("Sorry you don't have enough gold")
                        gold_coins = gold_coins - 20
                        inventory.append("torch")
                        print("Bought!")
                        
                    if buy == "map":
                        print("That'll be 30 gold")
                        if gold_coins < 30:
                            print("Sorry you don't have enough gold")
                        gold_coins = gold_coins - 30
                        inventory.append("map")
                        print("Bought!")
                        
                print("Villager: Thank you for buying my items! Be safe on your travels!")
                time.sleep(2)
                print("You: Thanks. I'm going to head off now.")
                time.sleep(2)
                plain_forest()
                input()
                forest_cave()#sidequest
                cavechoice = input("If you bought a torch last time, you can explore this cave now. This is an optional sidequest so just say skip if you don't want do it. Otherwise say yes")
                if cavechoice == "yes":
                    if "torch" in inventory:
                        print("you go in, since you have a torch")
                        forest_cave()
                        input()
                        print("You explore deeper into the cave")
                        input()
                        print("You see a bridge leading to a glimmer in the darkness... you cross it, eager to fnd out more...")
                        input()
                        print("The glimmer turns out to be a mystical sword, stuck in stone.")
                        if "strength_potion" in inventory:
                            print("You drink the strength potion you bought earlier, feeling a wave of power wash over you.")
                            inventory.remove("strength_potion")
                            time.sleep(1.5)
                            print("you heave the sword out of the stone")
                            time.sleep(3)
                            print("You free it, it is a magnificent sword with a silver blade, it does 25 damage")
                            sword_name = input("Name your sword")#only sword you can name because sidequest
                            weapons[sword_name] = 25
                            print("Putting the sword into your inventory, you smile to yourself")
                            time.sleep(1)
                            print("You make your way back out of the cave")
                            time.sleep(2)
                            plain_forest()
                            input()
                            forest_LVL2()
                            skip = input()
                            if skip == "skip fight":
                                forest_Level_3(health,gold_coins)
                            print("you encounter the alien monster!")
                            time.sleep(1)
                            enemy_health = 108
                            print(f"""  Enemy Health = {enemy_health}
                                _____________________
                               |_____________________|
                           Your health = {health}
                            """)
                            print("enemy also has 10 damage resistance with a 50% chance and 20 attack strength")
                            forest_LVL2()
                            fight(108,health,10,gold_coins,2)#level 2 slightly more challenging
                            print("Well done")
                            input()
                            #print("Level 3 coming soon")
                            forest_Level_3(health,gold_coins)
                            exit()
                    
                    
                    if "torch" not in inventory:
                        print("you enter a dark, mysterious cave")
                        forest_cave()
                        input()
                        print("you wander further into the darkness....")
                        input()
                        print("without a torch you cannot see... and you fall in the abyss....")
                        time.sleep(2)
                        print(f""" you died! :( """) # this bit is the death script
                        time.sleep(0.5)
                        print(f"""dropped {gold_coins} gold coins""")
                        print("respawning")
                        time.sleep(3)
                        atHome(0)
                    
                
                if cavechoice == "skip":#go directly to fight
                    forest_LVL2()
                    skip = input()
                    if skip == "skip fight":
                        forest_Level_3(health,gold_coins)
                    print("you encounter the alien monster!")
                    time.sleep(1)
                    enemy_health = 108
                    print(f"""  Enemy Health = {enemy_health}
                        _____________________
                       |_____________________|
                   Your health = {health}
                    """)
                    print("enemy also has 10 damage resistance with a 50% chance and 20 attack strength")
                    forest_LVL2()
                    fight(108,health,10,gold_coins,2)#level 2 slightly more challenging
                    print("Well done")
                    input()
                    #print("Level 3 coming soon")
                    forest_Level_3(health,gold_coins)
                    exit()
                
                  
                  
                
    if direction == "right":
        print("you enter a dark, mysterious cave")
        forest_cave()
        input()
        print("you wander further into the darkness....")
        input()
        print("without a torch you cannot see... and you fall in the abyss....")
        time.sleep(2)
        print(f""" you died! :( """) # this bit is the death script
        time.sleep(0.5)
        print(f"""dropped {gold_coins} gold coins""")
        print("respawning")
        time.sleep(3)
        atHome(0)
      
      
      
def fight(enemy_health,health,enemy_resistance,gold_coins,lvl):
    time.sleep(2)
    print("3!")
    time.sleep(1)
    print("2!")
    time.sleep(1)
    print("1!")
    time.sleep(1)
    print("Fight!")
    time.sleep(0.5)
    print("weapons:")
    print(weapons)
    print("number after the name of the weapon is the max damage")
    time.sleep(1.5)
    print("If you have done any sidequests, you can use that weapon. Otherwise, you use the next best weapon that you have")
    time.sleep(1)
    if lvl == 1:
        damagelimit = weapons.get("iron_sword")
    if lvl == 2:
        damagelimit = weapons.get("gold_sword")
    if lvl == 3 and cavechoice == "yes":
        swordname = input("Copy down the name of your sword")
        damagelimit = weapons.get(swordname)
    if lvl == 3:
        damagelimit = weapons.get("gold_sword")
        
    if lvl == 5:
        damagelimit = weapons.get("obsidian_sword")
    while enemy_health != 0:
        attack = int(input("enter the amount of damage you want the enemy to take , you cannot enter more than your sword can deal"))
        if attack > damagelimit:
            print("you cannot enter more than your sword can deal")
            while attack > damagelimit:
                attack = int(input("enter the amount of damage you want the enemy to take , you cannot enter more than your sword can deal"))
            
        resist_chance = randint(0,100) 
        if resist_chance <= 50:
            enemy_health = enemy_health - attack
            print(f"""  Enemy Health = {enemy_health}
                    _____________________
                   |__________________|__|
                   Your health = {health}
            """)
            
        if resist_chance >= 50:
            print("the enemy resisted your attack!")
            print(f"""  Enemy Health = {enemy_health}
                    _____________________
                   |__________________|__|
                   Your health = {health}
            """)
        print("Enemy's turn!")
        enemy_attack = randint(1,10)
        block_chance = randint(0,1)
        block = input("press b to block, it may not always work").upper()
        if block == "B" and block_chance == 1:
            time.sleep(2)
            print("Blocked!")
            print(f"""  Enemy Health = {enemy_health}
                    _____________________
                   |__________________|__|
                   Your health = {health}
            """)
        elif block == "B" and block_chance == 0:
             time.sleep(2)
             print("Block failed!")
             health = health - enemy_attack
             time.sleep(0.5)
             print("You got hit!")
             print(f"""  Enemy Health = {enemy_health}
                    _____________________
                   |_____________|_______|
                   Your health = {health}
            """)
        else:
            print("You must press b")
            while block != "B":
                block = input("press b to block, it may not always work").upper()
                
        if enemy_health == 0:
            time.sleep(1.5)
            print("You won!")
            reward_money = randint(20,260)
            gold_coins = reward_money + gold_coins
            print(f""" you got {gold_coins} gold coins!""")
            plain_forest()
            
        if health == 0:
            time.sleep(2)
            print(f""" you died! :( """)
            time.sleep(0.5)
            print(f"""dropped {gold_coins} gold coins""")
            print("respawning")
            time.sleep(3)
            atHome(0)
     
def forest(enemy_resistance,enemy_health,health,gold_coins):
    print("you enter the forest")
    forest_LVL1()
    skip = input()
    if skip == "skip fight":
        forest_Level_2(100,150) 
    print("you encounter the dragon!")
    time.sleep(1)
    print(f"""  Enemy Health = {enemy_health}
                _____________________
               |_____________________|
               Your health = {health}
        """)
    print("enemy also has 5 damage resistance with a 50% chance and 10 attack strength")
    forest_LVL1()
    fight(50,health,5,50,1)
    print("well done")#lvl 1  beginner fight
    forest_Level_2(100,gold_coins)
    

    
       
def town(gold_coins):
    time.sleep(1)
    bridge1()
    input()
    bridge2()
    input()
    bridge3()  #over the bridge
    input()
    plain_road()
    input()
    shop1()
    enter = input("Do you want to go inside this shop Y/N?").upper()
    if enter[0] == "Y":
        import ice_cream_shop
        print(" +1 icecream")
        print("-10 coins")
        gold_coins = gold_coins - 10
        item1 = "icecream"
        inventory.append(item1)
        plain_road()
        input()
        shop2()
        enter = input("Do you want to go inside this shop Y/N?").upper()#this is code to enter somewhere
        if enter[0] == "Y":
            import cupcake_factory
            print(" +1 cupcake")
            print("-10 coins")
            gold_coins = gold_coins - 10
            item2 = "cupcake"
            inventory.append(item2)
            plain_road()
            input()
            atHome(gold_coins)
            
        if enter[0] == "N":
            print("ok")
            plain_road()
            input()
            atHome(50)
                
           
    if enter[0] == "N":
        print("ok")
        plain_road()
        input()
        shop2()
        enter = input("Do you want to go inside this shop Y/N?").upper()#this is code to enter somewhere
        if enter[0] == "Y":
            import cupcake_factory
            print(" +1 cupcake")
            print("-10 coins")
            gold_coins = gold_coins - 10# adds cupcake to a list
            item2 = "cupcake"
            inventory.append(item2)
            plain_road()
            input()
            atHome(gold_coins)
            
        if enter[0] == "N":
            print("ok")
            plain_road()
            input()
            atHome(50)
        
def atHome(gold_coins):
    print("Welcome Home")
    insideHome()
    input()
    upstairs()# add functionality to intract with objects
    sleep = input("you can sleep in the bed Y/N").upper()
    if sleep[0] == "Y":
        upstairs_sleeping()
        stop = input("press enter to stop sleeping")
        if stop == "":
            upstairs()
            input()
            print("you open the chest")
            upstairs_chest()
            time.sleep(1)
            inventory.append("2x photos")
            inventory.append("5x berries")
            gold_coins = gold_coins + 50
            weapons["iron_sword"] = 10
            insideHome()
            choice = input("do you want to go to the forest or the town?")
            if choice == "town":
                town(50)
            if choice == "forest":
                forest(5,50,100,50)
    if sleep[0] == "N":
        print("you open the chest")
        time.sleep(1)
        upstairs_chest()
        inventory.append("2x photos")
        inventory.append("5x berries")
        gold_coins = gold_coins + 50
        weapons["iron_sword"] = 10 
        insideHome()
        choice = input("do you want to go to the forest or the town?")
        if choice == "town":
            town(50)
        if choice == "forest":
            forest(5,50,100,50)

            
            
global cavechoice
global health 
global enemy_health 
global enemy_resistance 
global gold_coins
            
print("______Trouble in Starville - the prequel to the 4 portals______")
time.sleep(1)
print("press enter to move around whenever you see a flashing cursor on its own")
time.sleep(2)
print("If the flashing cursor is at the end of text, read it and see what you have to do.")
time.sleep(2)
print("Don't rush into typing an answer; the game is coded to make realistic pauses whenever you do most things in game.")
print("A common example would be waiting for a character to speak")
time.sleep(1)
print(f""" Most importantly: have fun :)
   - The Dev """)
atHome(0)
