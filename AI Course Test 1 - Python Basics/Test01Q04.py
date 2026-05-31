duplicates = False
set_input = set()
while True:
    string = input('Enter string: ').lower().strip()
    if string == 'quit':
        break
    if string in set_input:
        duplicates = True
    set_input.add(string)
if duplicates:
    print('There were duplicates')
else:
    print('There were no duplicates')
