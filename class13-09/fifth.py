Numbers = [34,4,3,2,32,3,4,5,4,3,2,12,2,33,432,432]

def FindMin(Numbers):
    Value = 100000
    for i in Numbers:
        if i < Value:
            Value = i
    return Value

print(FindMin(Numbers))