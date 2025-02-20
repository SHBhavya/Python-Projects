# All 10 questions combined in one list
questions = [
    {'question': '😊 What is the output of print(2 ** 3)?', 'answer': '8', 'options': ['6', '8', '9', '16']},
    {'question': '😘 Which data type is mutable in Python?', 'answer': 'List', 'options': ['Tuple', 'String', 'List', 'Set']},
    {'question': '🤗 What is the correct way to start a function in Python?', 'answer': 'def my_function():', 'options': ['func my_function():', 'def my_function():', 'function my_function():', 'define my_function():']},
    {'question': '😎 What will be the output of print(10 // 3)?', 'answer': '3', 'options': ['3', '3.33', '4', '10']},
    {'question': '😃 How do you take user input in Python?', 'answer': 'input()', 'options': ['scanf()', 'cin>>', 'input()', 'gets()']},
    {'question': '😚 What is the correct way to write a comment in Python?', 'answer': '# This is a comment', 'options': ['// This is a comment', '# This is a comment', '/* This is a comment */', '-- This is a comment']},
    {'question': '😆 Which keyword is used to create a loop in Python?', 'answer': 'for', 'options': ['loop', 'repeat', 'for', 'do while']},
    {'question': '🥺 What is the result of len("Python")?', 'answer': '6', 'options': ['5', '6', '7', '8']},
    {'question': '🤥 What does the `append()` method do in Python?', 'answer': 'Adds an element to the end of a list', 'options': ['Removes an element', 'Adds an element to the end of a list', 'Sorts the list', 'Reverses the list']},
    {'question': '😂 What will `print(type(3.14))` output?', 'answer': '<class \'float\'>', 'options': ['<class \'int\'>', '<class \'float\'>', '<class \'str\'>', '<class \'list\'>']}
]

score = 0
def play_quiz():
    global score
    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f'{i + 1}📌 {option}')
        player_answer = int(input('Enter the correct option number 🫣  >> '))
        if 1 <= player_answer <= len(question['options']):
            if question['options'][player_answer - 1].lower() == question['answer'].lower():
                score += 1
            else:
                print(f"🫡 Incorrect! The correct answer is: {question['answer']} 🤫\n")
        else:
            print("😵 Invalid input! Moving to the next question. 😐\n")
    print(f"😇 Quiz over! \nYou scored: {score}/{len(questions)} 🙃\n😃 Thanks for using Bhavya Softwares! 🤗")
play_quiz()


