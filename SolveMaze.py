def solveMaze():
	directions = [North, East, South, West]
	index = 0
	
	while True:
		if get_entity_type() ==  Entities.Treasure:
			harvest()
			break
			
		if move(directions[(index -1 ) % 4]):
			index = (index -1) % 4
		else:
			if move(directions[index]) == False:
				move(directions[(index + 1) % 4])
				index = (index + 1) % 4