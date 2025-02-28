
import os
import requests
import cohere
import streamlit as st
from tavily import TavilyClient
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langgraph.graph import StateGraph, END


# -

# Set API Keys
os.environ["TAVILY_API_KEY"] = "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"
os.environ["COHERE_API_KEY"] = "7gASb38xz7rJYESOJs0JunSLzfTgqHvbbav8tFiQ"
os.environ["GOOGLE_API_KEY"] = "AIzaSyBtsj5HlYcv_c-TSa82jOMwXq5N2Xc1PNo"


# +
# Initialize clients
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def research_agent(state):
    query = state["query"]  # Fetch query from state

    # Tavily search
    search_results = tavily_client.search(query=query, num_results=3)
    urls = [result["url"] for result in search_results["results"]]

    extracted_texts = []
    for url in urls:
        try:
            response = requests.get(url)
            extracted_texts.append(response.text[:1000])  # Limit text size
        except:
            extracted_texts.append("Failed to fetch content.")

    # Summarization
    summaries = []
    for text in extracted_texts:
        try:
            response = co.summarize(text=text, length="medium")
            summaries.append(response.summary)
        except:
            summaries.append("Failed to summarize.")

    return {"query": query, "summaries": summaries}  # ✅ Return a dictionary

def answer_agent(state):
    summaries = state["summaries"]  # Get summaries from dictionary

    prompt = PromptTemplate(
        input_variables=["summaries"],
        template="Based on the following research summaries, generate a structured and detailed answer:\n{summaries}"
    )

    # Use Gemini API
    llm = GoogleGenerativeAI(model="gemini-2.0-pro-exp", google_api_key=os.getenv("GOOGLE_API_KEY"))
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    response = llm_chain.run(summaries)
    return {"query": state["query"], "summaries": summaries, "answer": response}  # ✅ Return a dictionary

graph = StateGraph(dict)
graph.add_node("research_agent", research_agent)
graph.add_node("answer_agent", answer_agent)
graph.set_entry_point("research_agent")
graph.add_edge("research_agent", "answer_agent")
graph.add_edge("answer_agent", END)
agent_executor = graph.compile()


# Streamlit UI
st.title("AI Research Agent")
user_query = st.text_input("Enter your research query:")

if st.button("Run Research"):
    if user_query:
        initial_state = {"query": user_query, "summaries": None, "answer": None}
        result = agent_executor.invoke(initial_state)
        
        st.subheader("Research Summaries")
        for summary in result["summaries"]:
            st.write(summary)
        
        st.subheader("Final Answer")
        st.write(result["answer"])



