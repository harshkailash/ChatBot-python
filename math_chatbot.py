import csv
import nltk
from nltk.chat.util import Chat, reflections

def load_chat_data(file_path):
    patterns = []
    responses = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            patterns.append((row['pattern'], row['response'].split(',')))
    
    return patterns

# Specify the path to your CSV file
csv_file_path = 'chat_data.csv'

# Load patterns from the CSV file
loaded_patterns = load_chat_data(csv_file_path)

# Create a Chat instance with the loaded patterns
chatbot = Chat(loaded_patterns, reflections)

# Define a function to handle math expressions and return the result
def evaluate_math_expression(expression):
    try:
        result = eval(expression)
        return f'The result is: {result}'
    except Exception as e:
        return f'Error: {str(e)}'

# Create a custom response function for the chatbot
def chatbot_response(user_input):
    # Check if the input is a math expression
    if any(char.isdigit() for char in user_input):
        return evaluate_math_expression(user_input)
    else:
        return chatbot.respond(user_input)

# Main loop to get user input and generate responses
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    response = chatbot_response(user_input)
    print("ChatBot:", response)