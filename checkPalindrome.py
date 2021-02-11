lst = []
for i in range(5):
    lst.append(input('Enter number :\t'))

for i in lst:
    if i[::-1] == i:
        print('Palindrome')
    else:
        print('Not Palindrome')