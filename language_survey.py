from survey import AnoymousSurvey

#Define a question and make a survey
question = "What langueage did you learn to speak first ? "
my_survey = AnoymousSurvey(question)

#show the question, store responses to the question
my_survey.show_question()
print("Enter 'q' anytime to quit.\n")
while True:
    response = input("Language : ")
    if response == 'q':
        break
    my_survey.store_response((response))

#show the survey results
print("\nThank you everyone for participating!!!")
my_survey.show_result()
