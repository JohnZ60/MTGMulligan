"""
open-mtg MIT license granted by Hylnur Davíð Hlynsson for simulating the game (https://github.com/hlynurd/open-mtg)
Original simulator coded by Hylnur and Erik Martinez, deck.py modified by Alexander Mains
"""

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

def get_RDW_deck():
    decklist = []
    decklist.append(cards.Creature('Fervent Champion', "Human Knight", {'Red': 1, 'Generic': 0}, 1, 1, 'First strike, haste \nWhenever Fervent Champion attacks, another target attacking Knight you control gets +1/+0 until end of turn. \nEquip abilities you activate that target Fervent Champion cost 3 less to activate.\n'))
    decklist.append(cards.Creature('Scorch Spitter', 'Elemental Lizard', {'Red': 1, 'Generic': 0}, 1, 1, 'Whenever Scorch Spitter attacks, it deals 1 damage to the player or planeswalker it\'s attacking.'))
    decklist.append(cards.Creature('Robber of the Rich', 'Human Archer Rogue', {'Red': 1, 'Generic': 1}, 2, 2, 'Reach, haste\nWhenever Robber of the Rich attacks, if defending player has more cards in hand than you, exile the top card of their library. \nDuring any turn you attacked with a Rogue, you may cast that card and you may spend mana as though it were mana of any color to cast that spell.'))
    decklist.append(cards.Creature('Runaway Steam-Kin', 'Elemental',{'Red': 1, 'Generic': 1}, 1, 1, "Whenever you cast a red spell, if Runaway Steam-Kin has fewer than three +1/+1 counters on it, put a +1/+1 counter on Runaway Steam-Kin.\nRemove three +1/+1 counters from Runaway Steam-Kin: Add ."))
    decklist.append(cards.Creature('Anax, Hardened in the Forge', 'Demigod', {'Red': 2, 'Generic': 1}, 0, 3, "Legendary\n Enchantment\n Anax's power is equal to your devotion to red. (Each Red in the mana costs of permanents you control counts toward your devotion to red.)Whenever Anax or another nontoken creature you control dies, create a 1/1 red Satyr creature token with 'This creature can't block.' If the creature had power 4 or greater, create two of those tokens instead."))
    decklist.append(cards.Creature('Bonecrusher Giant', 'Giant',{'Red': 1, 'Generic': 2}, 4, 3, "Stomp 1R: Instant - Adventure: Damage can't be prevented this turn. Stomp deals 2 damage to any target/Whenever Bonecrusher Giant becomes the target of a spell, Bonecrusher Giant deals 2 damage to that spell's controller."))
    decklist.append(cards.Creature('Torbran, Thane of Red Fell', 'Dwarf Noble',{'Red': 3, 'Generic': 1}, 2, 4, "If a red source you control would deal damage to an opponent or a permanent an opponent controls, it deals that much damage plus 2 instead."))
    decklist.append(cards.Artifact('Embercleave', 'Equipment' ,{'Red': 1, 'Generic': 0}, "Flash\nThis spell costs 1 less to cast for each attacking creature you control.\nWhen Embercleave enters the battlefield, attach it to target creature you control.\nEquipped creature gets +1/+1 and has double strike and trample.\nEquip 3 "))
    decklist.append(cards.Land('Castle Embereth', 'Land', '', [lambda self: self.owner.add_mana({"Red": 1}), "Castle Embereth enters the battlefield tapped unless you control a Mountain.Tap: Add R,  1RRTAP: Creatures you control get +1/+0 until end of turn."]))
    for i in range(1,16):
        decklist.append(cards.Land("Mountain", "Basic Land", "Mountain", [lambda self: self.owner.add_mana({"Red": 1})]))
    for i in ['Hearts', 'Clubs', 'Diamonds']: #count to 3
        decklist.append(cards.Creature('Fervent Champion', "Human Knight", {'Red': 1, 'Generic': 0}, 1, 1, 'First strike, haste \nWhenever Fervent Champion attacks, another target attacking Knight you control gets +1/+0 until end of turn. \nEquip abilities you activate that target Fervent Champion cost 3 less to activate.\n'))
        decklist.append(cards.Creature('Scorch Spitter', 'Elemental Lizard', {'Red': 1, 'Generic': 0}, 1, 1, 'Whenever Scorch Spitter attacks, it deals 1 damage to the player or planeswalker it\'s attacking.'))
        decklist.append(cards.Creature('Rimrock Knight', 'Dwarf Knight', {'Red': 1, 'Generic': 1}, 3, 1, 'Adventure - Instant R : Target Creature gets +2/+0 until end of turn,\n Rimrock Knight can\'t block.'))
        decklist.append(cards.Creature('Robber of the Rich', 'Human Archer Rogue', {'Red': 1, 'Generic': 1}, 2, 2, 'Reach, haste\nWhenever Robber of the Rich attacks, if defending player has more cards in hand than you, exile the top card of their library. \nDuring any turn you attacked with a Rogue, you may cast that card and you may spend mana as though it were mana of any color to cast that spell.'))
        decklist.append(cards.Creature('Runaway Steam-Kin', 'Elemental',{'Red': 1, 'Generic': 1}, 1, 1, "Whenever you cast a red spell, if Runaway Steam-Kin has fewer than three +1/+1 counters on it, put a +1/+1 counter on Runaway Steam-Kin.\nRemove three +1/+1 counters from Runaway Steam-Kin: Add ."))
        decklist.append(cards.Creature('Anax, Hardened in the Forge', 'Demigod', {'Red': 2, 'Generic': 1}, 0, 3, "Legendary\n Enchantment\n Anax's power is equal to your devotion to red. (Each Red in the mana costs of permanents you control counts toward your devotion to red.)Whenever Anax or another nontoken creature you control dies, create a 1/1 red Satyr creature token with 'This creature can't block.' If the creature had power 4 or greater, create two of those tokens instead."))
        decklist.append(cards.Creature('Bonecrusher Giant', 'Giant',{'Red': 1, 'Generic': 2}, 4, 3, "Stomp 1R: Instant - Adventure: Damage can't be prevented this turn. Stomp deals 2 damage to any target/Whenever Bonecrusher Giant becomes the target of a spell, Bonecrusher Giant deals 2 damage to that spell's controller."))
        decklist.append(cards.Creature('Torbran, Thane of Red Fell', 'Dwarf Noble',{'Red': 3, 'Generic': 1}, 2, 4, "If a red source you control would deal damage to an opponent or a permanent an opponent controls, it deals that much damage plus 2 instead."))
        decklist.append(cards.Artifact('Embercleave', 'Equipment' ,{'Red': 1, 'Generic': 0}, "Flash\nThis spell costs 1 less to cast for each attacking creature you control.\nWhen Embercleave enters the battlefield, attach it to target creature you control.\nEquipped creature gets +1/+1 and has double strike and trample.\nEquip 3 "))
        decklist.append(cards.Sorcery('Claim the Firstborn', '', {'Red': 1, 'Generic': 0}, "Gain control of target creature with converted mana cost 3 or less until end of turn. Untap that creature. It gains haste until end of turn."))
        decklist.append(cards.Land('Castle Embereth', 1, '', [lambda self: self.owner.add_mana({"Red": 1}), "Castle Embereth enters the battlefield tapped unless you control a Mountain.Tap: Add R,  1RRTAP: Creatures you control get +1/+0 until end of turn."]))
        decklist.append(cards.Land("Mountain", "Basic Land", "Mountain", [lambda self: self.owner.add_mana({"Red": 1})]))