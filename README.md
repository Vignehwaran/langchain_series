# Anxiety Management Bot using LangChain & Groq API

## Overview
The **Anxiety Bot** is an AI-powered chatbot designed to help users manage anxiety by providing calming conversations, mindfulness techniques, and helpful resources. It leverages **LangChain** for efficient AI agent orchestration and **Groq API** for fast and cost-effective LLM-based responses.

## Features
- 🧘 Provides personalized anxiety management techniques.
- 💬 Engages in calming and supportive conversations.
- 📖 Shares mental health resources and exercises.
- ⚡ Built using LangChain for seamless AI interaction.
- 🚀 Powered by Groq API for efficient natural language processing.

## Tech Stack
- **Python** (Backend)
- **LangChain** (AI Agent Framework)
- **Groq API** (LLM API)
- **Streamlit** (Web Interface, Optional)

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/anxiety-bot.git
   cd anxiety-bot
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up API Keys**
   - Get a **Groq API Key** from [Groq](https://groq.com/).
   - Create a `.env` file and add:
     ```env
     GROQ_API_KEY=your_api_key_here
     ```

## Usage
Run the chatbot using:
```bash
python app.py
```
For a web-based interface, run the Streamlit app:
```bash
streamlit run app.py
```

## Example Interaction
```
User: I'm feeling anxious today.
Bot: I'm here for you. Take a deep breath and try this mindfulness exercise: Close your eyes, inhale deeply for 4 seconds, hold for 4 seconds, and exhale for 4 seconds. Repeat a few times and let me know how you feel. 💙
```

## Future Enhancements
- ✅ Voice-enabled chatbot integration
- ✅ More personalized conversation models
- ✅ Integration with mental health APIs

## Contributing
Pull requests are welcome! Feel free to open an issue for feature requests or bug fixes.

## License
This project is licensed under the **MIT License**.

---
Developed with ❤️ to support mental well-being!"# langchain_series" 
