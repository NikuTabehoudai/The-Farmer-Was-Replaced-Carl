def field(type):
	goto(0,0)
	
	if not enoughForSeeds(type):
		return False
	
	if num_items(Items.Power) < 200 and type != Entities.Carrot and type != Entities.Sunflower:
		return False
	
	weird = False
	
	if type == Items.Weird_Substance:
		weird = True
		type = Entities.Cactus
		if not enoughForSeeds(type):
			return False
		
	waterAmount = enoughWater()	
	soil = needsSoil(type) 
	fieldList = []

	
	while True:	
		if type == Entities.Grass:
			if get_entity_type() == Entities.Grass:
				if atTopRight() or (atStart() and get_entity_type() == Entities.Grass):
					break
				moveNext()
				continue
				
		makeSoil(soil)
		

				
		
		if not type == Entities.Grass and not type == Entities.Cactus:
			water(waterAmount)			
			
		if type == Entities.Tree:
			plantTrees()
		else:
			plant(type)
			if weird:
				use_item(Items.Fertilizer)
				
			if type == Entities.Sunflower:
				cords = get_pos_x(), get_pos_y()
				measured = measure(), cords
				fieldList.append(measured)
				
		if atTopRight():
			break
		moveNext()
	
	if type == Entities.Sunflower:
		harvestSunflowers(fieldList)
	elif type == Entities.Pumpkin:
		harvestPumpkin()
	elif type ==  Entities.Cactus:
		harvestCactus()
	else:
		harvestField(type)
		
