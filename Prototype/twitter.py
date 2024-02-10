url = input("URL: ").strip()

name = url.removeprefix("https://twitter.com/")
print(f"hello: {name}")