def thaLoop():
	while True:
		targets = dynamic_targets()
		if thaLoopCheck(targets):
			break
		
		while num_items(Items.Hay) < targets[Items.Hay]:
			if field(Entities.Grass) == False:
				break
		
		while num_items(Items.Wood) < targets[Items.Wood]:
			if field(Entities.Tree) == False:
				break
			
		while num_items(Items.Power) < targets[Items.Power]:
			if field(Entities.Sunflower) == False:
				break
		
		while num_items(Items.Carrot) < targets[Items.Carrot]:
			if field(Entities.Carrot) == False:
				break
		
		while num_items(Items.Pumpkin) < targets[Items.Pumpkin]:
			if field(Entities.Pumpkin) == False:
				break
									
		while num_items(Items.Cactus) < targets[Items.Cactus]:
			if field(Entities.Cactus) == False:
				break
		
		while num_items(Items.Gold) < targets[Items.Gold]:
			if maze() ==  False:
				break
		
		while num_items(Items.Bone) < targets[Items.Bone]:
			if stupid_snek() == False:
				break
						
		while num_items(Items.Weird_Substance) < targets[Items.Weird_Substance]:
			if field(Items.Weird_Substance) == False:
				break
				
		unlocking()