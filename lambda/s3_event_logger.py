import json
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Log the full event
    logger.info('Received S3 event: ' + json.dumps(event))
    
    # Extract and log key details
    for record in event.get('Records', []):
        bucket = record.get('s3', {}).get('bucket', {}).get('name', 'unknown')
        key = record.get('s3', {}).get('object', {}).get('key', 'unknown')
        event_name = record.get('eventName', 'unknown')
        
        logger.info(f'Event: {event_name}, Bucket: {bucket}, Key: {key}')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Event processed successfully!')
    } 