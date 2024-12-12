def plantTrees():
	if even(get_pos_x()):
		if even(get_pos_y()):
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
	if not even(get_pos_x()):
		if not even(get_pos_y()):
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)