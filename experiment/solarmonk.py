def main():
    monks = 50
    food = 50
    
    while True:
        print(f"\nCurrent number of monks: {monks}")
        print(f"Current amount of food: {food}")
        
        directions = ["roll"]
        print("Roll for Earth phase of the year?")
        userInput = ""
        while userInput not in directions:
            print("Options: roll")
            userInput = input()
            import random
            x = random.randint(1,6)
            print(x)
            if (x) == 1:
                monks -= 1
                food -= 10
                print("Earthquake -10 food, -1 monk")
            if (x) == 2:
                monks -= 1
                food -= 1
                print("Sinkhole -1 food, -1 monk")
            if (x) == 3:
                food += 1
                print("Calm +1 food")
            if (x) == 4:
                print("Sleepy no change")
            if (x) == 5:
                print("Tranquil +1 food")
                food += 1
            if (x) == 6:
                food += 5
                print("Fruitful (+5 food)")
                
        print(f"\nCurrent number of monks: {monks}")
        print(f"Current amount of food: {food}")
                
        directions = ["roll"]
        print("Roll for Air phase of the year?")
        userInput = ""
        while userInput not in directions:
            print("Options: roll")
            userInput = input()
            import random
            x = random.randint(1,6)
            print(x)
            if (x) == 1:
                food -= 5
                print("Thunderstorms -5 food")
            if (x) == 2:
                monks -= 1
                print("Blizzards -1 monk")
            if (x) == 3:
                monks -= 1
                food -= 5
                print("Tornado -5 food, -1 monk")
            if (x) == 4:
                monks -= 1
                food -= 5
                print("Wildfires -5 food, -1 monk")
            if (x) == 5:
                food += 5
                print("Pleasant Breezes +5 food")
            if (x) == 6:
                monk += 1
                food += 5
                print("Balmy +5 food, +1 monk")
                
        print(f"\nCurrent number of monks: {monks}")
        print(f"Current amount of food: {food}")
        
        directions = ["roll"]
        print("Roll for Water phase of the year?")
        userInput = ""
        while userInput not in directions:
            print("Options: roll")
            userInput = input()
            import random
            x = random.randint(1,6)
            print(x)
            if (x) == 1:
                food += 5
                print("Gentle rains +5 food")
            if (x) == 2:
                food -= 5
                print("Heavy rains -5 food")
            if (x) == 3:
                food -= 15
                print("Flooding -15 food")
            if (x) == 4:
                food -= 10
                print("Drought -10 food")
            if (x) == 5:
                monks += 1
                food += 5
                print("Healthy rains +5 food, +1 monk")
            if (x) == 6:
                food += 1
                print("Average rains +1 food")
                
        print(f"\nCurrent number of monks: {monks}")
        print(f"Current amount of food: {food}")
        
        directions = ["roll"]
        print("Roll for Fire phase of the year?")
        userInput = ""
        while userInput not in directions:
            print("Options: roll")
            userInput = input()
            import random
            x = random.randint(1,6)
            print(x)
            if (x) == 1:
                monks -= 1
                food -= 5
                print("Extreme heat -5 food, -1 monk")
            if (x) == 2:
                print("Cool temperatures no change")
            if (x) == 3:
                food += 1
                print("Comfortable +1 food")
            if (x) == 4:
                food -= 5
                print("Temperate +5 food")
            if (x) == 5:
                print("Mild no change")
            if (x) == 6:
                monks -= 1
                food -= 1
                print("Extreme humidity -1 food, -1 monk")
                
        print(f"\nCurrent number of monks: {monks}")
        print(f"Current amount of food: {food}")
        
        directions = ["roll"]
        print("Roll for Ether phase of the year?")
        userInput = ""
        while userInput not in directions:
            print("Options: roll")
            userInput = input()
            import random
            x = random.randint(1,6)
            print(x)
            if (x) == 1:
                monks += 10
                food += 10
                print("Miracles +10 food, +10 monks")
            if (x) == 2:
                monks -= 5
                food -= 10
                print("War -10 food, -5 monks")
            if (x) == 3:
                monks -= 10
                food -= 10
                print("Plague -10 food, -10 monks")
            if (x) == 4:
                monks -= 1
                food -= 3
                print("Malaise -3 food, -1 monk")
            if (x) == 5:
                print("Neutral no change")
            if (x) == 6:
                monks += 3
                food += 3
                print("Satisfaction +3 food, +3 monks")
                
        print(f"\nCurrent number of monks: {monks}")
        print(f"Current amount of food: {food}")
        
        directions = ["roll"]
        print("Roll for new food this year?")
        userInput = ""
        while userInput not in directions:
            print("Options: roll")
            userInput = input()
            import random
            x = random.randint(2,12)
            food +=x
            print(x)
            
        print(f"\nCurrent number of monks: {monks}")
        print(f"Current amount of food: {food}")
        
        directions = ["roll"]
        print("Roll for new monks this year?")
        userInput = ""
        while userInput not in directions:
            print("Options: roll")
            userInput = input()
            import random
            x = random.randint(-5,5)
            monks +=x
            print(x)
            
                
print("Solarmonk")
print("Alice and Cheshire Cat stumble upon a monastery of Benedictine monks as they walk through a forest clearing. The monks do not know the way to the garden, but they are fascinated by its description, and plan to build their own one day. After a pleasant meal, Alice and Cheshire Cat continue on their way, and the monks continue their life of prayer and sustainable living. How long will they survive?")
print("It is the year of Our Lord 4073, and there are currently:")
directions = ["yes"]
print("View number of monks and food?")
userInput = ""
while userInput not in directions:
	print("Options: yes")
	userInput = input()
	if userInput == "yes": main()
