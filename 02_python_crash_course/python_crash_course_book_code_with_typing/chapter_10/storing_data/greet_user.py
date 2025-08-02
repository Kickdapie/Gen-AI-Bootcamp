from pathlib import Path
import json


path = Path('/home/sashank/Desktop/gen_ai_bootcamp/02_python_crash_course/python_crash_course_book_code_with_typing/chapter_10/storing_data/username.json')
contents = path.read_text()
# json.loads gets the contents of a json file
username = json.loads(contents)

print(f"Welcome back, {username}!")