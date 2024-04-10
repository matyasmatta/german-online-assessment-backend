# lambda_function.py

def lambda_handler(event, context):
    # Process incoming event (e.g., HTTP request)
    return {
        'statusCode': 200,
        'body': 'Hello from AWS Lambda!'
    }
