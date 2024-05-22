import random

# PARAMETERS
TOTAL_PULLS = 1000 # The pulls the simulation is going to have
TOTAL_PREMIUM_CURRENCY = 0 # The premium currency you have
HAS_SUB_PITTY = True
CHAR_BANNER = True

# SYSTEM VARIABLES
# Characters
FIVE_CHRACTER_RATE = 0.6
FOUR_CHRACTER_RATE = 5.1
PITTY_CHAR = 90
PITTY_FOUR_CHAR = 10
SUB_PITTY_START_CHAR = 74
SUB_PITTY_PROBABILITY_INCREASE_CHAR = 5

# Weapons
FIVE_WEAPON_RATE = 0.8
FOUR_WEAPON_RATE = 6.6
PITTY_WEAPON = 80
PITTY_FOUR_WEAPON = 10
SUB_PITTY_START_WEAPON = 64
SUB_PITTY_PROBABILITY_INCREASE_WEAPON = 5

# SIMULATION VARIABLES

amount_five_char = 0
amount_four_char = 0
amount_five_weapon = 0
amount_four_weapon = 0

amount_of_shit = 0

sub_pitty_added_prob_char = 0
sub_pitty_added_prob_weapon = 0

five_character_done_pulls = 0
five_weapon_done_pulls = 0
four_character_done_pulls = 0
four_weapon_done_pulls = 0

milestone_list = []


def check_result(rand, i):
    global amount_four_char, amount_five_char, amount_five_weapon, amount_four_weapon, five_weapon_done_pulls, five_character_done_pulls
    global sub_pitty_added_prob_char, sub_pitty_added_prob_weapon, four_character_done_pulls, four_weapon_done_pulls, amount_of_shit
    
    if CHAR_BANNER:
        
        five_character_done_pulls += 1
        four_character_done_pulls += 1
        temp_prob = FIVE_CHRACTER_RATE
        
        if five_character_done_pulls >= PITTY_CHAR:
            #Obtained 5 Star character
            milestone_list.append("CHAR OBTAINED AT: " + str(i+1) + " WITH PITTY AT " + str(five_character_done_pulls))
            amount_five_char += 1
            sub_pitty_added_prob_char = 0
            five_character_done_pulls = 0
            return 0
        
        # If subpitty exists, add probability to 5 star
        if HAS_SUB_PITTY and five_character_done_pulls > SUB_PITTY_START_CHAR:
            sub_pitty_added_prob_char += SUB_PITTY_PROBABILITY_INCREASE_CHAR
            temp_prob += sub_pitty_added_prob_char
            
        if rand <= temp_prob:
            #Obtained 5 Star character
            milestone_list.append("CHAR OBTAINED AT: " + str(i+1) + " WITH PITTY AT " + str(five_character_done_pulls))
            amount_five_char += 1
            sub_pitty_added_prob_char = 0
            five_character_done_pulls = 0
            return 0
        if rand <= FOUR_CHRACTER_RATE:
            #Obtained 4 Star character
            amount_four_char += 1
            four_character_done_pulls = 0
            return 1
        
        if four_character_done_pulls >= PITTY_FOUR_CHAR:
            #Obtained 4 Star character
            amount_four_char += 1
            four_character_done_pulls = 0
            return 1
        
        amount_of_shit += 1
        return 2
    else:
        
        five_weapon_done_pulls += 1
        four_weapon_done_pulls += 1
        temp_prob = FIVE_WEAPON_RATE
        
        if five_weapon_done_pulls >= PITTY_WEAPON:
            #Obtained 5 Star weapon
            milestone_list.append("WEAPON OBTAINED AT: " + str(i+1) + " WITH PITTY AT " + str(five_weapon_done_pulls))
            amount_five_weapon += 1
            sub_pitty_added_prob_weapon = 0
            five_weapon_done_pulls = 0
            return 0
        
        # If subpitty exists, add probability to 5 star
        if HAS_SUB_PITTY and five_weapon_done_pulls > SUB_PITTY_START_WEAPON:
            sub_pitty_added_prob_weapon += SUB_PITTY_PROBABILITY_INCREASE_WEAPON
            temp_prob += sub_pitty_added_prob_weapon
        
        if rand <= temp_prob:
            #Obtained 5 Star weapon
            milestone_list.append("WEAPON OBTAINED AT: " + str(i+1) + " WITH PITTY AT " + str(five_weapon_done_pulls))
            amount_five_weapon += 1
            sub_pitty_added_prob_weapon = 0
            five_weapon_done_pulls = 0
            return 0
        if rand <= FOUR_WEAPON_RATE:
            #Obtained 4 Star weapon
            amount_four_weapon += 1
            four_weapon_done_pulls = 0
            return 1
        
        if four_weapon_done_pulls >= PITTY_FOUR_WEAPON:
            #Obtained 4 Star weapon
            amount_four_weapon += 1
            four_weapon_done_pulls = 0
            return 1
        
        amount_of_shit += 1
        return 2


#Check if it is player or weapon banner

for i in range(TOTAL_PULLS):
    
    # Returns which has obtained (0 for 5 star char/ 1 for 4 star char / 2 else)
    res = check_result(random.uniform(0, 100), i)
    
print("FIVE STAR CHARACTERS: " + str(amount_five_char))
print("FOUR STAR CHARACTERS: " + str(amount_four_char))
print("FIVE STAR WEAPONS: " + str(amount_five_weapon))
print("FOUR STAR WEAPONS: " + str(amount_four_weapon))

print(milestone_list)
    
    
    
    
    