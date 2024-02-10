name = input("What's your username? ").strip()
if (",") in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")
