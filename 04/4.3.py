for value in range(1,5):
    print(value)
number = list(range(1,6))
print(number)

e_number = list(range(2,11,2))
print(e_number)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

digits = list(range(1,11))
print(min(digits))
print(max(digits))
print(sum(digits))

sqs = [sq**2 for sq in range(1,11)]
print(sqs)