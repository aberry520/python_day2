string = "sixteen characters"
counter = 0
for index in string:
    if counter % 2 == 0 and string[counter] != " ":
        print(counter)
        print(string[counter])
        print("")
    counter += 1