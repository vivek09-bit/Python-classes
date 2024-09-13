def square(numbers):
    squarenumbers = []
    for i in numbers:
        sq = i*i
        squarenumbers.append(sq)
    return squarenumbers


numbers =[1,2,3,4,5,6]

print(square(numbers))