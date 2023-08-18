input_string = input() 

numbers = {'0', '1', '2', '3', '4', '5', '6','7', '8', '9'}
english = []
total = 0 
for i in input_string:
    if i in numbers:
        total += int(i)
    else:
        english.append(i)

english.sort()

for e in english:
    print(e, end = '')
print(total)


        