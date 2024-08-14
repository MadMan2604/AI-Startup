from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_gemini_response(user_input)
    return jsonify({'response': response})

def get_gemini_response(message):
    api_url = "https://api.gemini.com/v1/chat"
    headers = {
        "Authorization": f"Bearer YOUR_API_KEY",
        "Content-Type": "application/json"
    }
    data = {
        "message": message
    }
    response = requests.post(api_url, headers=headers, json=data)
    return response.json().get('response')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
