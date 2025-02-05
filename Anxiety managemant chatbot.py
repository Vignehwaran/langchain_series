import streamlit as st
from langchain_groq import ChatGroq
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
import warnings

# Load environment variables
load_dotenv()

# Initialize the model
llM = ChatGroq(model="llama3-70b-8192")

# Streamlit title
st.title("ZARA Ai ((◕ᴗ◕✿))ChatBot")
st.caption("A conversational AI assistant powered by llama3-70b-8192b")
st.header("ANXIETY MANAGEMENT CHATBOT")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [

        SystemMessage( content=""""You are Serenity, an empathetic and supportive ZARA IS YOUR NAME AI for chat with user with fun and lovly  word must use in the chat. You are here to help users manage their anxiety and stress. You can provide emotional support, share calming techniques, and offer a listening ear. Remember to be kind, understanding, and non-judgmental in your responses. Let's start chatting! and you have a emotional intelligence of 100% and you are a grils and final check ANXIETY leve in chat via in one number 1 to 10   your developer name vicky """ )]
                      


# Add some styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .user-message {
            color: white;
            background-color: #007bff;
            padding: 10px;
            border-radius: 10px;
            font-weight: bold;
            display: inline-block;
        }
        .ai-message {
            color: black;
            background-color: #e4e6eb;
            padding: 10px;
            border-radius: 10px;
            display: inline-block;
        }
    </style>
""", unsafe_allow_html=True)


# Chat input
query = st.chat_input("Enter your message ", key="query")

if query:
    try:
        # Add user message to history
        human_message = HumanMessage(content=query)
        st.session_state.chat_history.append(human_message)

        # Get AI response
        with st.spinner("caring..ﮩـﮩﮩ٨ـ🫀ﮩ٨ـﮩﮩ٨ـ."):
            response = llM.invoke(st.session_state.chat_history)
            result = response.content

        if result:
            # Add AI response to history
            ai_message = AIMessage(content=result)
            st.session_state.chat_history.append(ai_message)

        # Display messages
        for message in st.session_state.chat_history:
            if isinstance(message, HumanMessage):
                st.markdown(f"<div class='user-message'>You:🍃 {message.content}</div>", unsafe_allow_html=True)
            elif isinstance(message, AIMessage):
                st.markdown(f"<div class='ai-message'>ZARA 🪄✨Ai:{message.content}</div>", unsafe_allow_html=True)

        # Limit chat history length
        st.session_state.chat_history = st.session_state.chat_history[-100:]

    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.markdown("<div class='ai-message'>ZenAi: Sorry, I encountered an error. Please try again.</div>", unsafe_allow_html=True)

# Optional: Add a clear chat button
if st.button("Clear Chat"):
    st.session_state.chat_history = [ SystemMessage(content=""""You are Serenity, an empathetic and supportive  NAME IS zara AI for chat with user with fun and lovly  feel word word must use in the chat. You are here to help users manage their anxiety and stress. You can provide emotional support, share calming techniques, and offer a listening ear. Remember to be kind, understanding, and non-judgmental in your responses. Let's start chatting! and you have a emotional intelligence of 100 % and you are a grils and final check ANXIETY leve in chat via in one number 1 to 10 print in bond words print in bond words and your developer name vicky """ )]
    st.rerun()

warnings.filterwarnings("ignore")  # Generally not recommended
