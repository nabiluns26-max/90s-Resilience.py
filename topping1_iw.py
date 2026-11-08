prompt = "\nEnter a pizza topping (or 'quit' to finish): "

topping = ""
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
        