## 🌍 AI Trip Planner - Agentic AI System with LLMOPS

![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic-orange.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-red.svg)

---

## Key Features

| Feature                            | Description                                         |
| ---------------------------------- | --------------------------------------------------- |
| **Agentic Workflow**         | ReAct (Reasoning + Acting) loop using LangGraph     |
| **Real-time Weather**        | Current & forecast weather via OpenWeatherMap API   |
| **Currency Conversion**      | Live exchange rates via ExchangeRate API            |
| **Places Search**            | Google Places API with Tavily fallback              |
| **Expense Calculator**       | Hotel cost, daily budget, total expense calculation |
| **Modular Configuration**    | YAML-based model switching (Groq/OpenAI)            |
| **Containerized Deployment** | Docker + GitHub Actions CI/CD to AWS ECR/EC2        |

---

## Architecture

┌──────────────┐ ┌──────────────┐ ┌─────────────────────┐
│ Streamlit │────▶│ FastAPI │────▶│ LangGraph Agent │
│ (Frontend) │◀────│ (Backend) │◀────│ │
└──────────────┘ └──────────────┘ └──────────┬──────────┘
│
▼
┌─────────────────┐
│ Tools │
│ • Weather │
│ • Currency │
│ • Places │
│ • Expense │
└────────┬────────┘
│
▼
┌─────────────────┐
│ External APIs │
│ • OpenWeatherMap│
│ • ExchangeRate │
│ • Google Places │
│ • Groq/OpenAI │
└─────────────────┘

Tech Stack

| Layer           | Technology                                      |
| --------------- | ----------------------------------------------- |
| Frontend        | Streamlit                                       |
| Backend         | FastAPI                                         |
| Agent Framework | LangGraph                                       |
| LLM Providers   | Groq / OpenAI                                   |
| Tools           | OpenWeatherMap, ExchangeRate-API, Google Places |
| Deployment      | Docker, AWS ECR/EC2, GitHub Actions             |

---

## Quick Start

```bash
# Clone repository
git clone https://github.com/rajaD1995/AI_trip_planner.git
cd AI_trip_planner

# Create virtual environment
uv venv env --python 3.10
source env/bin/activate  # or env\Scripts\activate on Windows

# Install dependencies
uv pip install -r requirements.txt

# Run FastAPI (Terminal 1)
uvicorn main:app --reload --port 8000

# Run Streamlit (Terminal 2)
streamlit run streamlit_app.py**
```

---

## Sample Prompt

**text**

```
Plan a trip to Manali for 2 people in mid-July from Kolkata for 5 days, 
starting Monday. Journey included in 5 days.
```

---

## Contact

**Raja Debnath** - rajadebnath0619@gmail.com

[GitHub](https://github.com/rajaD1995) | [LinkedIn](https://www.linkedin.com/in/raja-debnath-1941b2118)
