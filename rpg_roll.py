import random
import rpg_character
import rpg

async def roll(sender, channel, reroll) -> str:
	owner = sender


	race = get_race()
	klass = get_klass()
	alignment = get_alignment()
	strength = random.randint(1,20)
	dexterity = random.randint(1,20)
	constitution = random.randint(1,20)
	intelligence = random.randint(1,20)
	wisdom = random.randint(1,20)
	charisma = random.randint(1,20)
	charname = randomName(race)

	await rpg_character.addCharacter(owner, channel, race, klass, alignment, strength, dexterity, constitution, intelligence, wisdom, charisma, charname)

def get_race() -> str:
	races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Human", "Tiefling"]

	return random.choice(races)

def get_klass() -> str:
	klasser = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

	return random.choice(klasser)

def get_alignment() -> str:
	alignments = [
		"Lawful Good", "Neutral Good", "Chaotic Good",
		"Lawful Neutral", "True Neutral", "Chaotic Neutral",
		"Lawful Evil", "Neutral Evil", "Chaotic Evil"
	]
	return random.choice(alignments)

def modifier(roll) -> str:
	mod = int(roll/2-5)

	if mod == 0:
		pos = "+"
	elif mod > 0:
		pos = "+"
	else:
		pos = ""

	return "(" + pos + str(mod) + ")"

def print_stat(name, stat) -> str:
	return name + ": " + str(stat).ljust(2) + " - " + modifier(stat)

def randomName(race) -> str:
	firsts = {
		"Human": 
			["Jake","Jim","Carl","Roberto","Julius","Donald", "Harris", "Carlos", "Strongman", "Wilhelm", "Adolf", "Knut", "Kenneth", "Ian", "Mofo", "Bajsmannen", "Boppe", "Pepe", "Frank", "Tintin", "Franco", "Ralf", "Romeo", "Peder", "Jerry", "Otto", "Kent", "Dick", "Kawa", "Marre", "Edvard", "Nils", "Teodor", "Daniel", "Ale"],
		"Elf":
			["Caramellio", "Sebasthyon", "Legolas", "Nilsolas", "Tristan", "Fentanyl", "Citrus", "Alvedon", "Silvbert", "Linux", "Marzipanius"],
		"Halfling":
			["Frodo", "Grodo", "Melvin", "Mapp", "Bilf", "Grogu", "Merry", "Perry", "Pippin", "Sam", "Bongo", "Snoddas", "Bingo", "Milf"],
		"Half-Orc":
			["Boby", "Fucker", "Micke", "Garg", "Raaagghhhh", "Normalo"],
		"Dwarf":
			["Micke", "Runko", "Gimli", "Osvaldo", "Fernando", "Julio", "Antonio", "Damp"],
		"Dragonborn":
			["Drake", "Draco", "Draken", "Sv??rmor", "Exfru", "Nalxestuandor", "Naloxone", "Oxycontin", "Dinosaurius"],
		"Tiefling":
			["Tiefan", "Moronius", "Dumbassus", "Suckadickir", "Horny"],
		"Half-Elf":
			["Lolo"],
		"Gnome":
			["Liten", "Lille", "Mini", "Smutser", "Toker", "Plutten", "Slimp", "Dorkus"],
		"Troll":
			["Michael"],
		"Goblin":
			["Teodor"],
		"Skribent":
			["Michael", "Edvard", "Owe", "Gunnar", "B??rge", "Anders", "Gr??ger", "Knut", "G??ran", "Wilhelm von", "P-e-O", "Paul \"Bingo\"", "Otto", "??khe", "Golf", "Lehnart", "Cleo", "Karl-Teodor", "\"M\"", "Rudolf", "J??ran", "Hjohn"]
	}
	lasts = {
		"Human": 
			["Anderson", "Rogers", "Harris", "Hard", "Brown", "Hardbody", "Buff", "Bajs", "H??st", "Kill", "Fighter", "Weedsmoker", "Weed", "Grill", "Fuckington", "L??fv??n", "Storkuk", "Snopp", "Keatington", "Travolta", "Pitt", "Hitler"],
		"Elf":
			["Fj??rilsdr??m", "Kokos", "Orb", "Sybian", "Gyllenkuk", "Tampong", "Kretinius"],
		"Halfling":
			["Baggins", "Froggy", "Cruddy", "Gump", "Blob", "Gamgee", "R??kstr??m", "Bongo", "Muffins", "Dolme" ],
		"Half-Orc":
			["Kokos", "Gruff", "Bajs", "Sten", "R??v", "Turd", "Gurk", "Burk", ],
		"Dwarf":
			["Mongo", "L??fv??n", "Storkuk", "Dv??rgsson", "Llorente", "Torres", "Alba", "Banderas"],
		"Dragonborn":
			["Draksson", "Drakonius", "Drakstr??m", "Skalman", "Weedburner", "Assfucker", "Thongsong"],
		"Tiefling":
			["Tiefsson", "Meurling", "Chingy", "DemoniusX", "Joker", "Slok", "Skurk"],
		"Half-Elf":
			["Moce", "Plam"],
		"Gnome":
			["R??v", "N??t", "Task", "Boll", "Pinne", "R??vpillare", "Lol", "Keso", "Banan", "Sniglet", "Groda", "Mini"],
		"Troll":
			["Andersson"],
		"Goblin":
			["Meurling"],
		"Skribent":
			["Andersson", "Ekstr??m", "Svenson", "Nilsson", "Karlstr??m", "Wir??n", "Bergstr??m-Nyl??n", "H Pettersson", "Janzon", "Bred??ng", "Sportelius", "Bengt??n", "??rixon", "Kranstr??mer", "Brom??n", "Lindberg-Berglind", "Maxzelius", "P-son"]
	}

	first = firsts[race]
	last = lasts[race]

	if race == "Half-Elf":
		if random.choice([True, False]):
			first.extend(firsts["Human"])
			last.extend(lasts["Elf"])
		else:
			first.extend(firsts["Elf"])
			last.extend(lasts["Human"])
	elif race == "Half-Orc":
		if random.choice([True, False]):
			first.extend(firsts["Human"])
			last.extend(lasts["Halfling"])
		else:
			first.extend(firsts["Halfling"])
			last.extend(lasts["Human"])
	elif race == "Goblin":
		if random.choice([True, False]):
			first.extend(firsts["Gnome"])
			last.extend(lasts["Dwarf"])
		else:
			first.extend(firsts["Dwarf"])
			last.extend(lasts["Gnome"])

	name = random.choice(first) + " " + random.choice(last)
	
	return name