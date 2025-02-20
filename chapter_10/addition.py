print("Addition Calculator. Type 'q' to quit.")
while True:
    try:
        num_1 = input("Enter the first number: ")
        if num_1 == "q":
            break
        num_1 = int(num_1)

        num_2 = input("Enter the second number: ")
        if num_2 == "q":
            break
        num_2 = int(num_2)

    except ValueError:
        print("Sorry, you must enter a number.")

    else:
        sum = num_1 + num_2
        print(sum)
