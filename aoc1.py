calorie_total = 0
list_of_totals = []

with open('aoc1-input.txt', 'r') as file:
    for line in file:
        try: 
            calorie_total += int(line)
        except:
            list_of_totals.append(calorie_total)
            calorie_total = 0

print(max(list_of_totals))

top3 = 0

for x in range(3):
    top3 += max(list_of_totals)
    list_of_totals.remove(max(list_of_totals))

print(top3)
    
 



