import google.generativeai as genai

genai.configure(api_key="AIzaSyASqRqit7G2B_n5oTGCoss7UDZ0xLmeNDc")

model = genai.GenerativeModel('gemini-2.5-flash')

chat_history = []

while True:
    q = input("You: ")
    chat_history.append(f"User: {q}")
    prompt = "\n".join(chat_history) + "\nAI:"
    response = model.generate_content(prompt)
    chat_history.append(f"AI: {response.text}")
    print(f"AI: {response.text}")
    if q.lower() == "exit":
        break