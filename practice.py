#def add (*args):
#   total = 0 
#    for arg in args:
#        total += arg
#    return total
#print(add(1,2))

def display_name(*args):
    for arg in args:
        print(arg, end= " ")

display_name("Software Engineer", "Donita Rose", "D." , "Seguerra")


