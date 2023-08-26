import streamlit as st
import random

# Simple list of predefined responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing fine, thank you!", "All good, thanks!", "I'm great, and you?"],
    "what's your name": ["I'm a chatbot.", "I'm just a chatbot.", "You can call me Chatbot."],
    "bye": ["Goodbye!", "See you later!", "Have a nice day!"]
}

def get_response(input_text):
    input_text = input_text.lower()
    if input_text in responses:
        return random.choice(responses[input_text])
    else:
        return "I'm sorry, I don't understand that. Can you please try again?"

def main():
    st.title("Simple Chatbot")
    st.write("Ask me anything!")

    user_input = st.text_input("User Input:")
    if user_input:
        response = get_response(user_input)
        st.text_area("Chatbot:", value=response, height=100)

if __name__ == "__main__":
    main()
