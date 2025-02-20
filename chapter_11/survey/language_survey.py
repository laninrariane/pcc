from survey import AnonymousServey


# Define a question and make a survey
question = "What langauge did you first learn to speak?"
language_survey = AnonymousServey(question)

# Show the question and store the responses
language_survey.show_question()
print("Enter 'q' at any time to quit\n")
while True:
    response = input("Language: ")
    if response == "q":
        break
    language_survey.store_response(response)

# Show survey results
print("\nThank you to everyone who participated in the survey")
language_survey.show_results()
