from question import Question

question_prompts = [
    "What color are apples? \n(a) Red/Green \n(b) black \n(c) blue\n\n",
    "What color are coals? \n(a) Red/Green \n(b) black \n(c) blue\n\n",
    "What color are blueberries? \n(a) Red/Green \n(b) black \n(c) blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + " out of " + str(len(questions)) + " right!")

run_test(questions)