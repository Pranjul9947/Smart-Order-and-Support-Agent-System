
# 🧠 AI Multi-Agent Order & Feedback System

A modular, LLM-powered multi-agent system built with LangChain and OpenRouter (Mistral) that enables customers to:
- 📦 Place orders
- 📧 Receive email confirmations
- 💬 Interact with a customer support chatbot
- 📝 Provide feedback that is analyzed with real-time sentiment analysis
- 📊 View analytics from feedback and order logs

---

## 📌 Features

- **LangChain agents** for handling distinct responsibilities (Order, Feedback, Chat, Analysis)
- **Sentiment analysis** via OpenRouter API (Mistral 7B)
- **CSV-based logs** (`orders.csv`, `feedback.csv`) for later analysis
- **Live data visualization** using pandas, seaborn, and matplotlib
- **Streamlit-based UI** for deployment and usage
- **Email confirmation** sent upon order (requires SMTP setup)

---

## 📁 Project Structure

```
📦 multi-agent-order-feedback
├── main.py
├── agents/
│   ├── order_agent.py
│   ├── feedback_agent.py
│   ├── chatbot_agent.py
│   ├── analysis_agent.py
├── data/
│   ├── orders.csv
│   └── feedback.csv
├── .env
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation & Setup

1. **Create a Conda environment**
   ```bash
   conda create -n multiagent-llm python=3.10
   conda activate multiagent-llm
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your API Key**  
   Create a `.env` file in the root folder:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

4. **Run the app**
   ```bash
   streamlit run main.py
   ```

---

## 🔍 How It Works

| Agent | Function |
|-------|----------|
| `order_agent.py` | Takes customer name, item, quantity, and stores in `orders.csv`. Sends confirmation email. |
| `feedback_agent.py` | Collects feedback, calls OpenRouter API for sentiment (Positive/Negative/Neutral), logs to `feedback.csv`. |
| `chatbot_agent.py` | Provides basic LLM-powered responses to customer questions. |
| `analysis_agent.py` | Uses pandas, matplotlib, and seaborn to generate visualizations and reports from data logs. |

---

## 📬 Email Setup (Optional)

Update your `order_agent.py` with the following:
```python
EMAIL_ADDRESS = "youremail@example.com"
EMAIL_PASSWORD = "your_app_password"
```
Use services like Gmail with "App Password" enabled.

---

## 📈 Sample Analysis

- Sentiment distribution bar graph
- Ratings over time line chart
- Order count and delivery estimate graphs

---

## 📌 Future Scope

- Vector memory with LangGraph
- Database integration (SQLite, MongoDB)
- Multilingual support
- Authenticated customer dashboards

---

## 📚 References

- [LangChain](https://docs.langchain.com)
- [OpenRouter (Mistral)](https://openrouter.ai)
- [Streamlit](https://streamlit.io)
- [Matplotlib, Seaborn, Pandas]
