def earth():
	directions = ["roll"]
	print("Roll for Earth phase?")
	userInput = ""
	while userInput not in directions:
		print("Options: roll")
		userInput = input()
		import random
		x = random.randint(1,6)
		print(x)
		if (x) == 1:
			print("Earthquake -10 food, -1 monk")
		if (x) == 2:
			print("Sinkhole -1 food, -1 monk")
		if (x) == 3:
			print("Calm +1 food")
		if (x) == 4:
			print("Sleepy no change")
		if (x) == 5:
			print("Tranquil +1 food")
		if (x) == 6:
			print("Fruitful (+5 food)")



print("Solarmonk")
print("Alice and Cheshire Cat stumble upon a monastery of Benedictine monks as they walk through a forest clearing. The monks do not know the way to the garden, but they are fascinated by its description, and plan to build their own one day. After a pleasant meal, Alice and Cheshire Cat continue on their way, and the monks continue their life of prayer and sustainable living. How long will they survive?")
print("It is the year of Our Lord 4073, and there are currently 50 monks and 50 food at the monastry")
directions = ["yes"]
print("Begin the first year?")
userInput = ""
while userInput not in directions:
	print("Options: yes")
	userInput = input()
	if userInput == "yes": earth()