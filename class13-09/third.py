def square(numbers):
    squarenumbers = []
    totalsquarenumbers =0
    for i in numbers:
        sq = i*i
        squarenumbers.append(sq)
    for i in squarenumbers:
        totalsquarenumbers += i
    
    return totalsquarenumbers


numbers =[1,2,3,4,5,6]

print(square(numbers))