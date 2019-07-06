word = input('INPUT?\n')
search_code = input()
count = 0
index = 0 
if word[0] not in search_code:
    count = 1
else:
    for char in word:
        index = search_code.find(char,index)
        if index == -1:
            count = 1

if count == 1:
    print(' ')
else:
    print(word)