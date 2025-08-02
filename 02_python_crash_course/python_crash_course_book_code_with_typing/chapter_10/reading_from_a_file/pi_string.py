# from pathlib import Path

# path = Path('pi_million_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()

# print(f"{pi_string[:52]}...")
# print(len(pi_string))

from pathlib import Path

path = Path("/home/sashank/Desktop/gen_ai_bootcamp/02_python_crash_course/python_crash_course_book_code_with_typing/chapter_10/reading_from_a_file/pi_million_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(f'{pi_string[:51]}')