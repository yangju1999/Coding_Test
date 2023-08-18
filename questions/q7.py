input_string = input()

length = len(input_string)
left_string = input_string[:length//2]
right_string = input_string[length//2:]

dictionary = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

total_left = 0
for digit in left_string:
    total_left+=dictionary[digit]

total_right = 0
for digit in right_string:
    total_right+=dictionary[digit]

if total_left == total_right:
    print('LUCKY')
else:
    print('READY')
