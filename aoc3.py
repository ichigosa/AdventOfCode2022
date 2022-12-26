import string

#PART 1

#mapping priorities
letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
numbers = list(range(1, 53))
priorities = {letters[i]: numbers[i] for i in range(len(letters))}

packs = []
with open('aoc3-input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        compartment1 = line[0: len(line) // 2]
        compartment2 = line[len(line) // 2 :]
        rucksack = [compartment1, compartment2]
        packs.append(rucksack)

dupes = []
for pack in packs:
    for item in pack[0]:
        if item in pack[1]:
            dupes.append(item)
            break

dupe_total = 0
for dupe in dupes:
    priority = priorities[dupe]
    dupe_total += priority

print(dupe_total) # PART 1 Answer

#PART 2

n = 0
elf_groups = []
for pack in packs:
    full_pack = pack[0] + pack[1]
    if n == 0:
        group = []
        group.append(full_pack)
        n += 1
    elif n == 1:
        group.append(full_pack)
        n += 1
    elif n == 2:
        group.append(full_pack)
        elf_groups.append(group)
        n = 0

badges = []
for group in elf_groups:
    for item in group[0]:
        if item in group[1] and item in group[2]:
            badges.append(item)
            break

badge_total = 0
for badge in badges:
    priority = priorities[badge]
    badge_total += priority

print(badge_total) #PART 2 Answer
