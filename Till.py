def needsSoil(type):
	if type == Entities.Carrot:
		return True
	
	if type == Entities.Sunflower:
		return True
		
	if type == Entities.Pumpkin:
		return True
	
	if type == Entities.Cactus:
		return True
	
	if type == Entities.Grass:
		return False

def makeSoil(soil):
	if soil:
		if get_ground_type() == Grounds.Grassland:
			till()
	elif soil == False:
		if get_ground_type() == Grounds.Soil:
			till()