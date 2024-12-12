def field(type):
	goto(0,0)
	
	if not enoughForSeeds(type):
		return False
	
	waterAmount = enoughWater()	
	soil = needsSoil(type) 
	fieldList = []
	
	while True:	
		makeSoil(soil)
		if not type == Entities.Grass:
			water(waterAmount)
		if type == Entities.Tree:
			plantTrees()
		else:
			plant(type)
			if type == Entities.Sunflower:
				cords = get_pos_x(), get_pos_y()
				measured = measure(), cords
				fieldList.append(measured)
				
		if atTopRight():
			break
		moveNext()
	
	if type ==  Entities.Sunflower:
		harvestSunflowers(fieldList)
	elif type == Entities.Pumpkin:
		harvestPumpkin()
	else:
		harvestField(type)
		
