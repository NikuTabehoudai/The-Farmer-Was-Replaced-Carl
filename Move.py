def moveNext():
	wc = get_world_size() - 1
	if get_pos_y() == wc:
		move(North)
		move(East)
	else:
		move(North)
		
def goto(x, y):
    yDist = get_pos_y() - y
    xDist = get_pos_x() - x
    halfWorldSize = get_world_size()/2
    while get_pos_y() != y:
        if yDist >= halfWorldSize or (-halfWorldSize <= yDist and yDist < 0):
            move(North)
        else:
            move(South)
    while get_pos_x() != x:
        if xDist >= halfWorldSize or (-halfWorldSize <= xDist and xDist < 0):
            move(East)
        else:
            move(West)
            
def goto_d(x,y):
	while y != get_pos_y():
		if y > get_pos_y():
			if not move(North):
				return False
		if y < get_pos_y():
			if not move(South):
				return False
				
	while x != get_pos_x():
		if x > get_pos_x():
			if not move(East):
				return False
		if x < get_pos_x():
			if not move(West):
				return False
	
	return True

def goto_c(x,y):		
	while x != get_pos_x():
		if x > get_pos_x():
			if not move(East):
				return False
		if x < get_pos_x():
			if not move(West):
				return False
				
	while y != get_pos_y():
		if y > get_pos_y():
			if not move(North):
				return False
		if y < get_pos_y():
			if not move(South):
				return False
				
				
	
	return True