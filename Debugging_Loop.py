while True:
    q=input("Enter preference: ")
    if q.isdigit():
        q=int(q)
        if 1<=q<=6:
            print(f"Valid, you chose: {q}")
            break
        else:
            print("Invalid, please enter a number between 1 and 6.")
    else:
        print("Invalid, please enter a number between 1 and 6.")
