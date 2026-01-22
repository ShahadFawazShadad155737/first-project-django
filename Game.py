questions = [
    {"question": "الشمس أكبر من الأرض؟", "answer": "صح"},
    {"question": "الماء يغلي عند 50 درجة مئوية؟", "answer": "خطأ"},
    {"question": "القطط تحب الحليب؟", "answer": "صح"},
    {"question": "الأرض مسطحة؟", "answer": "خطأ"}
]

score = 0  


for q in questions:
    user_answer = input(q["question"] + " (صح/خطأ): ")
    if user_answer == q["answer"]:
        print("صحيح! ")
        score += 1
    else:
        print("خطأ! ")

print(f"\nانتهت اللعبة! مجموع نقاطك: {score}/{len(questions)}")