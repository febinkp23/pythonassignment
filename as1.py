# Function to classify a given number
def classify_number(number):
    if number < 0:
        print("The number is negative.")
    elif number == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")

# Taking user input
user_input = int(input("Enter a number: "))

# Calling the function with the user input
classify_number(user_input)
