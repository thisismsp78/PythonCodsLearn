#sumFunction=lambda first,second:first+second
#print(sumFunction(10,100))
#print((lambda number:pow(number,0.5))(10))
#print([(lambda n:pow(n,0.5))(number) for number in range(1,10)])

def test(operation,numbers):
    for number in numbers:
        print(operation(number))

test(lambda n:n/2,[2,4,6])
print("----------")
test(lambda n:n*2,[2,4,6])