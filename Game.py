questions = [
    {"question": "The sun is bigger than the earth?", "answer": "true"},
    {"question": "Water boils at 50 degrees Celsius?", "answer": "false"},
    {"question": "Do birds fly in the sky?", "answer": "true"},
    {"question": "Is the earth flat?", "answer": "false"}
]

score = 0   

for q in questions:
    user_answer = input(q["question"] + " (true/false): ").lower()
    if user_answer == q["answer"]:
        print("Correct")
        score += 1
    else:
        print("Wrong")

print(f"\nThe game is over! Your total score is: {score}/{len(questions)}")  