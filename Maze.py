def maze():
	if not enoughForSeeds(Entities.Treasure):
		break
	
	ws = get_world_size()
	if not even(ws):
		ws -=1
	goto(ws / 2, ws / 2)
		
	makeSoil(True)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, ws * 2)
	solveMaze()