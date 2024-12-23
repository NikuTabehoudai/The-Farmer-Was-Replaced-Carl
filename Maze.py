def maze():
	if not enoughForSeeds(Entities.Treasure):
		return False
	
	ws = get_world_size()
	if not even(ws):
		ws -=1
	goto(ws / 2, ws / 2)
		
	makeSoil(True)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, get_world_size() * num_unlocked(Unlocks.Mazes))
	solveMaze()