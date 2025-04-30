# 🧠 AI News Seeker

AI News Seeker is a real-time news aggregator that fetches and summarizes the latest updates in Artificial Intelligence, Machine Learning, Deep Learning, Generative AI, and Agentic AI — all in one smart, clean web app.

Live Demo 👉 [Try the App on Hugging Face](https://huggingface.co/spaces/AbbasN21/Ai-News-Seeker)

---

## 🚀 Features

- 📥 **Live News Fetching** from [NewsAPI](https://newsapi.org/)
- 🧠 **Custom AI Summarization** using a fine-tuned `T5-small` transformer model
- 🖥️ **Interactive Web UI** built with [Gradio](https://gradio.app/)
- 🔄 **Refresh Button** to fetch and summarize new articles on demand
- 📎 Clickable links to original sources

---

## 🛠️ Tech Stack

- `Python 3.11+`
- `Hugging Face Transformers` (for fine-tuning T5-small)
- `Gradio` (interactive frontend)
- `NewsAPI` (real-time article source)
- `Hugging Face Spaces` (live deployment)
- `SQLite` (optional local storage during dev)

---

## 🧩 How It Works

1. The app fetches the 5 latest news articles for each topic:
   - Artificial Intelligence
   - Machine Learning
   - Deep Learning
   - Generative AI
   - AI Agents
   - Agentic AI
2. The fine-tuned T5 model generates a summary for each article.
3. The Gradio interface displays the Title, Topic, Summary, and a direct link.

> **Note:** Refreshing can take 1–2 minutes due to live AI summarization.

---

## 📂 Folder Structure

ai-news-seeker/ ├── app.py # Main Gradio app logic ├── requirements.txt # Required Python packages ├── README.md # This file └── t5-small-finetuned-ai-news/ # Your trained model folder
