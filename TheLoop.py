def theLoop(power, carrot,wood,hay):
	while theLoopCheck(power, carrot,wood,hay):
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