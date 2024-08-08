#!pip install python-telegram-bot==13.7

import logging
import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


from elasticsearch import Elasticsearch
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)

es_client = Elasticsearch('http://localhost:9200') 


def elastic_search(query, index_name = "course-questions"):
    search_query = {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields"
                    }
                },
                "filter": {
                    "term": {
                        "course": "data-engineering-zoomcamp"
                    }
                }
            }
        }
    }

    response = es_client.search(index=index_name, body=search_query)
    
    result_docs = []
    
    for hit in response['hits']['hits']:
        result_docs.append(hit['_source'])
    
    return result_docs


def build_prompt(query, search_results):
    prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT: 
{context}
""".strip()

    context = ""
    
    for doc in search_results:
        context = context + f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}\n\n"
    
    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt

def llm(prompt):
    response = client.chat.completions.create(
        model='phi3',
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content


def rag(query):
    search_results = elastic_search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    return answer




# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Command handler for /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Send me a query and I'll process it for you.")

# Command handler for /help
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Send me a message with your query, and I will process it.")

# Function to handle text messages
def handle_message(update: Update, context: CallbackContext):
    query = update.message.text
    update.message.reply_text("Processing your query, please wait...")
    
    # Simulate processing and get result from rag_function
    result = rag(query)
    
    # Send result back to user
    update.message.reply_text(result)

def main():
    # Replace 'YOUR_TOKEN' with your actual bot token
    updater = Updater("", use_context=True)

    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Add message handler
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
