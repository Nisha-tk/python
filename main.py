from question_model import Question
from data import  question_data
from quiz_brain import QuizBrain
question_bank=[]

for  question in question_data:
    question_text= question["text"]
    question_answer=question["answer"]
    new_question=Question(text=question_text,answer=question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(q_list= question_bank)
while quiz.still_has_question():
    quiz.next_question()
print( "you have completed the quiz")
print(f" your Final score was  { quiz.score}/{ quiz.question_number}")
