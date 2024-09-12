def mul_Value(N1, N2):
    sum = N1 + N2
    product = N1 *N2
    return sum, product

# Lambda function only returns one value

sum, product = mul_Value(2,5)
print(f'Sum of values is:{sum} and product is: {product}')