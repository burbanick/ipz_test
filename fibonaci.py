prew = cur = 1
element = input('element number: ')
element = int(element)
for n in range(int(element-2)):
    tmp = prew + cur
    prew = cur
    cur = tmp
print(str(element)+' element =  ' + str(cur))
