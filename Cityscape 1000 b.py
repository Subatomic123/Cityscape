import random

state = {
"premium": False,
"instantbuilding": False,
"nodisasters": False

}

print("""
==========
|  Cityscape  |
==========""")

global name
name = 0
cash = 1000
turn = 1
diamonds = 10
happiness = 50
trust = 50
ver = 1000
population = 100
offices = 1
income = 100
buildings = 1
houses = 1
complexes = 0
villas = 0
boost = 10
inst = 25
prem = 50
dis = 75
jobs = 2

name_random = ["Theocity", "Syland", "Meotown", "Espertino", "York", "Sylv", "Union of districts", "Tillcity", "Poh", "Feehu", "Tikuve"]



choose = input("Random or custom name?")
if "Random" in choose or "1" in choose or "random" in choose or "RANDOM" in choose:
    name = random.choice(name_random)
if "custom" in choose or "Custom" in choose or "CUSTOM" in choose or "2" in choose:
    name1 = input("Name your city:")
    name = name1
if name == 0:
    name = random.choice(name_random)
    
print(f"Welcome to Cityscape {ver}! This is the {name} city. Your city is at turn {turn}. you have ${cash} and ◇{diamonds} diamonds. Your citizens don't really trust you yet, however your trust grows overtime. You're at {population} population.")


def mayor_guide():
    print(f"""
    
    Hello, Mayor of {name}! This is the mayor's guide! Here, you can find information on buildings and your city! for general information about {name}, you should type 'City Information Center' instead, or what i like to call it, the 'CIC.' Building information is here below:
        
        
        Houses: $80, increases trust by 2, and increases population by 4 per house, increases happiness by 6
        
        Offices: $50, Increases trust by 4, and increases population by 1, also increases jobs by 1. Increases happiness by 2.
        
        
        
        
        Good luck, Mayor!
        Sincerely,
        Team Quick
        
        
        
        """)




def shop():
    global diamonds
    print("Type 'exit' to exit")
    print("""1. Instant building (◇25 diamonds)
    2. Premium (◇50 diamonds)
    3. No Disasters (◇75 Diamonds)""")
    print("What would you like to buy?\n")
    while True:
        buy = input("")
        if "1." in buy or "1" in buy or "Instant" in buy or "Instant building" in buy or "building" in buy:
            if diamonds < 25:
                print(f"Insufficient balance! you have ◇{diamonds} and the item you were trying to buy is ◇25!")
            if diamonds >= 25:
                diamonds -= inst
                print(f"You bought it! You now have ◇{diamonds} diamonds and the item was $25")
        

while True:
    term = input(f"You have ${cash} and {population} people, what would you like to build? or would you like to go to the shop? if you don't know what to build, look at the mayor's guide by typing 'tutorials'  ")
    if term.lower() == "tutorials":
        mayor_guide()
    if term.lower() == "shop":
        shop()
    if term.lower() == "house":
        global amount
        amount = 0
        try:
            amount = int(input("How much would you like to build? for prices, we recommend looking at mayor's guide by typing 'tutorials'"))
        except ValueError:
            print("digits only")
        price = 80
        price += amount
        houses += amount
        population += 5 * amount
        trust += 2 * amount
        if cash >= price:
            print(f"You bought it! You now have {population} population and you have {income} income and {trust} trust!")
            
    if term.lower() == "office":
        try:
            amount = int(input("How much would you like to build? for prices we recommend looking at mayor's guide by typing 'tutorials.'"))
        except ValueError:
                print("digits only")
        price = 50
        price *= amount
        offices += amount
        if cash >= price:
            cash -= price
            happiness += 2 * amount
            trust += 4 * amount
            jobs += 3 * amount
            if jobs > population:
                jobs = population =- 1
            income += offices
            print(f"You now have {offices} offices! You now have ${cash}, your income is now {income} per turn! Your citizen happiness is now {happiness}.")
            continue
        if cash <= price:
            print(f"You don't have enough balance, you only have ${cash} and the cost is ${price}!")
    cash += income
    print(f"you have ${cash} this turn")