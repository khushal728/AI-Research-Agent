# 🚀 AI Research Agent

## 🔍 Overview

The AI Research Agent is a dual-agent system designed for deep research and automated content summarization. It uses Tavily for web crawling, Cohere for summarization, and Google Gemini for structured answer generation. The system is implemented using LangGraph and LangChain, with a Streamlit interface for user interaction.

## ✨ Features

🕵️ Automated Web Crawling: Uses Tavily to fetch relevant articles based on a user's query.

📄 Summarization Agent: Extracts key insights from fetched articles using Cohere.

🤖 Answer Generation Agent: Generates structured responses using Google Gemini.

🎨 Streamlit UI: Provides a user-friendly interface for query input and result display.

## 🛠 Technologies Used

🐍 Python

🔗 LangChain & LangGraph

🌐 Tavily API

✍️ Cohere API

⚡ Google Gemini API

📊 Streamlit

## 👅 Installation

1. Clone the repository:
```
git clone https://github.com/your-repo/ai-research-agent.git
cd ai-research-agent
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Set environment variables:
```
export TAVILY_API_KEY="your_tavily_api_key"
export COHERE_API_KEY="your_cohere_api_key"
export GOOGLE_API_KEY="your_google_gemini_api_key"
```
## ▶️ Running the Application
```
streamlit run AIResearchAgent.py
```

## 🚀 Deployment

To deploy the application, use Streamlit Cloud, Render, or Hugging Face Spaces. Ensure all dependencies are installed and API keys are securely managed.

## 📝 Usage

🔍 Enter a research query in the Streamlit UI.

🚀 Click Run Research.

📁 View research summaries and the final AI-generated response.

## 🚀 Future Enhancements

📈 Improve summarization accuracy with fine-tuned models.

🔎 Optimize search results filtering.

🧠 Add support for multiple AI models.

## 🐟 License

This project is open-source under the MIT License.





















