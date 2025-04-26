#!/usr/bin/env python3
"""
Test file for s3_event_logger.py Lambda function
"""

import json
import unittest
import logging
from unittest.mock import patch, MagicMock
from s3_event_logger import lambda_handler

class TestS3EventLogger(unittest.TestCase):
    """Tests for S3 event logger Lambda function"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Sample S3 event
        self.event = {
            "Records": [
                {
                    "eventVersion": "2.1",
                    "eventSource": "aws:s3",
                    "awsRegion": "us-east-1",
                    "eventTime": "2023-01-01T12:00:00.000Z",
                    "eventName": "ObjectCreated:Put",
                    "userIdentity": {
                        "principalId": "EXAMPLE"
                    },
                    "requestParameters": {
                        "sourceIPAddress": "127.0.0.1"
                    },
                    "responseElements": {
                        "x-amz-request-id": "EXAMPLE123456789",
                        "x-amz-id-2": "EXAMPLE123/abcdef1234567890"
                    },
                    "s3": {
                        "s3SchemaVersion": "1.0",
                        "configurationId": "testConfigRule",
                        "bucket": {
                            "name": "test-bucket",
                            "ownerIdentity": {
                                "principalId": "EXAMPLE"
                            },
                            "arn": "arn:aws:s3:::test-bucket"
                        },
                        "object": {
                            "key": "test-object.txt",
                            "size": 1024,
                            "eTag": "0123456789abcdef0123456789abcdef",
                            "sequencer": "0A1B2C3D4E5F678901"
                        }
                    }
                }
            ]
        }
        
        # Empty context for Lambda
        self.context = {}
    
    @patch('s3_event_logger.logger')
    def test_lambda_handler_logs_event(self, mock_logger):
        """Test that lambda_handler logs the event correctly"""
        # Call the lambda handler
        result = lambda_handler(self.event, self.context)
        
        # Check that logger.info was called with the expected arguments
        mock_logger.info.assert_any_call('Received S3 event: ' + json.dumps(self.event))
        mock_logger.info.assert_any_call('Event: ObjectCreated:Put, Bucket: test-bucket, Key: test-object.txt')
        
        # Verify the return structure
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(json.loads(result['body']), 'Event processed successfully!')
    
    @patch('s3_event_logger.logger')
    def test_lambda_handler_handles_empty_event(self, mock_logger):
        """Test that lambda_handler handles an empty event gracefully"""
        empty_event = {"Records": []}
        
        # Call the lambda handler with empty event
        result = lambda_handler(empty_event, self.context)
        
        # Check logger.info was called with the event but not with details
        mock_logger.info.assert_called_with('Received S3 event: ' + json.dumps(empty_event))
        
        # Verify the function completed successfully
        self.assertEqual(result['statusCode'], 200)
    
    @patch('s3_event_logger.logger')
    def test_lambda_handler_handles_missing_fields(self, mock_logger):
        """Test that lambda_handler handles missing fields gracefully"""
        # Event with missing fields
        event_missing_fields = {
            "Records": [
                {
                    "eventName": "ObjectCreated:Put",
                    "s3": {
                        "bucket": {},
                        "object": {}
                    }
                }
            ]
        }
        
        # Call the lambda handler
        result = lambda_handler(event_missing_fields, self.context)
        
        # Check that logger.info was called with "unknown" for missing fields
        mock_logger.info.assert_any_call('Event: ObjectCreated:Put, Bucket: unknown, Key: unknown')
        
        # Verify the function completed successfully
        self.assertEqual(result['statusCode'], 200)

if __name__ == '__main__':
    unittest.main() 