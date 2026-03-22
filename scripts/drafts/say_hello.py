"""Build and save simple greeting lines for learners enrolled in a selected course.

The script scans a small list of people, keeps only those taking a target course,
formats one greeting per matching person, and writes the result to a text file.
"""

# Define each person and their enrolled courses.
# Pillars: Data
people = [
  {"name": "Jon Doe", "courses": ["math1", "pSciComp", "physics1"]},
  {"name": "Leonardo Da Vinci", "courses": ["math99", "cosmology7"]},
  {"name": "Mona Lisa", "courses": ["linalg3", "pSciComp"]},
]

# Set the course to filter by
# Pillars: Configuration, Code.
course = 'pSciComp'

# Initialize an empty list that will store output greeting lines.
# Pillars : Code, Data.
greetings = []

# Iterate through each person record to evaluate enrollment and build output.
# Pillars: Code
for person in people:

  # Keep only people whose course list contains the selected course.
  # Pillars: Code, Configuration.
    if course in person['courses']:

    # Create a personalized greeting with name and add it to the output list.
    # Pillars: Code, Data.
        greetings.append(f"Hello {person['name']}\n")


# Open the target file in write mode.
# Pillars: Environment, Configuration, Code.
with open('data/final/greeting.txt', 'w') as f:

  # Write all greeting lines to the file
  # Pillars: Environment, Code, Data.
    f.writelines(greetings)
