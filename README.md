# Project 4: Interactive Quiz Application (Python)

A console quiz game based on the "Code With AI Quiz" from Lecture 10.

## Description
The program shows five multiple-choice questions one at a time. The player types the number of an answer, gets instant feedback, and sees a final score at the end.

## Technologies
- Python17
- Standard library: `iostream`, `vector`, `string`, `limits`

## Features
- Five questions on AI, commit messages, unit tests, CSS, and time complexity
- Numbered options with input validation (rejects letters and out-of-range numbers)
- Instant feedback, showing the correct answer when you are wrong
- Final score, for example "Your score is 4 out of 5"
- Questions stored in a `struct` so new ones are easy to add

## Setup and Run
```
g++ -std=c++17 project4_interactive_quiz.cpp -o quiz
./quiz
```

## Example
```
Q3. What must a unit test do before the bug is fixed?
   1) Fail
   2) Pass
   3) Stop running
   4) Delete the code
Your answer (1-4): 1
Correct!
```

## Adding a Question
Add one more entry to the `questions` vector in `main`, with the question text, the four options, and the index (starting at 0) of the correct option.

## Notes
This is a console version. The original Lecture 10 quiz was built with HTML, CSS, and JavaScript, so this is a separate C++ rewrite and not the web quiz.

## Author
Prathvi Singh
