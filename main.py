
# ASCII Art Dungeon Room Creator	
import random

# Define lists of possible room elements
room_shapes = ["square", "rectangular", "circular", "irregular"]
room_sizes = ["small", "medium", "large"]
room_contents = ["empty", "treasure", "trap", "monster", "puzzle", "monument"]

monster_list = [
 "Beholder", "Dragon", "Goblin", "Orc", "Kobold", "Skeleton", "Zombie",
 "Giant", "Troll", "Gnoll", "Minotaur", "Mimic", "Otyugh", "Gargoyle",
 "Medusa", "Gorgon", "Harpy", "Basilisk", "Chimera", "Cockatrice",
 "Displacer Beast", "Griffon", "Hippogriff", "Manticore", "Wyvern",
 "Rust Monster", "Sahuagin", "Spectator", "Succubus/Incubus", "Umber Hulk",
 "Will-o'-Wisp", "Yuan-ti", "Aboleth", "Bulette", "Flumph", "Gelatinous Cube",
 "Intellect Devourer", "Nothic", "Rakshasa", "Roper", "Rust Monster", "Slaad",
 "Xorn", "Yeth Hound", "Zorn", "Flumph", "Gibbering Mouther", "Grimlock",
 "Hook Horror", "Mongrelfolk", "Quaggoth", "Shrieker", "Thri-Kreen"
]
treasure_list = ["magic item", "trinket", "gem", "weapon", "armor piece"]
puzzle_list = [
 "a mirror room", "a puzzle door", "some tiles on the floor",
 'some runes on the wall', 'an empty handed statue'
]
monument_list = [
 "an intact tomb", "a broken tomb", "a sculpted face in the wall",
 "a statue sculpted in the wall", "an intact obelisk", "a ruined obelisk",
 "a deity statue", " a fountain", "a greenish water fountain", "a totem"
]
trap_list = [
 'spikes on the floor', 'dragon heads in the walls', 'a trapdoor',
 'a pressure plate', 'sticky floor'
]
room_purpose = [
 'kitchen', 'dorm', 'barracks', 'praying room', 'portal room', 'library'
]

# Generate random room information
shape = random.choice(room_shapes)
size = random.choice(room_sizes)
content = random.choice(room_contents)

# Define room dimensions based on size

def mainloop():
	if size == "small":
		width = random.randint(5, 7)
		height = random.randint(5, 7)
	elif size == "medium":
		width = random.randint(8, 12)
		height = random.randint(8, 12)
	elif size == "large":
		width = random.randint(13, 20)
		height = random.randint(13, 20)

	# Define room borders based on shape
	if shape == "square":
		borders = ("+", "-", "+", "|", "|", "+", "-", "+")
	elif shape == "rectangular":
		borders = ("+", "-", "+", "|", "|", "+", "-", "+")
	elif shape == "circular":
		borders = (" ", "-", " ", "|", "|", " ", "-", " ")
	elif shape == "irregular":
		borders = (" ", "-", " ", "|", "|", " ", "-", " ")

	# Generate room layout
	room = []
	for i in range(height):
		row = []
		for j in range(width):
			if i == 0:
				if j == 0:
					row.append(borders[0])
				elif j == width - 1:
					row.append(borders[2])
				else:
					row.append(borders[1])
			elif i == height - 1:
				if j == 0:
					row.append(borders[5])
				elif j == width - 1:
					row.append(borders[7])
				else:
					row.append(borders[6])
			else:
				if j == 0 or j == width - 1:
					row.append(borders[3])
				else:
					row.append(" ")
		room.append(row)

	# Place content in room
	if content == "treasure":
		treasure_x = random.randint(1, width - 2)
		treasure_y = random.randint(1, height - 2)
		room[treasure_y][treasure_x] = "$"
	elif content == "trap":
		trap_x = random.randint(1, width - 2)
		trap_y = random.randint(1, height - 2)
		room[trap_y][trap_x] = "^"
	elif content == "monster":
		monster_x = random.randint(1, width - 2)
		monster_y = random.randint(1, height - 2)
		room[monster_y][monster_x] = "M"
	elif content == "puzzle":
		puzzle_x = random.randint(1, width - 2)
		puzzle_y = random.randint(1, height - 2)
		room[puzzle_y][puzzle_x] = "?"
	elif content == "monument":
		monument_x = random.randint(1, width - 2)
		monument_y = random.randint(1, height - 2)
		room[monument_y][monument_x] = "*"

	# Display room layout
	print("+" + "-" * width + "+")
	for row in room:
		print("|" + "".join(row) + "|")
	print("+" + "-" * width + "+")


	doors = random.randint(1, 4)
	room_height = random.randint(2, 7)
	rpr = random.choice(room_purpose)

 # printing stuff on screen
	print("----" * 10)
	print(f'the room is {size} and {shape}, it is {room_height}m tall')
	print(f'the seen room is a {rpr}')
	if doors == 1:
		print(f'the room has {doors} door')
	else:
		print(f'the room has {doors} doors')
	if rpr == 'portal room':
		portal = [
		'shadowfell',
		'feywild',
		'ethereal plane',
		'water plane',
		'fire plane',
		'earth plane',
		'wind plane',
		'Sigil, the city of doors',
		]
		port = random.choice(portal)
		print(f'the portal leads to {port}')

	# Printing the random contents onscreen
	if content == "monster":
		mon = random.choice(monster_list)
		print(f'you find a {mon}')
	elif content == "treasure":
		trs = random.randint(1, 25)
		trsi = random.choice(treasure_list)
		print(f'you find {trs} gold pieces and a {trsi} inside a small chest')
	elif content == "monument":
		mon = random.choice(monument_list)
		print(f'you see {mon} in the room')
	elif content == "puzzle":
		puz = random.choice(puzzle_list)
		print(f'you see {puz}, what can it be?')
	elif content == "trap":
		trp = random.choice(trap_list)
		if trp == 'sticky floor':
			print(f'the room has a sticky floor and a {mon}')
		print(f'you see {trp}')

 # Mainloop continuing
continue = str(input('Do you want to continue? [y/n]'))
if continue == 'y':
    mainloop()
    continue
else:
    print('Finishing Program')
    break
