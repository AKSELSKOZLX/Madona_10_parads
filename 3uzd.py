with open('teksts.txt') as file:
    lines = file.readlines()

third_line = lines[2].strip()
fourth_line = lines[3].strip()

print(third_line)
print(fourth_line)