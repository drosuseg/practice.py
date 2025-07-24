from script1 import *

def favorite_drink(drink):
     print(f"Your favorite drink: {drink}")

def main():
    print("This is script 2")
    favorite_food("Sushi")
    favorite_drink("coffee")
    print('GOODBYE')

if __name__=='__main__':
     main()