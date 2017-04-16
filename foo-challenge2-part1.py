def answer(s):
    # your code here
    # hall ex: "--->-><-><-->-"
    hall = list(s)
    right = hall.count(">")
    left = hall.count("<")
    print('Hall: ',hall)
    print('Going right: ',right)
    print('Going left: ',left)
    # return salute
    infront = []
    salutesr = 0
    salutesl = 0

    for space in range(0,len(hall)):
        if hall[space] == '>':
            infront = (hall[(space+1):])
            salutesr = salutesr + infront.count('<')
    for space in range(len(hall)-1,-1,-1):      
        if hall[space] == '<':
            infront = (hall[:(space)])
            salutesl = salutesl + infront.count('>')
    print('Salutes right: ', salutesr)
    print('Salutes left: ', salutesl)
    totalsalutes = salutesr+ salutesl
    print('Total salutes: ',totalsalutes) 
    return totalsalutes

# test
#answer("--->-><-><-->-")
answer("<<>><")
    
