from pathlib import Path

path = Path('/home/sashank/Desktop/gen_ai_bootcamp/02_python_crash_course/python_crash_course_book_code_with_typing/chapter_10/reading_from_a_file/pi_digits.txt')
#read_text
contents = path.read_text()

# .splitlines
lines = contents.splitlines()
for line in lines:
    print(line)