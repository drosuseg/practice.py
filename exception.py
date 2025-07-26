# An event that interrupts the flow of a program
# (ZeroDivision, TypeError, ValueError)
# 1.try, 2.except, 3.finally

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Please enter a number IDIOT!")
except Exception:
    print("Something is not correct")
finally:
    print("pls cleanup")