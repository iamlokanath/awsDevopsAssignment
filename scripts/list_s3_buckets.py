#!/usr/bin/env python3
"""
Script to interact with AWS S3 using boto3:
- Lists all S3 buckets in your AWS account
- Displays the total number of objects in a specified S3 bucket
"""

import boto3
import sys
import argparse

def list_all_buckets():
    """List all S3 buckets in the AWS account"""
    try:
        # Create an S3 client
        s3 = boto3.client('s3')
        
        # Get all buckets
        response = s3.list_buckets()
        
        # Print bucket info
        print("S3 Buckets in your AWS account:")
        print("-" * 40)
        if not response['Buckets']:
            print("No buckets found.")
            return
        
        for i, bucket in enumerate(response['Buckets'], 1):
            print(f"{i}. {bucket['Name']} (Created: {bucket['CreationDate']})")
            
        print(f"\nTotal buckets: {len(response['Buckets'])}")
    
    except Exception as e:
        print(f"Error listing buckets: {e}")
        sys.exit(1)

def count_objects_in_bucket(bucket_name):
    """Count objects in a specified S3 bucket"""
    try:
        # Create an S3 client
        s3 = boto3.client('s3')
        
        # Check if bucket exists
        try:
            s3.head_bucket(Bucket=bucket_name)
        except Exception as e:
            print(f"Error: Bucket '{bucket_name}' does not exist or you don't have access to it.")
            return
        
        # List all objects in the bucket
        paginator = s3.get_paginator('list_objects_v2')
        total_objects = 0
        total_size = 0
        
        print(f"\nObjects in bucket '{bucket_name}':")
        print("-" * 40)
        
        for page in paginator.paginate(Bucket=bucket_name):
            if 'Contents' in page:
                total_objects += len(page['Contents'])
                # Sum up the size of all objects
                for obj in page['Contents']:
                    total_size += obj['Size']
        
        # Convert size to a readable format
        size_str = format_size(total_size)
            
        print(f"Total objects: {total_objects}")
        print(f"Total size: {size_str}")
    
    except Exception as e:
        print(f"Error counting objects: {e}")
        sys.exit(1)

def format_size(size_bytes):
    """Format bytes to a human-readable size"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='AWS S3 Bucket and Object Management')
    parser.add_argument('--bucket', '-b', type=str, help='Specify a bucket name to count objects')
    
    args = parser.parse_args()
    
    # List all buckets
    list_all_buckets()
    
    # If a bucket name is provided, count objects in that bucket
    if args.bucket:
        count_objects_in_bucket(args.bucket)

if __name__ == "__main__":
    main() 