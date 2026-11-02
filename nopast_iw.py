sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'egg', 'veggie', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")