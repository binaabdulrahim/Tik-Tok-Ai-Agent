import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain.agents import Tool, initialize_agent, AgentType
from langchain_community.utilities import SerpAPIWrappe

st.title("AI TikTok Agent")

with st.sidebar:
    st.header("Keys & Settings")

    # API Keys
    groq_api_key = st.text_input("Groq API Key", type="password")
    serpapi_key = st.text_input("SerpAPI Key (for Google Search)", type="password")

    # LLM model
    model = st.selectbox("Choose Model", ["llama3-8b-8192", "llama3-70b-8192"])

    # Search toggle
    enable_search = st.checkbox("Use Google Search (SerpAPI)", value=True)