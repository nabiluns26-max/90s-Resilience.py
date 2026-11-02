active = True
while active:
    topping = input("\nEnter a pizza topping (or 'quit' to finish): ")
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")