# All 10 questions combined in one list
questions = [
    {'question': '1. Solve for x: 2x + 5 = 11.', 'answer': '3', 'options': ['4', '3', '2', '1']},
    {'question': '2. Find the perimeter of the rectangle with length 6cm and width 4cm.', 'answer': '20 cm', 'options': ['30 cm', '25 cm', '20 cm', '40 cm']},
    {'question': '3. What starts with an E, ends with an E, but only contains one letter.', 'answer': 'envelope'},
    {'question': '4. Two Truths and a Lie', 'answer': 'Humans only use 10 percent of their brain capacity.', 'options': ['The brain processes visual information faster than text-based information.', 'The average person has around 70,000 thoughts per day.', 'Humans only use 10 percent of their brain capacity.']},
    {'question': '5. How do introverts usually prefer to communicate?', 'answer': 'By texting or writing', 'options': ['By talking on the phone', 'By texting or writing', 'By video calls', 'In person only']},
    {'question': '6. A man is looking at a photograph of someone. His friend asks him, "Who is in the picture?" The man replies, "Brothers and sisters I have none, but that man\'s father is my father\'s son." Who is in the picture?', 'answer': 'His son', 'options': ['His son', 'His father', 'Himself', 'His uncle']},
    {'question': "7. Which element has the chemical symbol 'Au'?", 'answer': 'Gold', 'options': ['Gold', 'Silver', 'Iron', 'Copper']},
    {'question': "8. If you multiply me by any other number, the result will always be the same. What number am I?", 'answer': '0', 'options': ['0', '1', '2', '10']},
    {'question': "9. What is the next number in the sequence: 2, 6, 12, 20, 30?", 'answer': '42', 'options': ['42', '36', '50', '40']},
    {'question': "10. What is a six-letter word that can be written forward, backward, and upside down and still be read the same?", 'answer': 'SIXES', 'options': ['NOON', 'LEVEL', 'DEIFIED', 'SIXES']}
]
score = 0

def play_quiz():
    global score
    for question in questions:
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i+1}. {option}")
        
        player_ans = input("Enter the option number: ")
        
        if player_ans.isdigit() and 1 <= int(player_ans) <= len(question['options']):
            if question['options'][int(player_ans) - 1].lower() == question['answer'].lower():
                score += 1
                print("Correct!\n")
            else:
                print(f"Incorrect! The correct answer is: {question['answer']}\n")
        else:
            print("Invalid input! Moving to the next question.\n")
    
    print(f"Quiz over! You scored: {score}/{len(questions)}")

# Start the quiz
play_quiz()


