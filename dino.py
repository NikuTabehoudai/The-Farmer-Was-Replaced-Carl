def dino():
	goto(0,0)
	change_hat(Hats.Dinosaur_Hat)
	while True:
		next = measure()
		if not goto_d(next[0],next[1]):
			if not goto_c(next[0], next[1]):
				break

					
	change_hat(Hats.Dinosaur_Hat)