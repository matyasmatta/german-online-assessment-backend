import json
import csv

# Load JSON data from file
with open('articles.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Extract articles from JSON data
articles = data['articles']

# Define CSV file path
csv_file = 'articles.csv'

# Write articles data to CSV
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for article in articles:
        writer.writerow({'id': article['id'], 'text': article['text']})

print(f'CSV file generated successfully: {csv_file}')
