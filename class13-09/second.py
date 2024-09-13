Numbers = [34,4,3,2,32,3,4,5,4,3,2,1,12,2,33,432,1,432,1]
def oddfinder(Number):
    if (Number %2 != 0):
        return True
    else:
        return False
    
oddlist = filter(oddfinder, Numbers)
for odd in oddlist:
    print(odd, end=" ")