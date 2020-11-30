
from cards import Card, Sorcery, Creature, Land, Artifact
import copy

mana_colors_to_types = {"White": "Plains", "Blue": "Island", "Black": "Swamp", 
                        "Red": "Mountain", "Green": "Forest"}
mana_types_to_colors = {"Plains": "White", "Island": "Blue", "Swamp": "Black", 
                        "Mountain": "Red", "Forest": "Green"}
mana_have = {}
mana_need = {}
mana_left = {}
hand_number = 0
hands = []

def determine_weights_of_cards_in_hand(hand, i):
    for card in hand: # iterates twice bc we need the amount of land to 
                      #determine value of other cards
        if isinstance(card, Creature):
            get_total_mana_cost(card)
            if card.total_mc <= i and have_enough_mana_for_card(card):
                card.value_in_hand = (10 - i) * card.base_power
                print(card, (10-i), card.base_power)
                mana_left = copy.deepcopy(mana_have)
    
def get_total_mana_cost(card):    
    for mana_type in card.mc:
        card.total_mc += card.mc[mana_type] 
        mana_need[mana_type] += card.mc[mana_type]
    
def determine_whether_to_mulligan(hand, mulligans):
    num_lands = 0
    num_creatures = 0
    min_mc = 100
    for card in hand:
        get_total_mana_cost(card)
        if isinstance(card, Creature):
            num_creatures += 1
            if card.total_mc < min_mc:
                min_mc = card.total_mc
        if isinstance(card, Land):
            num_lands += 1
    if num_lands < (3 - mulligans * .5) or num_lands > (4 - mulligans * .5):
        #print("Based on the number of lands you were dealt, you should mulligan.")
        return True
    if num_creatures < (2 - mulligans * .5) or num_creatures > (3 - mulligans * .5):
        #print("Based on the number of creatures you were dealt, you should mulligan.")
        return True
    if min_mc > 2:
        #print("You have no creatures that you can use in the first 3 turns. Mulligan!")
        return True
    return False

def print_hand(hand):
    #print("This is your hand:")
    for card in hand:
        if isinstance(card, Creature):
            print(card, "- Creature")
        if isinstance(card, Land):
            print(card, "- Land")
        if isinstance(card, Sorcery):
            print(card, "- Sorcery")
        if isinstance(card, Artifact):
            print(card, "- Artifact")
    
def deal_new_hand(player, mulligans):
    #print("Dealing new hand")
    player.put_cards_back()
    player.shuffle_deck()
    player.draw_cards()
    
def assess_starting_hand(player):
    print_hand(player.hand)
    initialize_mana_dicts()
    should_mulligan = determine_whether_to_mulligan(player.hand, 0)
    #if should_mulligan == False:
    #    print("No need to mulligan. Carry on.")
    if should_mulligan == True:
        mulligans = 1
        while should_mulligan == True and mulligans < 4:
            deal_new_hand(player, mulligans)
            print_hand(player.hand)
            should_mulligan = determine_whether_to_mulligan(player.hand, mulligans)
            if should_mulligan == True:
                mulligans += 1
            if should_mulligan == False:
                for j in range(mulligans):
                    one_creatures = []
                    expensive_creatures = []
                    two_creatures = []
                    lands = []
                    for card in player.hand:
                        if isinstance(card, Land):
                            mana_have[mana_types_to_colors[card.subtypes]] += 1
                            card.value_in_hand = mana_have[mana_types_to_colors[card.subtypes]]
                            lands.append(card)
                        if isinstance(card, Creature):
                            if card.total_mc >= 4:
                                expensive_creatures.append(card)
                            if card.total_mc == 2 and have_enough_mana_for_card(card) == False:
                                two_creatures.append(card)
                                continue
                            if card.base_power == 1:
                                one_creatures.append(card)
                    for i in range(get_total_mana(mana_have)):     
                        determine_weights_of_cards_in_hand(player.hand, i)
                    if len(expensive_creatures) > 1:
                        player.put_particular_card_back(expensive_creatures.pop())
                    elif len(one_creatures) > 1:
                        player.put_particular_card_back(one_creatures.pop())
                    elif len(two_creatures) > 1:
                        player.put_particular_card_back(two_creatures.pop())
                    elif len(lands) >= ((7-mulligans)/2)+1:
                        player.put_particular_card_back(can_land_be_used(lands))
                    else:
                        player.put_particular_card_back(player.hand[0])
            
    
def initialize_mana_dicts(): #DONE
    for each in mana_colors_to_types:
        mana_have[each] = 0
        mana_need[each] = 0
    mana_need["Generic"] = 0
    mana_need["Colorless"] = 0
    
def can_land_be_used(land_cards):
    for card in land_cards:
        if mana_need[mana_types_to_colors[str(card)]] == 0:
            return card
    return card.pop()
    
    
def have_enough_mana_for_card(card): #DONE
    temp_mana = copy.deepcopy(mana_have)
    extra_mana = 0
    rest_of_mana = 0
    for mana_type in card.mc:
        if mana_type == "Colorless" or mana_type == "Generic":
            rest_of_mana += card.mc[mana_type]
            continue
        if temp_mana[mana_type] < card.mc[mana_type]:
            return False
        else:
            temp_mana[mana_type] -= card.mc[mana_type]
            extra_mana = get_total_mana(temp_mana)
    if extra_mana < card.mc["Colorless"] + card.mc["Generic"]:
        return False
    return True

def get_total_mana(mana_dict):
    total_mana = 0
    for mana_type in mana_dict:
        total_mana += mana_dict[mana_type]
    return total_mana