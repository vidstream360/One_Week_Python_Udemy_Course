#for letter in "supercalifragilisticexpialidocious":
#    if letter == 'c':
#        break
#    print(letter)

message = input("say hi: ")
while True:
    if message == "hi":
        break
    message = input("please say hi: ")
print("Thanks for saying hi")

#for char in "FATCAT":
#    if char == "A":
#        continue
#    print(char)
#print("After Loop")

for letter in "supercalifragilisticexpialidocious":
    if letter == 'c':
        continue
    print(letter)