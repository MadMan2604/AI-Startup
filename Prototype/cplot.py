import requests

def send_message(message):
    api_url = "http://127.0.0.1:5000/chat"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "message": message
    }
    response = requests.post(api_url, headers=headers, json=data)
    return response.json().get('response')

if __name__ == '__main__':
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = send_message(user_input)
        print(f"Gemini: {response}")
