from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('/home/sashank/Desktop/gen_ai_bootcamp/02_python_crash_course/python_crash_course_book_code_with_typing/chapter_10/storing_data/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)