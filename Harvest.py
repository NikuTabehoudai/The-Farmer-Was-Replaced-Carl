def harvestField(type):
	goto(0,0)
	while True:
		harvestWait()
		
		if atTopRight():
			break
		moveNext()

def harvestSunflowers(unsortedList):
	while True:
		if can_harvest():
			break
	petals = 15
	sortedList = []
	while petals > 6:
		for i in unsortedList:
			if i[0] == petals:
				sortedList.append(i[1])
		petals = petals - 1
	
	for i in sortedList:
		goto(i[0],i[1])
		harvest()