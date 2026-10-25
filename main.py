"""Project 4: Interactive Quiz Application
Console version of the "Code With AI Quiz" from Lecture 10.
"""

QUESTIONS = [
    {
        "question": "What does a large language model actually predict?",
        "options": ["The next token", "The entire paragraph", "The final answer", "The user's intention"],
        "answer": "The next token",
    },
    {
        "question": "In the commit-message format used in this course, what comes before the colon?",
        "options": ["The type, such as feat or fix", "The filename", "The programmer name", "The date"],
        "answer": "The type, such as feat or fix",
    },
    {
        "question": "What must a unit test do before the bug is fixed?",
        "options": ["Fail", "Pass", "Stop running", "Delete the code"],
        "answer": "Fail",
    },
    {
        "question": "Where should the styling for a webpage live?",
        "options": ["In a separate CSS file", "Inside Python", "Inside the browser console", "Inside a text file"],
        "answer": "In a separate CSS file",
    },
    {
        "question": "What does a loop inside another loop usually mean for time complexity?",
        "options": ["It is quadratic", "It is constant", "It is logarithmic", "It has no complexity"],
        "answer": "It is quadratic",
    },
]


def ask_choice(count):
    """Ask until the user enters a number from 1 to count."""
    while True:
        try:
            choice = int(input(f"Your answer (1-{count}): "))
            if 1 <= choice <= count:
                return choice
        except ValueError:
            pass
        print("Invalid choice, try again.")


def run_quiz(questions):
    score = 0
    print("=== Code With AI Quiz ===\n")

    for number, q in enumerate(questions, start=1):
        print(f"Q{number}. {q['question']}")
        for i, option in enumerate(q["options"], start=1):
            print(f"   {i}) {option}")

        selected = q["options"][ask_choice(len(q["options"])) - 1]
        if selected == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. Correct answer: {q['answer']}\n")

    print("Quiz Complete")
    print(f"Your score is {score} out of {len(questions)}")
    return score


if __name__ == "__main__":
    run_quiz(QUESTIONS)
