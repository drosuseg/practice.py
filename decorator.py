#added function
def add_sprinkles (func):
    #must add the *args/**kwarggs to accept any number of arguments or keyword (Added in the base is the "flavor")
    def wrapper(*args, **kwarggs):
        print("*You add sprinkles 🎆*")
        func(*args, **kwarggs)
    return(wrapper)

#added function
def add_fudge(func):
    def wrapper(*args, **kwarggs):
        print("*You add fudge 🍫*")
        func(*args, **kwarggs)
    return (wrapper)

#to apply, better use "@" sign for the remaining added function that is modfying the base 
@add_sprinkles
@add_fudge

#base function
def get_ice_cream(flavor):
    #flavor is the added keyword argument
    print(f"Here is your {flavor} ice cream 🍦")

get_ice_cream("vanilla")