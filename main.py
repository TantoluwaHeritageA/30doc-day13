def pick_acryn(word):
    acry = ''
    space = ' '
    output = []
    for el in word:
        if el.isalpha() or el == space:
            acry += el
    for i in acry.split(' '):
        if i.isupper() and len(i) > 1:
            output.append(i)
    return output


print(pick_acryn(str(input("Enter sentence with acronym: "))))
