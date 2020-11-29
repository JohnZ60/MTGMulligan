
from cards import Card, Sorcery, Creature, Land
import copy

mana_colors_to_types = {"White": "Plains", "Blue": "Island", "Black": "Swamp", "Red": "Mountain", "Green": "Forest"}
mana_have = {}
mana_need = {}
mana_left = {}
hand_number = 1

def initialize_mana_dicts(): #DONE
    for each in mana_colors_to_types:
        mana_have[mana_colors_to_types[each]] = 0
        mana_need[each] = 0
    mana_need["Generic"] = 0
    mana_need["Colorless"] = 0

def determine_weights_of_cards_in_hand():
    print("determining weights")
    
    
def assess_rest_of_deck():
    print("assessing rest of deck")

def have_enough_mana_for_card(card):
    print("has enough mana?")
    for mana_type in card.mc:
        if mana_left[mana_type] < card.mc[mana_type]:
            return False
    return True

def take_mana_from_mana_dict():
    print("taking mana from mana list")
    
def assess_starting_hand(hand):
    initialize_mana_dicts()
    
    print(mana_have)
    print(mana_need)
    print("assessing starting hand")
    print(len(hand))
    print(hand)
    for card in hand:
        if isinstance(card, Land):
            mana_have[card.subtypes] += 1
            card.value_in_hand = mana_have[card.subtypes] #temp value only used for hand evaluation
    mana_left = copy.deepcopy(mana_have)        
    for card in hand: # iterates twice bc we need the amount of land to 
                      #determine value of other cards
        if isinstance(card, Creature) or isinstance(card, Sorcery):
            for mana_type in card.mc:
                card.total_mc += card.mc[mana_type] 
                mana_need[mana_type] += card.mc[mana_type]
            if card.total_mc == hand_number and have_enough_mana_for_card(card):
                hand_number += 1
                
                
    print(mana_need)
    print(mana_have)