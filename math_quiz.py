import json

# Load questions from JSON file
with open("questions.json", "r") as file:
    questions = json.load(file)

# Get user name
user_name = input("Enter your name: ")

# Initialize score
score = 0

# Ask each question
for q in questions:
    answer = int(input(f"{q['question']} = "))
    if answer == q["answer"]:
        score += 1

# Print user score
print(f"{user_name}, your score is {score}/{len(questions)}")

# Load existing results or initialize an empty list
try:
    with open("results.json", "r") as file:
        results = json.load(file)
except FileNotFoundError:
    results = []

# Append new result
results.append({"name": user_name, "score": score})

# Save results back to JSON file
with open("results.json", "w") as file:
    json.dump(results, file, indent=4)
