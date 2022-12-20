elf_choice = []
user_hint = []

with open('aoc2-input.txt', 'r') as file:
    for line in file:
        elf_choice.append(line[0])
        user_hint.append(line[2])

total_score1 = 0
score_element1 = 0
score_element2 = 0
outcome = ''

def score_element1(hint):
    if hint == 'X':
        score_element1 = 1
    elif hint == 'Y':
        score_element1 = 2
    elif hint == 'Z':
        score_element1 = 3
    else: print('something went wrong')

    return score_element1

def game_outcome(elf_choice, hint):
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
    outcome = game_outcome(elf_choice[x], user_hint[x])
    score1 = score_element1(user_hint[x])
    score2 = score_element2(outcome)    
    round_score1 = score1 + score2
    total_score1 += round_score1

print(total_score1)

#PROBLEM 2

# def correct_chooser(elf_choice, user_hint):
#     choice_dict_A = {'X': 'draw', 'Y': 'win', 'Z': 'lose'}
#     choice_dict_B = {'Y': 'draw', 'Z': 'win', 'X': 'lose'}
#     choice_dict_C = {'Z': 'draw', 'X': 'win', 'Y': 'lose'}

#     if elf_choice == 'A':
#         correct_choice = choice_dict_A[user_hint]
#     elif elf_choice == 'B':
#         correct_choice = choice_dict_B[user_hint]
#     elif elf_choice == 'C':
#         correct_choice = choice_dict_C[user_hint]
#     print(correct_choice)
    
#     return correct_choice

# for x in range(len(elf_choice)):
#     score1 = score_element1(user_hint[x])  
#     correct_chooser(elf_choice[x], user_hint[x])
#     round_score2 = score1 
#     total_score2 += round_score2

# print(total_score2)

# score