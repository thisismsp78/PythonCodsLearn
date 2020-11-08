start=int(input("Start : "))
end=int(input("End : "))
numbers=[number for number in range(start,end) if number%2==0 if number%3==0]
print(numbers)