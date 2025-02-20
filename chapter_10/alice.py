from pathlib import Path

def count_words(path):
    """Count the approximate number of words in file"""
    try:
        contents = path.read_text(encoding="utf-8")
    # except FileNotFoundError:
    #     print(f"Sorry, the file {path} does not exist")
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path("alice.txt")
count_words(path)

path = Path("moby_dick.txt")
count_words(path)

path = Path("siddhartha.txt")
count_words(path)

path = Path("little_women.txt")
count_words(path)