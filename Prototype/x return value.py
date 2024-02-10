def main():
    x = get_int()
    print(f"x = {x}")

def get_int():
    while True:
        try:
            x = int(input("What's the x? "))
        except ValueError:
            print("Value error lol")
        else:
            break
    return x

main()
