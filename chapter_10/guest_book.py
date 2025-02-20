from pathlib import Path

path = Path("guest_book.txt")

guest_names = []
while True:
    guest = input("Input a guest name and press enter ('quit' to exit) ")
    if guest == 'quit':
        break
    guest_names.append(guest)

file_string = ''
for guest in guest_names:
    file_string += f"{guest}\n"

path.write_text(file_string)