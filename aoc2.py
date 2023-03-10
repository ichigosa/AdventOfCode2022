elf_choice = []
user_hint = []
total_score1 = 0
total_score2 = 0
score_element1 = 0
score_element2 = 0
outcome = ''

with open('aoc2-input.txt', 'r') as file:
    for line in file:
        elf_choice.append(line[0])
        user_hint.append(line[2])

def score_element1(hint):
    if hint == 'X':
        score_element1 = 1
    elif hint == 'Y':
        score_element1 = 2
    elif hint == 'Z':
        score_element1 = 3
    else: print('something went wrong')

    return score_element1

def game_outcome_round1(elf_choice, hint):
    if elf_choice == 'A' and hint == 'X':
        outcome = 'draw'
    elif elf_choice == 'A' and hint == 'Y':
        outcome = 'win'
    elif elf_choice == 'A' and hint == 'Z':
        outcome = 'lose'
    elif elf_choice == 'B' and hint == 'X':
        outcome = 'lose'
    elif elf_choice == 'B' and hint == 'Y':
        outcome = 'draw'
    elif elf_choice == 'B' and hint == 'Z':
        outcome = 'win'
    elif elf_choice == 'C' and hint == 'X':
        outcome = 'win'
    elif elf_choice == 'C' and hint == 'Y':
        outcome = 'lose'
    elif elf_choice == 'C' and hint == 'Z':
        outcome = 'draw'
    else: print('something went wrong')

    return outcome

def score_element2(outcome):
    if outcome == 'draw':
        score_element2 = 3
    elif outcome == 'win':
        score_element2 = 6
    elif outcome == 'lose':
        score_element2 = 0
    else: print('something went wrong')

    return score_element2

#PROBLEM 1
for x in range(len(elf_choice)):
    outcome = game_outcome_round1(elf_choice[x], user_hint[x])
    score1 = score_element1(user_hint[x])
    score2 = score_element2(outcome)    
    round_score1 = score1 + score2
    total_score1 += round_score1

print(total_score1)

#PROBLEM 2    

def game_outcome_round2(elf_choice, user_hint):
    choice_dict_A = {'X': 'scissors', 'Y': 'rock', 'Z': 'paper'}
    choice_dict_B = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
    choice_dict_C = {'X': 'paper', 'Y': 'scissors', 'Z': 'rock'}

    if user_hint == 'X':
        outcome = 'lose'
    elif user_hint == 'Y':
        outcome = 'draw'
    elif user_hint == 'Z':
        outcome = 'win'

    if elf_choice == 'A':
        correct_choice = choice_dict_A[user_hint]
    elif elf_choice == 'B':
        correct_choice = choice_dict_B[user_hint]
    elif elf_choice == 'C':
        correct_choice = choice_dict_C[user_hint]

    if correct_choice == 'rock':
        score = 1
    elif correct_choice == 'paper':
        score = 2
    elif correct_choice == 'scissors':
        score = 3

    return [outcome, score]

for x in range(len(elf_choice)):
    outcome = game_outcome_round2(elf_choice[x], user_hint[x])[0]
    score = game_outcome_round2(elf_choice[x], user_hint[x])[1]     
    round_score2 = score + score_element2(outcome) 
    total_score2 += round_score2

print(total_score2)
