
try:
    number = int(input("Enter a number: "))
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("Hey dude you can't divide by 0, Duh!")
except ValueError:
    print("Please enter a valid number, my app isn't that smart yet. :(")
except Exception as e:
    print(f"An unexpected error has occured: {e}")