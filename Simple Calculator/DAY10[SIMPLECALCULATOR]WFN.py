string_list = ["Welcome to Warren's simple calculator program!", "What is the first number in the calculation?",
               "+\n-\n*\n/\nexponent\nPick an operation:", "What is the second number in the calculation?",
               "You may not divide by zero. Enter new values"]
def calculator(first_number, operator, second_number):
    if operator == "+":
        result = round(first_number + second_number, 2)
        return result
    elif operator == "-":
        result = round(first_number - second_number, 2)
        return result
    elif operator == "*":
        result = round(first_number * second_number, 2)
        return result
    elif operator == "/":
        result = round(first_number / second_number, 2)
        return result

while True:
    first_number = float(input(string_list[1]))
    while True:
        operator = input(string_list[2])
        second_number = float(input(string_list[3]))
        if operator == "/" and second_number == 0:
            print(string_list[4])
            break
        answer = calculator(first_number, operator, second_number)
        print(f"The answer to {first_number}{operator}{second_number} is {answer}.")
        first_number = calculator(first_number, operator, second_number)
        request = input(f"Type 'y' to use {first_number} for next calculation,\n or type 'n' to start over...")
        if request.lower() == "n":
            break