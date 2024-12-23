def harvestWait():
	while True:
		if can_harvest():
			harvest()
			break

def even(int):
	if int % 2 == 0:
		return True
	return False

def enoughItems(item, target):
	if num_items(item) < target:
		return False
	return True
	
def theLoopCheck(gold, cactus, pumpkin, power, carrot, wood, hay):
	if enoughItems(Items.Gold, gold):
		if enoughItems(Items.Cactus, cactus):
			if enoughItems(Items.Pumpkin, pumpkin):
				if enoughItems(Items.Power, power):
					if enoughItems(Items.Carrot, carrot):
						if enoughItems(Items.Wood, wood):
							if enoughItems(Items.Hay, hay):
								return False
	return True