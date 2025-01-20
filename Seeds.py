def enoughForSeeds(type):
	fs = get_world_size() * get_world_size()
	if type == Entities.Carrot:
		cost = get_cost(type)
		if num_items(Items.Hay) > cost[Items.Hay] *  fs and num_items(Items.Wood) > cost[Items.Wood] * fs:
			return True
		return False
	
	if type == Entities.Sunflower:
		cost = get_cost(type)
		if num_items(Items.Carrot) > cost[Items.Carrot] *  fs:
			return True
		return False
		
	if type == Entities.Pumpkin:
		cost = get_cost(type)
		if num_items(Items.Carrot) > (cost[Items.Carrot] * fs) * 2:
			return True
		return False
		
	if type == Entities.Cactus:
		cost = get_cost(type)
		if num_items(Items.Pumpkin) > cost[Items.Pumpkin] * fs:
			return True
		return False
		
	if type == Entities.Treasure:
		if num_items(Items.Weird_Substance) > get_world_size() * num_unlocked(Unlocks.Mazes):
			return True
		return False
	
	if type == Items.Weird_Substance:
		if num_items(Items.Fertilizer) > fs * 2:
			return True
		return False
		
	return True