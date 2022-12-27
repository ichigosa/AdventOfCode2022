import re

crates = []
instructions = []

with open('aoc5-input.txt', 'r') as file:
    for i in range(8):
        crates.append(next(file))
    for line in file:
        if line.startswith('move'):
            instructions.append(line.strip())

instruction_numbers = []
for instruction in instructions:
    temp_list = re.findall(r'\d+', instruction)
    numbers = [int(i) for i in temp_list]
    instruction_numbers.append(numbers)

stack = []
for line in crates:
    layer = []
    i = 1
    while i < 36:
        layer.append(line[i])
        i += 4
    stack.append(layer)

#PART 1 and 2
def find_depth(stack, col): #finding the row on which the stack starts
    d = 0
    while True:
        if d == len(stack):
            break
        elif stack[d][col] == ' ':
            d += 1
        else:
            break
    return d

for numbers in instruction_numbers:
    col = numbers[1] - 1
    col2 = numbers[2] -1
    d = (find_depth(stack, col))
    h = (find_depth(stack, col2))
    stack_top = stack[d][col]
    stack_depth = numbers[0]
    stack_slice = []

    #creating a slice of the stack
    for i in range(stack_depth):
        stack_slice.append(stack[d + i][col])
        stack[d+i][col] = ' '

    #adding more rows if not enough space
    if h < len(stack_slice):
        for i in range(len(stack_slice) - h):
            stack.insert(0, [' '] * 9)
            h += 1

    # stack_slice.reverse() #uncomment this line for code to evaluate answer 2

    #adding the crates in the slice to new column
    for i in range(len(stack_slice)):
        stack[h - (1 + i)][col2] = stack_slice[i]

result = []
for i in range(len(stack[0])):
    for layer in stack:
        if layer[i] != ' ':
            result.append(layer[i])
            break

print(result)









































