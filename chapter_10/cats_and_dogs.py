from pathlib import Path

files = ["cats.txt", "dogs.txt"]

for file in files:

    path = Path(file)
    try:
        contents = path.read_text()

    except FileNotFoundError:
        pass

    else:
        print(f"Parsing {file}: ")
        print(contents)
        print("\n")
