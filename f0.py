sunflowers(Entities.Sunflower)

def sunflowers(type):

	goto(0,0)
	
	if not enoughForSeeds(type):
		return False
	
	waterAmount = enoughWater()	
	soil = needsSoil(type) 
	
	
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
		
	harvestSunflowers(fieldList)