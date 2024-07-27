from flask import Flask, request, jsonify
import os
import sys

# Add the path to the extracted files
sys.path.append('/mnt/data/Limitless-main/Limitless-main')

# Import the necessary functions from the provided Python files
from questionsGenerator import generate_followup_questions
from prompter import get_final_decision

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')

    # Generate follow-up questions using the provided function
    followup_questions = generate_followup_questions(question)

    return jsonify({"followup_questions": followup_questions})

@app.route('/submit_answers', methods=['POST'])
def submit_answers():
    data = request.json
    answers = data.get('answers')

    # Generate the final decision using the provided function
    response = get_final_decision(answers)

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
