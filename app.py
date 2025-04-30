import gradio as gr
from transformers import T5Tokenizer, T5ForConditionalGeneration
import requests
import pandas as pd
import os

# Load model
model = T5ForConditionalGeneration.from_pretrained("t5-small-finetuned-ai-news")
tokenizer = T5Tokenizer.from_pretrained("t5-small-finetuned-ai-news")

# Get API key
api_key = '2e5da21b90f74f65b69051e506278e54'

topics = [
    "artificial intelligence",
    "machine learning",
    "deep learning",
    "generative AI",
    "AI agents",
    "agentic AI"
]

def generate_summary(content):
    input_text = "summarize: " + content
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs.input_ids, max_length=128, num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def fetch_and_summarize_news():
    articles_list = []
    for topic in topics:
        url = f'https://newsapi.org/v2/everything?q={topic.replace(" ", "+")}&sortBy=publishedAt&language=en&apiKey={api_key}'
        response = requests.get(url)
        if response.status_code != 200:
            continue
        data = response.json()
        if data['status'] != 'ok':
            continue
        articles = data['articles'][:5]
        for article in articles:
            title = article.get("title")
            link = article.get("url")
            content = article.get("content", "")
            if not content or not title or not link:
                continue
            try:
                summary = generate_summary(content)
            except:
                summary = "Summary unavailable."
            articles_list.append({
                "Title": title,
                "Summary": summary,
                "URL": link,
                "Topic": topic
            })
    return pd.DataFrame(articles_list)

news_df = fetch_and_summarize_news()

def show_news():
    news_cards = ""
    for _, row in news_df.iterrows():
        news_cards += f"""
        <h3>{row['Title']}</h3>
        <i>{row['Topic']}</i><br>
        <p>{row['Summary']}</p>
        <a href="{row['URL']}" target="_blank">🔗 Read more</a>
        <hr>
        """
    return news_cards

def refresh_news():
    global news_df
    news_df = fetch_and_summarize_news()
    return show_news()

with gr.Blocks() as demo:
    gr.Markdown("## 🧠 AI News Aggregator (with Fine-Tuned Summaries)\n⏳ *Refreshing may take 1–2 minutes to generate real AI summaries*")
    output = gr.HTML(value=show_news())
    refresh_btn = gr.Button("🔄 Refresh News")
    refresh_btn.click(fn=refresh_news, inputs=[], outputs=output)

demo.launch(share=True)
