#!/usr/bin/env python3
"""
Script to interact with AWS S3 using boto3:
- Lists all S3 buckets in your AWS account
- Displays the total number of objects in a specified S3 bucket
"""

import argparse
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

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
            return True
        
        for i, bucket in enumerate(response['Buckets'], 1):
            print(f"{i}. {bucket['Name']} (Created: {bucket['CreationDate']})")
            
        print(f"\nTotal buckets: {len(response['Buckets'])}")
        return True
    
    except ClientError as e:
        error_code = e.response.get('Error', {}).get('Code', 'Unknown')
        error_message = e.response.get('Error', {}).get('Message', str(e))
        print(f"AWS Error ({error_code}): {error_message}")
        print("\nPossible causes:")
        print("- Your IAM user doesn't have permission to list all buckets")
        print("- Your AWS credentials are invalid or expired")
        return False
    except NoCredentialsError:
        print("Error: No AWS credentials found. Please configure AWS credentials.")
        print("Run 'aws configure' to set up your credentials.")
        return False
    except Exception as e:  # pylint: disable=W0718
        print(f"Unexpected error listing buckets: {e}")
        return False

def count_objects_in_bucket(bucket_name):
    """Count objects in a specified S3 bucket"""
    try:
        # Create an S3 client
        s3 = boto3.client('s3')
        
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
        return True
    
    except ClientError as e:
        error_code = e.response.get('Error', {}).get('Code', 'Unknown')
        error_message = e.response.get('Error', {}).get('Message', str(e))
        print(f"\nCannot access bucket '{bucket_name}'")
        print(f"AWS Error ({error_code}): {error_message}")
        print("\nPossible causes:")
        print("- The bucket doesn't exist")
        print("- You don't have permission to access this bucket")
        print("- Your AWS credentials are invalid or expired")
        return False
    except NoCredentialsError:
        print("Error: No AWS credentials found. Please configure AWS credentials.")
        print("Run 'aws configure' to set up your credentials.")
        return False
    except Exception as e:  # pylint: disable=W0718
        print(f"Unexpected error counting objects: {e}")
        return False

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
    parser.add_argument('--profile', '-p', type=str, help='AWS profile name to use')
    
    args = parser.parse_args()
    
    # Use a specific profile if provided
    if args.profile:
        boto3.setup_default_session(profile_name=args.profile)
    
    # List all buckets
    buckets_listed = list_all_buckets()
    
    # If a bucket name is provided and we could list buckets, count objects in that bucket
    if args.bucket and buckets_listed:
        count_objects_in_bucket(args.bucket)
    elif args.bucket:
        # Try to directly access the bucket even if we couldn't list all buckets
        print("\nTrying to directly access the specified bucket...")
        count_objects_in_bucket(args.bucket)

if __name__ == "__main__":
    main()
