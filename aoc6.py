#PART 1

with open('aoc6-input.txt', 'r') as file:
    for line in file:
        datastream = line

def find_marker(datastream, n):
    i = 0
    while True:
        signal = datastream[:n + i][-n:]
        if len(signal) == len(set(signal)):
            return n + i
        else: i += 1

print(find_marker(datastream, 4)) #Answer to Part 1
print(find_marker(datastream, 14)) #Answer to Part 2