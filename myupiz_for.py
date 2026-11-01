pizzas = ['Margherita', 'Siciliana', 'Calzone']
friend_pizza = pizzas[:]

pizzas.append('Neapolitan')
friend_pizza.append('Romana')

print("My favorit pizza are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizza are:")
for frined_fav in friend_pizza:
    print(frined_fav)