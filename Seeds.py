def enoughForSeeds(type):
	fs = get_world_size() * get_world_size()
	if type == Entities.Carrot:
		if num_items(Items.Hay) > fs and num_items(Items.Wood) > fs:
			return True
		return False
	
	if type == Entities.Sunflower:
		if num_items(Items.Carrot) > fs:
			return True
		return False
		
	if type == Entities.Pumpkin:
		if num_items(Items.Carrot) > fs:
			return True
		return False
		
	return True