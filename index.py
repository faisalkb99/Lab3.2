
numbers = []

for i in range(10):
    value = input(f"Enter value {i+1} (or 'stop' to exit): ")
    if value.lower() == 'stop':
        break
    numbers.append(float(value))

if len(numbers) == 0:
    print("No numbers entered.")
else:
   
    largest = numbers[0]


    for number in numbers:
        if number > largest:
            largest = number


    print("The largest number is:", largest)