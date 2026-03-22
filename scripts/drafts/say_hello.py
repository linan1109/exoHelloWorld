"""Build and save simple greeting lines for learners enrolled in a selected course.

The script scans a small list of people, keeps only those taking a target course,
formats one greeting per matching person, and writes the result to a text file.
"""

from exohw.utils import load_json_file
from types import SimpleNamespace
import os
# Define each person and their enrolled courses.
# Pillars: Data
# people = [
#   {"name": "Jon Doe", "courses": ["math1", "pSciComp", "physics1"]},
#   {"name": "Leonardo Da Vinci", "courses": ["math99", "cosmology7"]},
#   {"name": "Mona Lisa", "courses": ["linalg3", "pSciComp"]},
# ]
# with open('data/input.json', 'r') as f:
#     people = json.load(f)
    
# with open('config/config.json', 'r') as f:
#     config = json.load(f)
input_path = os.environ.get("INPUT_FILE_PATH", "data/input.json")
config_path = os.environ.get("CONFIG_FILE_PATH", "config/config.json")
output_path = os.environ.get("OUTPUT_FILE_PATH", "data/final/greeting.txt")
# with open(input_path, 'r') as f:
#     people = json.load(f)
# with open(config_path, 'r') as f:
#     config = json.load(f)
people = load_json_file(input_path)
config = load_json_file(config_path)

cfg = SimpleNamespace(**config)
# Set the course to filter by
# Pillars: Configuration, Code.
# course = 'pSciComp'
course = cfg.course

# Initialize an empty list that will store output greeting lines.
# Pillars : Code, Data.
greetings = []

# Iterate through each person record to evaluate enrollment and build output.
# Pillars: Code
for person in people:

  # Keep only people whose course list contains the selected course.
  # Pillars: Code, Configuration.
    # if course in person['courses']:
    if course in person[cfg.key_courses]:

    # Create a personalized greeting with name and add it to the output list.
    # Pillars: Code, Data.
        # greetings.append(f"Hello {person['name']}\n")
        greetings.append(f"Hello {person[cfg.key_name]}\n")

# Open the target file in write mode.
# Pillars: Environment, Configuration, Code.
# with open('data/final/greeting.txt', 'w') as f:
if not os.path.exists(os.path.dirname(output_path)):
    os.makedirs(os.path.dirname(output_path))
with open(output_path, 'w') as f:
  # Write all greeting lines to the file
  # Pillars: Environment, Code, Data.
    f.writelines(greetings)
