import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Initialize Groq client
client = Groq(
    api_key="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"
)

def get_groq_response(user_input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

# Route for the home page with the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the chat input
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_response = get_groq_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)
