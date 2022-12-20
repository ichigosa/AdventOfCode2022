elf_choice = []
user_choice = []

with open('aoc2-input.txt', 'r') as file:
    for line in file:
        elf_choice.append(line[0])
        user_choice.append(line[2])

total_score1 = 0
total_score2 = 0
outcome = ''
score_element1 = 0
score_element2 = 0

def score_element1(choice):
    if choice == 'X':
        score_element1 = 1
    elif choice == 'Y':
        score_element1 = 2
    elif choice == 'Z':
        score_element1 = 3
    else: print('something went wrong')

    return score_element1

def score_element2(elf_choice, choice):
    if elf_choice == 'A' and choice == 'X':
        outcome = 'draw'
    elif elf_choice == 'A' and choice == 'Y':
        outcome = 'win'
    elif elf_choice == 'A' and choice == 'Z':
        outcome = 'lose'
    elif elf_choice == 'B' and choice == 'X':
        outcome = 'lose'
    elif elf_choice == 'B' and choice == 'Y':
        outcome = 'draw'
    elif elf_choice == 'B' and choice == 'Z':
        outcome = 'win'
    elif elf_choice == 'C' and choice == 'X':
        outcome = 'win'
    elif elf_choice == 'C' and choice == 'Y':
        outcome = 'lose'
    elif elf_choice == 'C' and choice == 'Z':
        outcome = 'draw'
    else: print('something went wrong')

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
    score1 = score_element1(user_choice[x])
    score2 = score_element2(elf_choice[x], user_choice[x])    
    round_score1 = score1 + score2
    total_score1 += round_score1

print(total_score1)

#PROBLEM 2

def correct_chooser(elf_choice, user_choice):
    choice_dict_A = {'X': 'draw', 'Y': 'win', 'Z': 'lose'}
    choice_dict_B = {'Y': 'draw', 'Z': 'win', 'X': 'lose'}
    choice_dict_C = {'Z': 'draw', 'X': 'win', 'Y': 'lose'}

    if elf_choice == 'A':
        correct_choice = choice_dict_A[user_choice]
    elif elf_choice == 'B':
        correct_choice = choice_dict_B[user_choice]
    elif elf_choice == 'C':
        correct_choice = choice_dict_C[user_choice]
    print(correct_choice)
    
    return correct_choice

for x in range(len(elf_choice)):
    score1 = score_element1(user_choice[x])  
    correct_chooser(elf_choice[x], user_choice[x])
    round_score2 = score1 
    total_score2 += round_score2

print(total_score2)

# score