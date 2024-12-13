def theLoop(cactus, pumpkin, power, carrot, wood, hay):
	while theLoopCheck(cactus, pumpkin, power, carrot, wood, hay):
		while num_items(Items.Cactus) < cactus:
			if field(Entities.Cactus) == False:
				break
				
		while num_items(Items.Pumpkin) < pumpkin:
			if field(Entities.Pumpkin) == False:
				break
		
		while num_items(Items.Power) < power:
			if field(Entities.Sunflower) == False:
				break
						
		while num_items(Items.Carrot) < carrot:
			if field(Entities.Carrot) == False:
				break
		
		while num_items(Items.wood) < wood:
			field(Entities.Tree)
		
		while num_items(Items.Hay) < hay:
			field(Entities.Grass)