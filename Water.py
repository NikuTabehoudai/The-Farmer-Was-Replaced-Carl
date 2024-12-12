def enoughWater():
	fs = get_world_size() * get_world_size()
	if num_items(Items.Water) >= fs * 4:
		return 4
	if num_items(Items.Water) >= fs * 3:
		return 3
	if num_items(Items.Water) >= fs * 2:
		return 2
	if num_items(Items.Water) >= fs:
		return 1
	return 0
	
def water(amount):
	i = 0
	while True: 
		if get_water() < 0.76:
			if i < amount:
				use_item(Items.Water)
				i= i + 1
			else:
				break
		else: 
			break
	