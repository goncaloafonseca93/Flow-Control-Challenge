# Exercice 1
# 1.1

import random
balance = 1000
bet_amount = 10 # you can choose another amount to bet (as long as it is lower than your initial_balance)
bet_choice = "red" # choose "red" or "black"
outcome = random.choice(['red', 'black'])
# your solution here

if outcome == bet_choice:
    balance += bet_amount
else:
    balance -= bet_amount

#1.2

balance = 1000
bet_amount = 10
bet_choice = "red"  # choose "red" or "black" (for all plays!)
outcomes = []
# your solution here

for bet in range(50):
    outcome = random.choice(['red', 'black'])
    outcomes.append(outcome)
    
    if outcome == bet_choice:
        balance += bet_amount
    else:
        balance -= bet_amount

#1.3

balance = 1000
bet_amount = 10
bet_choice = "red" # choose "red", "black"
outcomes = []
# your solution here

list_of_possibilities = ['green'] + 18 * ['red'] + 18 * ['black']

for bet in range(50):
    outcome = random.choice(list_of_possibilities)
    outcomes.append(outcome)
    
    if outcome == bet_choice:
        balance += bet_amount
    else:
        balance -= bet_amount

#1.4

balance = 1000
bet_amount = 10
bet_choice = "red"  # choose "red" or "black"
ofm_number_of_plays = 0
outcomes = []
# your solution here

while balance > bet_amount:
    
    outcome = random.choice(['red', 'black'])
    outcomes.append(outcome)
    
    if outcome == bet_choice:
        balance += bet_amount
    else:
        balance -= bet_amount

    ofm_number_of_plays += 1