couples = [
    ["Johnny", "June"],
    ["John", "Yoko"],
    ["Sonny","Cher"],
]

for couple in couples:
    print(couple)
    for person in couple:
        print(f"Sending invite to... {person}")
