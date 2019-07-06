word = input('INPUT?')
search_code = list(input())
output = '' 
for char in word:
    for code in search_code:
        search_code.remove(code)
        if char == code:
            output += code
            break
       
if output == word:
    print(word)
