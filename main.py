print("Hello World")

x = input("Enter 1 or 2: ")

match x:
    case "1":
        print("You entered 1")
    case "2":
        print("You entered 2")
    case _:
        print("You entered something else")