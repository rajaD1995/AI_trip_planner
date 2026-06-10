```

# 🌍 AI Trip Planner - Agentic AI System with LLMOPS

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Agentic-orange.svg)](https://www.langchain.com/langgraph)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Overview

**AI Trip Planner** is an end-to-end agentic AI application that helps users plan their trips using natural language. It leverages **LangGraph** for multi-agent orchestration, integrates real-time tools (weather, currency, places search, expense calculator), and provides a responsive chat interface via **Streamlit** with a **FastAPI** backend.

### 🎯 Key Features

| Feature | Description |
|---------|-------------|
| 🤖 **Agentic Workflow** | ReAct (Reasoning + Acting) loop using LangGraph |
| 🌤️ **Real-time Weather** | Current & forecast weather via OpenWeatherMap API |
| 💱 **Currency Conversion** | Live exchange rates via ExchangeRate API |
| 🏨 **Places Search** | Google Places API with Tavily fallback |
| 💰 **Expense Calculator** | Hotel cost, daily budget, total expense calculation |
| ⚙️ **Modular Configuration** | YAML-based model switching (Groq/OpenAI) |
| 🐳 **Containerized Deployment** | Docker + GitHub Actions CI/CD to AWS ECR/EC2 |

---

## 🏗️ Architecture
```

┌─────────────┐ ┌─────────────┐ ┌─────────────────────────────────┐
│ Streamlit │────▶│ FastAPI │────▶│ LangGraph Agent │
│ (Frontend) │◀────│ (Backend) │◀────│ │
└─────────────┘ └─────────────┘ │ ┌──────┐ ┌──────┐ ┌──────┐ │
│ │Weather│ │Currency│ │Places│ │
│ └──────┘ └──────┘ └──────┘ │
│ ┌──────────────┐ │
│ │ Expense │ │
│ │ Calculator │ │
│ └──────────────┘ │
└─────────────────────────────────┘

**text**

```

### Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| Backend API | FastAPI |
| Agent Framework | LangGraph |
| LLM Providers | Groq (DeepSeek) / OpenAI (GPT-4o-mini) |
| Tools | OpenWeatherMap, ExchangeRate-API, Google Places, Tavily |
| Deployment | Docker, AWS ECR, AWS EC2, GitHub Actions |

---

## 📁 Project Structure
```

AI_Trip_Planner/
├── agent/
│ └── agentic_workflow.py # LangGraph graph builder
├── tools/
│ ├── weather_info_tool.py
│ ├── currency_conversion_tool.py
│ ├── place_search_tool.py
│ └── expense_calculator_tool.py
├── utils/
│ ├── weather_info.py
│ ├── currency_converter.py
│ ├── place_info_search.py
│ ├── expense_calculator.py
│ ├── model_loader.py
│ └── save_to_document.py
├── config/
│ └── config.yaml
├── prompt_library/
│ └── prompt.py
├── main.py
├── streamlit_app.py
├── requirements.txt
├── Dockerfile
├── .env
└── .github/workflows/deploy.yml

**text**

```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- UV (fast package manager) or pip
- API Keys (see below)

### Step 1: Clone Repository

```bash
git clone https://github.com/rajaD1995/AI_trip_planner.git
cd AI_trip_planner
```

### Step 2: Set Up Virtual Environment

**bash**

```
# Install UV (if not installed)
pip install uv

# Create virtual environment with Python 3.10
uv venv env --python 3.10

# Activate on Windows
env\Scripts\activate.bat

# Activate on macOS/Linux
source env/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

### Step 3: Configure API Keys

Create `.env` file in project root:

**bash**

```
# .env
OPENWEATHERMAP_API_KEY=your_openweather_key
EXCHANGE_RATE_API_KEY=your_exchangerate_key
GPLACES_API_KEY=your_google_places_key
GROQ_API_KEY=your_groq_key
OPENAI_API_KEY=your_openai_key
```

### Step 4: Configure LLM Provider

Edit `config/config.yaml`:

**yaml**

```
llm:
  active_model: "groq"   # or "openai"

  groq:
    provider: "groq"
    model_name: "deepseek-r1-distill-llama-70b"

  openai:
    provider: "openai"
    model_name: "o4-mini"
```

### Step 5: Run Application

**Terminal 1 - FastAPI Backend:**

**bash**

```
uvicorn main:app --reload --port 8000
```

**Terminal 2 - Streamlit Frontend:**

**bash**

```
streamlit run streamlit_app.py
```

Open browser to `http://localhost:8501`

---

## 💬 Sample Prompts

Copy and try these examples:

**text**

```
Plan a trip to Goa for 5 days with ₹50000 budget

What's the weather in Manali?

Convert 100 USD to INR

Calculate daily budget for 7 days in Dubai with total ₹70000

Plan a trip to Manali for 2 people in mid-July from Kolkata for 5 days, starting Monday. Journey included in 5 days.
```
