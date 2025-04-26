import json
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, _):
    # Log the full event
    logger.info('Received S3 event: %s', json.dumps(event))
    
    # Extract and log key details
    for record in event.get('Records', []):
        bucket = record.get('s3', {}).get('bucket', {}).get('name', 'unknown')
        key = record.get('s3', {}).get('object', {}).get('key', 'unknown')
        event_name = record.get('eventName', 'unknown')
        
        logger.info('Event: %s, Bucket: %s, Key: %s', event_name, bucket, key)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Event processed successfully!')
    }   
