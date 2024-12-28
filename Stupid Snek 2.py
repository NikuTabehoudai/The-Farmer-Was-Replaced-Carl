def stupid_snek():
	goto(0,0)
	change_hat(Hats.Dinosaur_Hat)
	if num_items(Items.Pumpkin) < 200:
		return False
	while True:
		if not goto_c(0,9):
			break
		if not goto_c(1,1):
			break
		if not goto_c(2,9):
			break
		if not goto_c(3,1):
			break
		if not goto_c(4,9):
			break
		if not goto_c(5,1):
			break
		if not goto_c(6,9):
			break
		if not goto_c(7,1):
			break
		if not goto_c(8,9):
			break
		if not goto_c(9,0):
			break
		if not goto_c(0,0):
			break
	change_hat(Hats.Straw_Hat)