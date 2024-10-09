def odd_numbers(end,start = 0):
    """Calculate odd numbers"""
    for number in range(start,end):
        if number % 2 == 0:
            continue
        print(number, sep=",")
odd_numbers(50)

