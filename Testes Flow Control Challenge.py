def test_ex_1_1(balance, bet_amount, bet_choice, outcome):
    bet_choice = bet_choice.lower()

    test_balance = 1000
    assert bet_choice in ('red', 'black'), "bet_choice should be either black or red!"
    assert bet_amount < balance, "bet_amount is greater than balance"
    assert type(bet_choice) == str, "bet_choice should be a string 'red' or 'black'"
    if outcome == bet_choice:
        assert_msg = f"You're not adding correctly to balance -> your balance ({balance}) is different than initial_balance (1000) + bet_amount ({bet_amount})"
        assert balance == (test_balance + bet_amount), assert_msg
    else:
        assert_msg = f"You're not subtracting correctly from balance -> your balance ({balance}) is different than initial balance (1000) - bet_amount ({bet_amount})"
        assert balance == (test_balance - bet_amount), assert_msg
    print("All basic tests passed!")

def test_ex_1_2(balance, bet_amount, bet_choice, outcomes):
    bet_choice = bet_choice.lower()
    assert bet_choice in ('red', 'black'), "You must select a bet on either black or red!"
    assert len(outcomes) == 50, "You did not play 50 times!"
    assert all([i in ('red', 'black') for i in outcomes]), "wrong outcome in outcomes list. ensure outcomes are 'black' and 'red' only"
    test_balance = 1000
    for outcome in outcomes:
        if outcome == bet_choice:
            test_balance += bet_amount
        else:
            test_balance -= bet_amount
    assert_msg = f"Given balance: {balance} is not equal to the final expected balance: {test_balance}."
    assert balance == test_balance, assert_msg
    print("All basic tests passed!")


def test_ex_1_3(balance, bet_amount, bet_choice, outcomes):
    bet_choice = bet_choice.lower()
    assert bet_choice in ('red', 'black'), "You must select a bet on either black, red!"
    assert len(outcomes) == 50, "You did not play 50 times!"
    assert all([i in ('red', 'black', 'green') for i in outcomes]), "wrong outcome in outcomes list. ensure outcomes are 'black', 'red', 'green' only"
    test_balance = 1000
    for outcome in outcomes:
        if outcome == bet_choice:
            test_balance += bet_amount
        else:
            test_balance -= bet_amount
    assert_msg = f"Given balance: {balance} is not equal to the final expected balance: {test_balance}."
    assert balance == test_balance, assert_msg
    print("All basic tests passed!")

def test_ex_1_4(balance_no_green, balance_green, bet_amount, bet_choice, outcomes_no_green, outcomes_green, less_winnings):
    bet_choice = bet_choice.lower()
    assert bet_choice in ('red', 'black'), "You must select a bet on black or red!"
    assert len(outcomes_green) == 1000, "You did not play 1000 times in the green number case!"
    assert len(outcomes_green) == 1000, "You did not play 1000 times in the non-green number case!"
    assert all([i in ('red', 'black', 'green') for i in outcomes_green]), "wrong outcome in outcomes_green list. ensure you are only including 'red' and 'black' and 'green'"
    assert all([i in ('red', 'black') for i in outcomes_no_green]), "wrong outcome in outcomes list. ensure you are only including 'red' and 'black'"
    test_balance_no_green, test_balance_green = 1000, 1000
    for outcome_no_green, outcome_green in zip(outcomes_no_green, outcomes_green):
        if outcome_no_green == bet_choice:
            test_balance_no_green += bet_amount
        else:
            test_balance_no_green -= bet_amount
        if outcome_green == bet_choice:
            test_balance_green += bet_amount
        else:
            test_balance_green -= bet_amount
    assert_msg_no_green = f"Given no_green case balance: {balance_no_green} is not equal to the final expected balance: {test_balance_no_green}."
    assert_msg_green = f"Given green case balance: {balance_green} is not equal to the final expected balance: {test_balance_green}."
    assert_msg_winnings = f"expected less_winnings is {test_balance_green < test_balance_no_green} but received {less_winnings}"
    assert balance_no_green == test_balance_no_green, assert_msg_no_green
    assert balance_green == test_balance_green, assert_msg_green
    assert less_winnings == (test_balance_green < test_balance_no_green), assert_msg_winnings
    print("All basic tests passed!")

def test_ex_1_5(balance, bet_amount, bet_choice, outcomes, ofm_number_of_plays):
    bet_choice = bet_choice.lower()
    assert len(outcomes) > 0, "outcomes list is empty!"
    assert bet_choice in ('red', 'black'), "You must select a bet on either black or red!"
    assert all([i in ('red', 'black') for i in outcomes]), "wrong outcome in outcomes list. ensure outcomes are 'black' and 'red' only"

    test_balance = 1000
    test_nbr_plays = 0
    for outcome in outcomes:
        if outcome == bet_choice:
            test_balance += bet_amount
        else:
            test_balance -= bet_amount
        test_nbr_plays += 1
    assert test_balance >= 0, f"Negative balance {test_balance}! Ensure you play until you don't have more balance to place another bet (amount: {bet_amount})"
    assert_msg_balance = f"Given balance: {balance} is not equal to the final expected balance: {test_balance}."
    assert balance == test_balance, assert_msg_balance
    assert ofm_number_of_plays == test_nbr_plays, f"ofm_number_of_plays does not match the expected number of plays: {test_nbr_plays}"
    print("All basic tests passed!")

    
def test_ex_2(balance, bet_choice, bet_amount, times_played, outcomes):
    assert type(bet_choice) == int, "You must choose a number between 0 and 36 to bet on"
    assert bet_choice in range(0,37), "You must choose a number between 0 and 36 to bet on"
    assert bet_amount < 1000,"You cannot bet more money than your initial balance"
    assert len(outcomes) > 0, "outcomes list is empty!"
    assert all([i in range(0, 37) for i in outcomes]), "Each outcome should be a number between 0 and 36"
    test_balance = 1000
    test_nbr_plays = 0
    for outcome in outcomes:
        if outcome == bet_choice:
            test_balance += 35* bet_amount
        else:
            test_balance -= bet_amount
        test_nbr_plays += 1
    assert test_balance >= 0, f"Negative balance {test_balance}! Ensure you play until you don't have more balance to place another bet (amount: {bet_amount})"
    assert_msg_balance = f"Given balance: {balance} is not equal to the final expected balance: {test_balance}."
    assert balance == test_balance, assert_msg_balance
    assert times_played == test_nbr_plays, f"times_played does not match the expected number of plays: {test_nbr_plays}"
    print('All basic tests passed!')
