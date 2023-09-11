encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
sollist = list()
for z in range(len(encrypted_message)):
    sollist.append('')
count = 1
solution = ''
for x in range(len(encrypted_message)):
        if (count % 2) == 0:
            first = encrypted_message[len(encrypted_message) - 1 - x]
            second = encrypted_message[x]
        else:
            first = encrypted_message[x]
            second = encrypted_message[len(encrypted_message) - 1 - x]
        count += 1
        if x >= (len(encrypted_message) - x): break
        sollist[x], sollist[len(sollist) - x - 1] = first, second
for letter in sollist:
    solution += letter
print(solution)

