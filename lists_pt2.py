string = input("enter a word\n")
empty_list = []
for index in range(len(string)):
    empty_list.append(string[index])
print(empty_list)
rev_list = list(reversed(empty_list))
print(rev_list)
empty_string = ""
for index in rev_list:
    empty_string += index
print(empty_string)