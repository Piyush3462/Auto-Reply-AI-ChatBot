# WhatsApp Auto Reply AI Chatbot

This project is a Python-based WhatsApp Auto Reply Chatbot that generates intelligent, human-like responses using the Gemini API.

The bot automatically replies to incoming WhatsApp messages and can communicate in Gujarati, Hindi, and English. It is designed to simulate a real user by responding in a personalized conversational style.

## Features

- WhatsApp auto-reply system
- Multilangauge support (Gujarati, Hindi, English)
- AI-powered responses using Gemini API
- Human-like conversational behavior
- Personalized reply style (acts as the configured user)

## Tech Stack

- Python
- Gemini API (Google Generative AI)
- python-dotenv

## Installation

1. Clone the repository:

   git clone https://github.com/Piyush3462/Auto-Reply-AI-ChatBot.git  
   cd Auto-Reply-AI-ChatBot

2. Create virtual environment:

   python -m venv .venv  
   source .venv/bin/activate

3. Install dependencies:

   pip install -r requirements.txt

## Environment Setup

Create a `.env` file in the project root and add:

   GOOGLE_API_KEY=your_api_key_here

## Run

   python Main.py
