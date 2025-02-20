from pathlib import Path


def count_common_words(file, word):
    """Counts # of times provided word appears in .txt file"""
    path = Path(file)

    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        count = contents.lower().count(word)
        print(f"{file} has the word {word} in it {count} times.")


count_common_words("five_years.txt", "the")
