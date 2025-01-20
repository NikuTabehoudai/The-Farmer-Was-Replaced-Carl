def dynamic_targets():

	targets = {}
	targets[Items.Hay] = 2000
	targets[Items.Wood] = 2000
	targets[Items.Carrot] = 2000
	targets[Items.Pumpkin] = 2000
	targets[Items.Cactus] = 2000
	targets[Items.Gold] = 2000
	targets[Items.Bone] = 2000
	targets[Items.Power] = 2000
	targets[Items.Fertilizer] = 2000
	targets[Items.Weird_Substance] = 2000
	
	#targets = add_cost(targets, get_cost(Unlocks.Fertilizer))
	#targets = add_cost(targets, get_cost(Unlocks.Cactus))
	#targets = add_cost(targets, get_cost(Unlocks.Dinosaurs))
	#targets = add_cost(targets, get_cost(Unlocks.Mazes))
	#targets = add_cost(targets, get_cost(Unlocks.Polyculture))
	
	targets = add_cost(targets, get_cost(Unlocks.Leaderboard))
	
	return targets
	
def add_cost(targetdict, cost):
	for item in cost:
		targetdict[item] = targetdict[item] + cost[item]

	return targetdict



