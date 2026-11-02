def make_sandwich(*items):
    print("\nMaking a sandwich with:")
    for item in items:
        print(f"- {item}")


make_sandwich("cheese", "tomato")
make_sandwich("chicken", "lettuce", "mayonnaise")
make_sandwich("egg", "cheese", "onion", "tomato")