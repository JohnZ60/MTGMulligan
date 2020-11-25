import cards


def get_bear_wars_deck():
    decklist = []
    for i in range(12):
        decklist.append(cards.Creature("Grizzly Bears 1", "bear", {'Green': 3, 'Generic': 0}, 3, 1))
        decklist.append(cards.Creature("Grizzly Bears 2", "bear", {'Green': 3, 'Generic': 0}, 4, 1))
        decklist.append(cards.Creature("Grizzly Bears 3", "bear", {'Green': 3, 'Generic': 0}, 5, 1))
        decklist.append(cards.Creature("Grizzly Bears 4", "bear", {'Green': 3, 'Generic': 0}, 6, 1))
        decklist.append(cards.Creature("Grizzly Bears 5", "bear", {'Green': 3, 'Generic': 0}, 7, 1))
        decklist.append(cards.Land("Forest", "Basic Land", "Forest", [lambda self: self.owner.add_mana({"Green": 1})]))
        decklist.append(cards.Land("Taiga", "Land", "Mountain Forest", [lambda self: self.owner.add_mana({"Green": 1}),
                                                                        lambda self: self.owner.add_mana({"Red": 1})]))
    return decklist


def get_8ed_core_gold_deck():
    decklist = []
    for i in range(8):  # (8):
        decklist.append(
            cards.Land("Mountain", "Basic Land", "Mountain", [lambda self: self.owner.add_mana({"Red": 1})]))
    for i in range(7):  # (7):
        decklist.append(cards.Land("Forest", "Basic Land", "Forest", [lambda self: self.owner.add_mana({"Green": 1})]))
    for i in range(2):
        decklist.append(cards.Creature("Norwood Ranger", "Elf Scout", {'Green': 1}, 1, 2))
        decklist.append(cards.Sorcery("Lava Axe", "", {'Red': 1, 'Generic': 4}))
        decklist.append(cards.Creature("Grizzly Bears", "Bear", {'Green': 1, 'Generic': 1}, 2, 2))
        decklist.append(cards.Creature("Enormous Baloth", "Beast", {'Green': 1, 'Generic': 6}, 7, 7))
        decklist.append(cards.Creature("Goblin Raider", "Goblin Warrior", {'Red': 1, 'Generic': 1}, 2, 2, True))
        decklist.append(cards.Creature("Hill Giant", "Giant", {'Red': 1, 'Generic': 3}, 3, 3))
        decklist.append(cards.Sorcery("Volcanic Hammer", "", {'Red': 1, 'Generic': 1}))
    for i in range(1):
        decklist.append(cards.Creature("Spined Wurm", "Wurm", {'Green': 1, 'Generic': 4}, 4, 3))
        decklist.append(cards.Creature("Ogre Taskmaster", "Ogre", {'Red': 1, 'Generic': 3}, 4, 3, True))
        decklist.append(cards.Sorcery("Stone Rain", "", {'Red': 1, 'Generic': 2}))
        decklist.append(cards.Sorcery("Rampant Growth", "", {'Green': 1, 'Generic': 1}))
    return decklist


def get_8ed_core_silver_deck():
    decklist = []
    for i in range(8):
        decklist.append(cards.Land("Plains", "Basic Land", "Plains", [lambda self: self.owner.add_mana({"White": 1})]))
    for i in range(7):
        decklist.append(cards.Land("Island", "Basic Land", "Island", [lambda self: self.owner.add_mana({"Blue": 1})]))
    for i in range(4):
        decklist.append(cards.Creature("Glory Seeker", "Human Soldier", {'White': 1, 'Generic': 1}, 2, 2))
    for i in range(3):
        decklist.append(cards.Creature("Giant Octopus", "Octopus", {'Blue': 1, 'Generic': 3}, 3, 3))
    for i in range(2):
        decklist.append(cards.Creature("Coral Eel", "Eel", {'Blue': 1, 'Generic': 1}, 2, 1))
        decklist.append(cards.Creature("Vizzerdrix", "Beast", {'Blue': 1, 'Generic': 6}, 6, 6))
        decklist.append(cards.Sorcery("Sacred Nectar", "", {'White': 1, 'Generic': 1}))
        decklist.append(cards.Sorcery("Vengeance", "", {'White': 1, 'Generic': 1}))
    for i in range(1):
        decklist.append(cards.Creature("Eager Cadet", "Human Soldier", {'White': 1, 'Generic': 0}, 1, 1))
        decklist.append(cards.Creature("Fugitive Wizard", "Human Wizard", {'Blue': 1, 'Generic': 0}, 1, 1))
        decklist.append(cards.Sorcery("Index", "", {'Blue': 1, 'Generic': 0}))
    return decklist
