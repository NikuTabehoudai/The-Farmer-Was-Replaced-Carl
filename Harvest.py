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

def harvestPumpkin():
	goto(0,0)
	while True:
		if get_entity_type() == None:
			while not can_harvest():
				plant(Entities.Pumpkin)
				use_item(Items.Fertilizer)
		
		if atTopRight():
			harvest()
			break
		moveNext()

def harvestCactus():
	goto(0,0)
	swapped = False
	wsl = get_world_size() -1
	while True:
		if measure() > measure(North) and not get_pos_y() == wsl:
			swap(North)
			swapped = True
		if measure() > measure(East) and not get_pos_x() == wsl:
			swap(East)
			swapped = True
			
		if atTopRight():
			if not swapped:
				break
			swapped = False
		moveNext()
	harvest()		