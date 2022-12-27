#PART 1

#turn input pairs into lists of ranges
pairs = []
with open('aoc4-input.txt', 'r') as file:
    for line in file:
        pair = line.strip().split(',')
        for i, elf in enumerate(pair):
            sector_range = [int(elf.split('-')[0]), int(elf.split('-')[1])]
            pair[i] = list(range(sector_range[0], sector_range[1]+1))
        pairs.append(pair)

#check if the lists contain each other
tally = 0
for pair in pairs:
    if all(item in pair[0] for item in pair[1]) or all(item in pair[1] for item in pair[0]):
        tally += 1

print(tally) #Answer to Part 1

#PART 2
#check if the lists contain any item of the other
tally2 = 0
for pair in pairs:
    if any(item in pair[0] for item in pair[1]) or any(item in pair[1] for item in pair[0]):
        tally2 += 1

print(tally2) #Answer to Part 2
        