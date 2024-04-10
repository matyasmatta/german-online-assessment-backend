import csv
import json
import random
import boto3
import io

# Initialize S3 client
s3 = boto3.client('s3')

# Sample S3 bucket and key (replace these with your S3 bucket and CSV file key)
s3_bucket_name = 'german-assessment-data'
s3_file_key = 'database.csv'

def load_articles_from_csv(s3_bucket, s3_key):
    articles = []
    try:
        # Retrieve CSV file from S3
        response = s3.get_object(Bucket=s3_bucket, Key=s3_key)
        csv_data = response['Body'].read().decode('utf-8')

        # Parse CSV data
        csv_reader = csv.DictReader(io.StringIO(csv_data))
        for row in csv_reader:
            articles.append({
                'id': int(row['id']),
                'text': row['text']
            })

        return articles

    except Exception as e:
        # Handle exceptions (e.g., S3 access errors)
        print(f"Error loading articles from S3: {str(e)}")
        return []

def fetch_random_articles(articles_list):
    # Choose two random articles from the list
    selected_articles = random.sample(articles_list, 2)
    return selected_articles

def handle_user_selection(event):
    # Extract user selections from the event data
    selected_article_ids = event['selected_article_ids']
    user_key = event['user_key']
    time_val = event['time']

    # Perform actions based on user selections (e.g., update user profile, store data)
    # For demonstration, print selected article IDs
    print("User selected articles:", selected_article_ids)
    write_into_database(time_val, user_key, selected_article_ids)

    # Return a response indicating successful processing
    return {
        'statusCode': 200,
        'body': json.dumps('User selection handled successfully')
    }

def write_into_database(time_val, key, data):
    with open("database.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([time_val, key, data])

def lambda_handler(event, context):
    # Load articles from the specified S3 bucket and key
    articles = load_articles_from_csv(s3_bucket_name, s3_file_key)

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
