import csv
import json
import random

# Sample CSV file path (replace this with your CSV file path)
csv_file_path = 'articles.csv'

def load_articles_from_csv(file_path):
    articles = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            articles.append({
                'id': int(row['id']),
                'text': row['text']
            })
    return articles

def fetch_random_articles(articles_list):
    # Choose two random articles from the list
    selected_articles = random.sample(articles_list, 2)
    return selected_articles

def handle_user_selection(event):
    # Extract user selections from the event data
    selected_article_ids = event['selected_article_ids']

    # Perform actions based on user selections (e.g., update user profile, store data)
    # For demonstration, print selected article IDs
    print("User selected articles:", selected_article_ids)

    # Return a response indicating successful processing
    return {
        'statusCode': 200,
        'body': json.dumps('User selection handled successfully')
    }

def lambda_handler(event, context):
    # Load articles from the CSV file
    articles = load_articles_from_csv(csv_file_path)

    # Check if the event contains user selections
    if 'selected_article_ids' in event:
        return handle_user_selection(event)

    # Fetch two random articles
    selected_articles = fetch_random_articles(articles)

    # Prepare response with the selected articles
    response = {
        'statusCode': 200,
        'body': json.dumps(selected_articles)
    }

    return response
