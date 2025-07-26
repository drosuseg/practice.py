def add_sprinkles (func):
    def wrapper(*args, **kwarggs):
        print("*You add sprinkles 🎆*")
        func(*args, **kwarggs)
    return(wrapper)

def add_fudge(func):
    def wrapper(*args, **kwarggs):
        print("*You add fudge 🍫*")
        func(*args, **kwarggs)
    return (wrapper)

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")

get_ice_cream("vanilla")