def theLoop(weird, bone, gold, cactus, pumpkin, power, carrot, wood, hay):
	while theLoopCheck(weird, bone, gold, cactus, pumpkin, power, carrot, wood, hay):
		while num_items(Items.Power) < power:
			if field(Entities.Sunflower) == False:
				break
				
		while num_items(Items.Carrot) < carrot:
			unlock(Unlocks.Pumpkins)
			if field(Entities.Carrot) == False:
				break
				
		
		while num_items(Items.Bone) < bone:
			if stupid_snek()== False:
				break
		
		while num_items(Items.Weird_Substance) < weird:
			if field(Items.Weird_Substance) == False:
				break
		
		while num_items(Items.Gold) < gold:
			if maze() ==  False:
				break
			
		while num_items(Items.Cactus) < cactus:
			unlock(Unlocks.Speed)
			if field(Entities.Cactus) == False:
				break
				
		while num_items(Items.Pumpkin) < pumpkin:
			if field(Entities.Pumpkin) == False:
				break

		while num_items(Items.wood) < wood:
			field(Entities.Tree)
			unlock(Unlocks.Carrots)
		
		while num_items(Items.Hay) < hay:
			field(Entities.Grass)
			unlock(Unlocks.Grass)
			unlock(Unlocks.Trees)
			
			