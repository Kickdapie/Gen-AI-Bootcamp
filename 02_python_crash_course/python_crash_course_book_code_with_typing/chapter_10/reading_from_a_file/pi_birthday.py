from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

# Remember .splitlines makes list of strings based on newlines
lines = contents.splitlines()
pi_string = ''
for line in lines:
    # Remember lstrip removes whitespace
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")